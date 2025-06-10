# Displaying an updating path of a user’s location history

**Framework**: MapKit

Continually update a MapKit overlay displaying the path a user travels.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Xcode 16.0+

#### Overview

Travel History is a sample app that allows a user to track their location history, and displays a live-updating path of that history on a map. The app combines location updates from Core Location with a custom MapKit overlay for the location history. MapKit draws the user’s path using a custom MapKit overlay renderer.

For this sample app to show a path, it needs to receive a stream of location updates. Install the app on a device, and take a walk with it recording locations. Alternately, use one of the routes in the iOS simulator, such as Freeway Drive or City Bicycle Ride. To set a route in the iOS simulator, see [`Set a location or route`](https://developer.apple.comhttps://help.apple.com/simulator/mac/current/#/devc6eac95d6).

##### Configure a Location Manager to Receive Location Updates

Before recording the user’s path, the app asks the user for permission to access location data while the app is running. After the user grants location authorization, a `CLLocationManager` receives a stream of location updates as the user travels. The app also receives location updates while in the background by setting the `allowsBackgroundLocationUpdates` property of [`CLLocationManager`](https://developer.apple.com/documentation/CoreLocation/CLLocationManager) to `true`. This combination of when-in-use authorization and background updates allows the app to receive location updates while in the background, and the system displays a location service indicator when the app isn’t in the foreground.

```swift
locationManager.requestWhenInUseAuthorization()

/// Enable the app to collect location updates while it's in the background.
locationManager.allowsBackgroundLocationUpdates = true
```

The app sets a default value for the [`desiredAccuracy`](https://developer.apple.com/documentation/CoreLocation/CLLocationManager/desiredAccuracy) property on the location manager. This value is customizable in a menu to demonstrate how the value of this property affects the accuracy of the recorded data. Lower accuracy values allow the device to conserve power and have less impact on the device’s battery life. For example, if this app is for hiking, it needs high-accuracy data to capture a detailed path for the user’s hiking route, requiring `kCLLocationAccuracyBest` to facilitate the required detail. In contrast, if the app tracks overall progress between a start and end point without needing the exact path taken, using a lower accuracy value, such as `kCLLocationAccuracyKilometer` or `kCLLocationAccuracyThreeKilometers`, is a better choice because it conserves power.

The app also sets a default value for the `activityType` property, and is configurable in a menu. This property provides a hint to Core Location about the type of travel the device encounters while monitoring location. For example, if someone uses this app often while running, it sets `activityType` to [`CLActivityType.fitness`](https://developer.apple.com/documentation/CoreLocation/CLActivityType/fitness). If they use it for providing driving directions, it sets `activityType` to [`CLActivityType.automotiveNavigation`](https://developer.apple.com/documentation/CoreLocation/CLActivityType/automotiveNavigation) so that Core Location makes small adjustments to the reported location to match known roads.

```swift
locationManager.requestWhenInUseAuthorization()

/// Enable the app to collect location updates while it's in the background.
locationManager.allowsBackgroundLocationUpdates = true
```

After the app calls `startUpdatingLocation` on the location manager, Core Location provides location updates to the location manager’s delegate. Then the app forwards the location updates to other functions in the app responsible for maintaining the user’s location history.

```swift
func locationManager(_ manager: CLLocationManager, didUpdateLocations locations: [CLLocation]) {
    
    // Play a sound so it's easy to tell when a location update occurs while the app is in the background.
    if chimeOnLocationUpdate && !locations.isEmpty {
        setSessionActiveWithMixing(true) // Ducks the audio of other apps when playing the chime.
        playSound()
    }
    
    // Always process all of the provided locations. Don't assume the array only contains a single location.
    for location in locations {
        displayNewBreadcrumbOnMap(location)
    }
}
```

##### Define a Custom Map Overlay Data Object

MapKit treats overlay data as static when using the system-provided overlay classes, such as [`MKPolyline`](MKPolyline.md). For example, apps that only need to show a path with a static set of coordinates, such as the path a user took in the distant past, can use `MKPolyline`. Because this app continually updates with new data, it implements its own data class, called `BreadcrumbPath`, conforming to the [`MKOverlay`](MKOverlay.md) protocol, rather than using `MKPolyline`. `BreadcrumbPath` maintains an array of location  comprising the user’s location history.

When drawing an overlay on the map, MapKit uses the overlay’s [`boundingMapRect`](MKOverlay/boundingMapRect.md) to determine when the overlay is visible. Because this app can’t determine the extent of the path the user might track on the map, `BreadcrumbPath` declares its `boundingMapRect` as [`world`](MKMapRect/world.md). In an app that has well-defined usage patterns, such as a hiking app for use within a national park, the `boundingMapRect` might consist of a large area the path is likely to remain within, such as the bounds of the national park.

When the app adds a new location, `BreadcrumbPath` validates that the information in `CLLocation` is usable for its purposes. Each app that maintains a location history needs to define criteria for ensuring a location update is usable based on the app’s specific needs.

```swift
private func isNewLocationUsable(_ newLocation: CLLocation, breadcrumbData: BreadcrumbData) -> Bool {
    /**
     Always check the timestamp of a location value to ensure the location is recent, such as within the last 60 seconds. When starting
     location updates, the values that return may reflect cached values while the device works to acquire updated locations according to
     the accuracy level of the location manager. For some apps, the cached values may be sufficient, but in an app that draws a map of
     a user's travel path, values that are too old may deviate too far from the user's actual path.
     */
    let now = Date()
    let locationAge = now.timeIntervalSince(newLocation.timestamp)
    guard locationAge < 60 else { return false }
    
    /**
     An app might keep the first few updates before applying any further filtering, such as to ensure there is an intial set of
     locations while waiting for the location accuracy to increase to the requested level.
     */
    guard breadcrumbData.locations.count > 10 else { return true }
    
    /**
     Identify locations that shouldn't be part of the breadcrumb data, such as locations that are too close together.
     Get the distance between this new location and the previous location, and use a minimum threshold
     to determine if keeping the location is useful. For example, a location update that is just a few meters from the
     prior location might represent a user that hasn't moved.
     
     Your app may apply other criteria. For example, an app tracking a user at walking speed may discard updates that show the user
     moving at car speeds because that might indicate the user forgot to stop recording their location after completing the walk.
     Consider comparing an average value over the last several location updates, such as the user's average speed.
     
     If using the location accuracy properties as criteria for determining a usable location, expect the values to vary, and don't
     throw away low-accuracy values by expecting only high-accuracy values. Discarding locations due to lower than expected accuracy
     can cause the user's location to appear to jump if the user is moving.
     */
    let minimumDistanceBetweenLocationsInMeters = 10.0
    let previousLocation = breadcrumbData.locations.last!
    let metersApart = newLocation.distance(from: previousLocation)
    return metersApart > minimumDistanceBetweenLocationsInMeters
}
```

After `BreadcrumbPath` validates that a location is usable, it updates its data structures to include the new location. One of the properties of `BreadcrumbPath` is `pathBounds`, the bounding rectangle containing all of the locations for the overlay. Unlike `boundingMapRect`, `pathBounds` changes its value as the app adds locations to the overlay. A custom overlay renderer reads the value of `pathBounds` from multiple threads concurrently, so `BreadcrumbPath` uses [`OSAllocatedUnfairLock`](https://developer.apple.com/documentation/os/OSAllocatedUnfairLock) to protect reading of this property from data races.

```swift
/// This is a lock protecting the `locations` and `bounds` properties that define the breadcrumb path from data races.
private let protectedBreadcrumbData = OSAllocatedUnfairLock(initialState: BreadcrumbData())

/**
 This is a rectangle encompassing the breadcrumb path, including a reasonable amount of padding. The value of this property changes
 when adding a new location to the breadcrumb path that’s outside of the existing `pathBounds`.
 */
var pathBounds: MKMapRect {
    /**
     The app accesses this property from the main thread in `BreadcrumbViewController`, and multiple
     background threads running in parallel, through the `canDraw(_:zoomScale)` method.
     Using a lock for access avoids data races.
     */
    return protectedBreadcrumbData.withLock { breadcrumbData in
        return breadcrumbData.bounds
    }
}
```

##### Implement a Custom Overlay Renderer to Display the Path

To implement a custom overlay renderer object that complements the custom overlay data object, the app subclasses [`MKOverlayRenderer`](MKOverlayRenderer.md). To determine whether an overlay has content to draw, MapKit queries the [`canDraw(_:zoomScale:)`](MKOverlayRenderer/canDraw(_:zoomScale:).md) method of an overlay renderer. The `BreadcrumbPathRenderer` class in this sample overrides this method to check whether the provided [`MKMapRect`](MKMapRect.md) intersects the `pathBounds` property of the `BreadcrumbPath` object.

```swift
override func canDraw(_ mapRect: MKMapRect, zoomScale: MKZoomScale) -> Bool {
    return crumbs.pathBounds.intersects(mapRect)
}
```

A custom overlay renderer also needs to implement the [`draw(_:zoomScale:in:)`](MKOverlayRenderer/draw(_:zoomScale:in:).md) method to draw the requested section of the overlay. The app draws only the portion of the overlay within the bounds of the provided `MKMapRect` into the provided [`CGContext`](https://developer.apple.com/documentation/CoreGraphics/CGContext).

```swift
override func draw(_ mapRect: MKMapRect, zoomScale: MKZoomScale, in context: CGContext) {
    /// Scale the width of the line to match the width of a road.
    let lineWidth = MKRoadWidthAtZoomScale(zoomScale)
    
    /// Outset `mapRect` by the line width to include points just outside of the current rectangle in the generated path.
    let clipRect = mapRect.insetBy(dx: -lineWidth, dy: -lineWidth)
    
    /**
     Because the system might call this function on multiple background threads simultaneously,
     and the `locations` property of the `BreadcrumbPath` updates frequently,
     `locations` needs to guard against data races. See the comments in `BreadcrumbPath` for details.
     */
    let points = crumbs.locations.map { MKMapPoint($0.coordinate) }
    if let path = pathForPoints(points, mapRect: clipRect, zoomScale: zoomScale) {
        context.addPath(path)
        context.setStrokeColor(UIColor.systemBlue.withAlphaComponent(0.5).cgColor)
        context.setLineJoin(.round)
        context.setLineCap(.round)
        context.setLineWidth(lineWidth)
        context.strokePath()
    }
}
```

##### Request That the Map Update the Overlay

When the sample app receives a location update, it adds the location to the custom overlay by calling a method that `BreadcrumbPath` defines. This method returns information indicating the result of adding the location to the overlay. When successful, the app calls [`setNeedsDisplay(_:)`](MKOverlayRenderer/setNeedsDisplay(_:).md) on the custom overlay renderer to trigger a redraw of the overlay within the region of the map where the user traveled.

```swift
/**
 If the `BreadcrumbPath` model object determines that the current location moves far enough from the previous location,
 use the returned updateRect to redraw just the changed area.
*/
let result = breadcrumbs.addLocation(newLocation)

/**
 If the `BreadcrumbPath` model object sucessfully adds the location to the path,
 update the rendering of the path to include the new location.
 */
 if result.locationAdded {
    // Compute the currently visible map zoom scale.
    let currentZoomScale = mapView.bounds.size.width / mapView.visibleMapRect.size.width
    
    /**
     Find out the line width at this zoom scale and outset the `pathBounds` by that amount to ensure the full line width draws.
     This covers situations where the new location is right on the edge of the provided `pathBounds`, and only part of the line width
     is within the bounds.
    */
    let lineWidth = MKRoadWidthAtZoomScale(currentZoomScale)
    var areaToRedisplay = breadcrumbs.pathBounds
    areaToRedisplay = areaToRedisplay.insetBy(dx: -lineWidth, dy: -lineWidth)
    
    /**
     Tell the overlay view to update just the changed area, including the area that the line width covers.
     Use `setNeedsDisplay(_:)` to only redraw the changed area of a breadcrumb overlay. For this sample,
     the changed area includes the entire overlay because if the app was recently in the background, the breadcrumb path
     that's visible when the app returns to the foreground might change significantly.

     In general, avoid calling `setNeedsDisplay()` on the overlay renderer without a map rectangle, as that may cause a render
     pass for the entire visible map, only some of which may contain updated data in the overlay.
     
     To avoid an expensive operation, call `setNeedsDisplay(_:)` instead of removing the overlay from the map and then immediately
     adding it back to trigger a render pass when the data is changing often. The rendering of an overlay after adding it to the
     map is not instantaneous, so removing and adding an overlay may cause a visual flicker as the system updates the map view
     without the overlay, and then updates it again with the overlay. This is especially true if the map is displaying more than
     one overlay or updating the overlay data often, such as on each location update.
    */
    breadcrumbPathRenderer?.setNeedsDisplay(areaToRedisplay)
}
```

## See Also

- [Displaying overlays on a map](displaying-overlays-on-a-map.md)
  Add regions of layered content to a map view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkit/displaying-an-updating-path-of-a-user-s-location-history)*