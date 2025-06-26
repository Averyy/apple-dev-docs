# MKMapView

**Framework**: MapKit  
**Kind**: class

An embeddable map interface, similar to the one that the Maps app provides.

**Availability**:
- iOS 3.0+
- iPadOS 3.0+
- Mac Catalyst 13.1+
- macOS 10.9+
- tvOS 9.2+
- visionOS 1.0+

## Declaration

```swift
@MainActor
class MKMapView
```

#### Overview

Use this class as-is to display map information and to manipulate the map contents from your app. The map view supports several display styles, including the [`MKStandardMapConfiguration`](mkstandardmapconfiguration.md) that provides rich 2D and 3D presentations, an [`MKHybridMapConfiguration`](mkhybridmapconfiguration.md) that provides a hybrid satellite map presentation, and [`MKImageryMapConfiguration`](mkimagerymapconfiguration.md) that provides an imagery-based map presentation. Each of these map configurations support customization properties that refine specific elements of the map’s presentation.

You can center the map on specific coordinates, specify the size of the area you want to display, and annotate the map with custom information. When you initialize a map view, you specify the initial region for that map to display by setting the [`region`](mkmapview/region.md) property of the map. MapKit defines a region by a center point and a horizontal and vertical distance, referred to as the . The  defines how much of the map is visible, and is also how you set the zoom level. For example, specifying a large span results in the user seeing a wide geographical area at a low zoom level, whereas specifying a small span results in a more narrow geographical area and a higher zoom level.

In addition to setting the span programmatically, the `MKMapView` class supports many standard interactions for changing the position and zoom level of the map. In particular, map views support flick and pinch gestures for scrolling around the map and zooming in and out. The map view enables support for these gestures by default. You can enable and disable them using the [`isScrollEnabled`](mkmapview/isscrollenabled.md) and [`isZoomEnabled`](mkmapview/iszoomenabled.md) properties.

You can also use projected map coordinates instead of regions to specify some values. When you project the curved surface of the globe onto a flat surface, you get a two-dimensional version of a map where longitude lines appear to be parallel. To specify locations and distances, you use the [`MKMapPoint`](mkmappoint.md), [`MKMapSize`](mkmapsize.md), and [`MKMapRect`](mkmaprect.md) data types.

Don’t subclass the `MKMapView` class itself. You can get information about the map view’s behavior by providing a delegate object. The map view calls the methods of your custom delegate to let it know about changes in the map status and to coordinate the display of custom annotations. The delegate object can be any object in your app as long as it conforms to the [`MKMapViewDelegate`](mkmapviewdelegate.md) protocol. For more information about implementing the delegate object, see [`MKMapViewDelegate`](mkmapviewdelegate.md).

In macOS 10.14 and later, you can apply a light or dark appearance to your maps by modifying the [`appearance`](https://developer.apple.com/documentation/AppKit/NSAppearanceCustomization/appearance) property of your map view (or one of its ancestor views). Even if you specify a custom appearance, users can use the Maps app to force all maps to adopt a light appearance. Use the map view’s [`effectiveAppearance`](https://developer.apple.com/documentation/AppKit/NSAppearanceCustomization/effectiveAppearance) property to determine the actual appearance of your map. For information about how to set view appearances, see [`Choosing a Specific Appearance for Your macOS App`](https://developer.apple.com/documentation/AppKit/choosing-a-specific-appearance-for-your-macos-app).

##### Annotating the Map

The `MKMapView` class supports the ability to annotate the map with custom information. Because a map may have large numbers of annotations, map views differentiate between the annotation objects MapKit uses to manage the annotation data and the view objects for presenting that data on the map.

An  is any object that conforms to the [`MKAnnotation`](mkannotation.md) protocol. Typically, you implement annotation objects using existing classes in your app’s data model. This allows you to manipulate the annotation data directly, but still make it available to the map view. Each annotation object contains information about the annotation’s location on the map, along with descriptive information that the map can display in a callout.

An ,_ _which is an instance of the [`MKAnnotationView`](mkannotationview.md) class, handles the presentation of annotation objects on the screen. An annotation view is responsible for presenting the annotation data in a way that makes sense. For example, the Maps app uses a marker icon to denote specific points of interest on a map. The MapKit framework offers the [`MKMarkerAnnotationView`](mkmarkerannotationview.md) class for similar annotations in your own apps. You can also create annotation views that cover larger portions of the map.

Because the map view needs annotation views only when they’re onscreen, the `MKMapView` class provides a mechanism for queueing annotation views that aren’t in use. The map view detaches annotation views with a reuse identifier and queues them internally when they move offscreen. This feature improves memory use by keeping only a small number of annotation views in memory at once, and by recycling the views you do have. It also improves scrolling performance by alleviating the need to create new views while the map is scrolling.

When configuring your map interface, be sure to add all of your annotation objects right away. The map view uses the coordinate data in each annotation object to determine when the corresponding annotation view needs to appear onscreen. When an annotation moves onscreen, the map view asks its delegate to create a corresponding annotation view. If your app has different types of annotations, it can define different annotation view classes to represent each type.

##### Adding Overlays to the Map

You can use overlays to layer content over a wide portion of the map. An  object is any object that conforms to the [`MKOverlay`](mkoverlay.md) protocol. An overlay object is a data object that contains the points that specify the shape and size of the overlay and its location on the map. Overlays can represent shapes like circles, rectangles, multisegment lines, and simple or complex polygons. You can also define your own custom overlays to represent other shapes.

 objects, which are instances of the [`MKOverlayRenderer`](mkoverlayrenderer.md) class, handle the presentation of an overlay. The job of the renderer is to draw the overlay’s content onto the screen when the map view requests it. For example, if you have a simple overlay that represents a bus route, you can use a polyline renderer to draw the line segments that trace the route of the bus. You can also define a custom renderer that draws both the bus route and icons at the location of each bus stop. When specifying overlays, you can add them to specific levels of the map, which tells the map view to render them above or below other types of map content.

When configuring your map interface, you can add overlay objects at any time. The map view uses the data in each overlay object to determine when the corresponding overlay view needs to appear onscreen. When an overlay moves onscreen, the map view asks its delegate to create a corresponding overlay renderer.

##### Adding Points of Interest to the Map

In iOS16 and macOS 13, and later, you can configure the map view to allow people to interact with a wide variety of points of interest (POIs) the map displays. These are instances of the [`MKMapFeatureAnnotation`](mkmapfeatureannotation.md) class, and cover a wide variety of elements visible on the map, including:

- Points of interest, such as museums, cafes, parks, and schools.
- Territorial boundaries, such as national borders, state boundaries, and neighborhoods.
- Features on the Earth’s surface, such as mountain ranges, rivers, and ocean basins.

You can control which features a person can interact with by configuring one of the [`MKMapConfiguration`](mkmapconfiguration.md) subclasses that defines the map’s presentation. Create an `MKMapConfiguration` with a set of [`MKMapFeatureOptions`](mkmapfeatureoptions.md) that describe the categories of POIs the map responds to. To further refine the specific kinds of points of interest the map display presents, use an [`MKPointOfInterestFilter`](mkpointofinterestfilter.md).

When a person interacts with a specific POI, the framework calls your delegate object with one of the [`MKMapViewDelegate`](mkmapviewdelegate.md) protocol methods, depending on whether the person selects or deselects a specific POI. These methods give your app a chance to respond to the selection or deselection of an element. Depending on the kind of element, you can decide whether you want to customize the display characteristics in the case of a POI, or in the case of territories or geographic map features, you can create custom interactions to display information.

##### Adding Look Around Views to the Map

iOS16 and macOS 13, and later, support the inclusion of a Look Around view within the map view. Look Around allows people to explore the environment at street level. You request a Look Around view by creating an [`MKLookAroundSceneRequest`](mklookaroundscenerequest.md) with either an [`MKMapItem`](mkmapitem.md) or a [`CLLocationCoordinate2D`](https://developer.apple.com/documentation/CoreLocation/CLLocationCoordinate2D), and if there’s Look Around imagery available for the specified location, the framework returns an [`MKLookAroundScene`](mklookaroundscene.md) for you to display using an [`MKLookAroundViewController`](mklookaroundviewcontroller.md).

## Topics

### Configuring the map appearance
- [var preferredConfiguration: MKMapConfiguration](mkmapview/preferredconfiguration.md)
  The characteristics of the map view, including the map type and features the map displays.
- [var pitchButtonVisibility: MKFeatureVisibility](mkmapview/pitchbuttonvisibility.md)
  A value that indicates whether the map’s pitch button is visible.
- [var showsUserTrackingButton: Bool](mkmapview/showsusertrackingbutton.md)
  A Boolean value that indicates whether the map displays the user tracking button.
- [class MKMapConfiguration](mkmapconfiguration.md)
  An abstract class that represents the shared elements of map configurations.
- [class MKStandardMapConfiguration](mkstandardmapconfiguration.md)
  The class that represents the default map presentation, which is a street map that shows the position of all roads and some road names.
- [class MKHybridMapConfiguration](mkhybridmapconfiguration.md)
  The class that represents a satellite image of the area with road and road name information layers on top.
- [class MKImageryMapConfiguration](mkimagerymapconfiguration.md)
  The class that represents an imagery-based map presentation, such as one using satellite imagery.
### Customizing the map view behavior
- [var delegate: (any MKMapViewDelegate)?](mkmapview/delegate.md)
  The receiver’s delegate.
- [protocol MKMapViewDelegate](mkmapviewdelegate.md)
  Optional methods that you use to receive map-related update messages.
### Accessing map properties
- [enum MKMapType](mkmaptype.md)
  The type of map to display.
- [var isZoomEnabled: Bool](mkmapview/iszoomenabled.md)
  A Boolean value that determines whether the user may use pinch gestures to zoom in and out of the map.
- [var isScrollEnabled: Bool](mkmapview/isscrollenabled.md)
  A Boolean value that determines whether the user may scroll around the map.
- [var isPitchEnabled: Bool](mkmapview/ispitchenabled.md)
  A Boolean value that indicates whether the map uses the camera’s pitch information.
- [var isRotateEnabled: Bool](mkmapview/isrotateenabled.md)
  A Boolean value that indicates whether the map uses the camera’s heading information.
- [var mapType: MKMapType](mkmapview/maptype.md)
  The type of data the map view displays.
### Manipulating the visible portion of the map
- [var region: MKCoordinateRegion](mkmapview/region.md)
  The area the map view displays.
- [func setRegion(MKCoordinateRegion, animated: Bool)](mkmapview/setregion(_:animated:).md)
  Changes the currently visible region, and optionally animates the change.
- [var centerCoordinate: CLLocationCoordinate2D](mkmapview/centercoordinate.md)
  The map coordinate at the center of the map view.
- [func setCenter(CLLocationCoordinate2D, animated: Bool)](mkmapview/setcenter(_:animated:).md)
  Changes the center coordinate of the map, and optionally animates the change.
- [func showAnnotations([any MKAnnotation], animated: Bool)](mkmapview/showannotations(_:animated:).md)
  Sets the visible region so that the map displays the specified annotations.
- [var visibleMapRect: MKMapRect](mkmapview/visiblemaprect.md)
  The area visible in the map view.
- [func setVisibleMapRect(MKMapRect, animated: Bool)](mkmapview/setvisiblemaprect(_:animated:).md)
  Changes the currently visible portion of the map, and optionally animates the change.
- [func setVisibleMapRect(MKMapRect, edgePadding: UIEdgeInsets, animated: Bool)](mkmapview/setvisiblemaprect(_:edgepadding:animated:).md)
  Changes the currently visible portion of the map, allowing you to specify additional space around the edges.
### Constraining the map view
- [func setCameraBoundary(MKMapView.CameraBoundary?, animated: Bool)](mkmapview/setcameraboundary(_:animated:).md)
  Sets the camera boundary for the map view, specifying whether to use animation.
- [var cameraBoundary: MKMapView.CameraBoundary?](mkmapview/cameraboundary-swift.property.md)
  The boundary of the area within which the map view’s center needs to remain.
- [func setCameraZoomRange(MKMapView.CameraZoomRange?, animated: Bool)](mkmapview/setcamerazoomrange(_:animated:).md)
  Sets the camera zoom range for the map view, specifying whether to use animation.
- [var cameraZoomRange: MKMapView.CameraZoomRange!](mkmapview/camerazoomrange-swift.property.md)
  The zoom range to apply to the map view.
- [MKMapView.CameraBoundary](mkmapview/cameraboundary-swift.class.md)
  A boundary of an area within which the map’s center needs to remain.
- [MKMapView.CameraZoomRange](mkmapview/camerazoomrange-swift.class.md)
  A camera zoom range that limits the distances to which the user can zoom.
### Configuring the map display
- [func setCamera(MKMapCamera, animated: Bool)](mkmapview/setcamera(_:animated:).md)
  Changes the camera to use for determining the map’s viewing parameters, and optionally animates the change.
- [var camera: MKMapCamera](mkmapview/camera.md)
  The camera to use for determining the appearance of the map.
- [var showsCompass: Bool](mkmapview/showscompass.md)
  A Boolean value that indicates whether the map displays a compass control.
- [var showsPitchControl: Bool](mkmapview/showspitchcontrol.md)
  A Boolean value that indicates whether the map displays the pitch control.
- [var showsScale: Bool](mkmapview/showsscale.md)
  A Boolean value that indicates whether the map shows scale information.
- [var showsZoomControls: Bool](mkmapview/showszoomcontrols.md)
  A Boolean value that indicates whether the map displays zoom controls.
- [var showsBuildings: Bool](mkmapview/showsbuildings.md)
  A Boolean value that indicates whether the map displays extruded building information on supported map types.
- [var showsPointsOfInterest: Bool](mkmapview/showspointsofinterest.md)
  A Boolean value that indicates whether the map displays point-of-interest information.
- [var pointOfInterestFilter: MKPointOfInterestFilter?](mkmapview/pointofinterestfilter.md)
  The filter to use for determining the points of interest that appear on the map.
- [var showsTraffic: Bool](mkmapview/showstraffic.md)
  A Boolean value that indicates whether the map displays traffic information.
### Displaying the user’s location
- [Converting a user’s location to a descriptive placemark](converting-a-user-s-location-to-a-descriptive-placemark.md)
  Transform the user’s location that displays on a map into an informative textual description by reverse geocoding.
- [var showsUserLocation: Bool](mkmapview/showsuserlocation.md)
  A Boolean value that indicates whether the map tries to display the user’s location.
- [var isUserLocationVisible: Bool](mkmapview/isuserlocationvisible.md)
  A Boolean value that indicates whether the user’s location is visible in the map view.
- [var userLocation: MKUserLocation](mkmapview/userlocation.md)
  The annotation object that represents the user’s location.
- [var userTrackingMode: MKUserTrackingMode](mkmapview/usertrackingmode.md)
  The mode to use for tracking the user’s location.
- [func setUserTrackingMode(MKUserTrackingMode, animated: Bool)](mkmapview/setusertrackingmode(_:animated:).md)
  Sets the mode to use for tracking the user’s location, with optional animation.
- [enum MKUserTrackingMode](mkusertrackingmode.md)
  The mode to use for tracking the user’s location on the map.
### Annotating the map
- [var annotations: [any MKAnnotation]](mkmapview/annotations.md)
  The annotations associated with the map view.
- [func addAnnotation(any MKAnnotation)](mkmapview/addannotation(_:).md)
  Adds the specified annotation to the map view.
- [func addAnnotations([any MKAnnotation])](mkmapview/addannotations(_:).md)
  Adds an array of annotation objects to the map view.
- [func removeAnnotation(any MKAnnotation)](mkmapview/removeannotation(_:).md)
  Removes the specified annotation object from the map view.
- [func removeAnnotations([any MKAnnotation])](mkmapview/removeannotations(_:).md)
  Removes an array of annotation objects from the map view.
- [func annotations(in: MKMapRect) -> Set<AnyHashable>](mkmapview/annotations(in:).md)
  Returns the annotation objects within the specified map rectangle.
### Managing annotation selections
- [var annotationVisibleRect: CGRect](mkmapview/annotationvisiblerect.md)
  The visible rectangle where the map is displaying annotation views.
- [var selectedAnnotations: [any MKAnnotation]](mkmapview/selectedannotations.md)
  The selected annotations.
- [func selectAnnotation(any MKAnnotation, animated: Bool)](mkmapview/selectannotation(_:animated:).md)
  Selects the specified annotation and displays a callout view for it.
- [func deselectAnnotation((any MKAnnotation)?, animated: Bool)](mkmapview/deselectannotation(_:animated:).md)
  Deselects the specified annotation and hides its callout view.
### Creating annotation views
- [func register(AnyClass?, forAnnotationViewWithReuseIdentifier: String)](mkmapview/register(_:forannotationviewwithreuseidentifier:).md)
  Registers an annotation view class that the map can create automatically.
- [func dequeueReusableAnnotationView(withIdentifier: String, for: any MKAnnotation) -> MKAnnotationView](mkmapview/dequeuereusableannotationview(withidentifier:for:).md)
  Returns a reusable annotation view using the specified identifier with a specified existing annotation view, if possible.
- [func dequeueReusableAnnotationView(withIdentifier: String) -> MKAnnotationView?](mkmapview/dequeuereusableannotationview(withidentifier:).md)
  Returns a reusable annotation view using its identifier.
- [func view(for: any MKAnnotation) -> MKAnnotationView?](mkmapview/view(for:)-33w8k.md)
  Returns the annotation view associated with the specified annotation object, if any.
- [let MKMapViewDefaultAnnotationViewReuseIdentifier: String](mkmapviewdefaultannotationviewreuseidentifier.md)
  The default reuse identifier for your map’s annotation views.
- [let MKMapViewDefaultClusterAnnotationViewReuseIdentifier: String](mkmapviewdefaultclusterannotationviewreuseidentifier.md)
  The default reuse identifier for the annotation view representing a cluster of annotations.
### Accessing overlays
- [var overlays: [any MKOverlay]](mkmapview/overlays.md)
  The overlay objects associated with the map view.
- [func overlays(in: MKOverlayLevel) -> [any MKOverlay]](mkmapview/overlays(in:).md)
  Returns overlay objects in the specified level of the map.
- [func renderer(for: any MKOverlay) -> MKOverlayRenderer?](mkmapview/renderer(for:).md)
  Returns the renderer object for drawing the contents of the specified overlay object.
- [enum MKOverlayLevel](mkoverlaylevel.md)
  Constants that indicate the position of overlays relative to other content.
- [func view(for: any MKOverlay) -> MKOverlayView](mkmapview/view(for:)-38z60.md)
  Returns the view associated with the overlay object, if any.
### Adding and inserting overlays
- [func addOverlay(any MKOverlay, level: MKOverlayLevel)](mkmapview/addoverlay(_:level:).md)
  Adds the overlay object to the map at the specified level.
- [func addOverlays([any MKOverlay], level: MKOverlayLevel)](mkmapview/addoverlays(_:level:).md)
  Adds an array of overlay objects to the map at the specified level.
- [func addOverlay(any MKOverlay)](mkmapview/addoverlay(_:).md)
  Adds a single overlay object to the map.
- [func addOverlays([any MKOverlay])](mkmapview/addoverlays(_:).md)
  Adds an array of overlay objects to the map.
- [func insertOverlay(any MKOverlay, at: Int, level: MKOverlayLevel)](mkmapview/insertoverlay(_:at:level:).md)
  Inserts an overlay object into the level at the specified index.
- [func insertOverlay(any MKOverlay, at: Int)](mkmapview/insertoverlay(_:at:).md)
  Inserts an overlay object into the list associated with the map.
- [func insertOverlay(any MKOverlay, above: any MKOverlay)](mkmapview/insertoverlay(_:above:).md)
  Inserts one overlay object above another.
- [func insertOverlay(any MKOverlay, below: any MKOverlay)](mkmapview/insertoverlay(_:below:).md)
  Inserts one overlay object below another.
- [func exchangeOverlay(any MKOverlay, with: any MKOverlay)](mkmapview/exchangeoverlay(_:with:).md)
  Exchanges the positions of two overlay objects.
- [func exchangeOverlay(at: Int, withOverlayAt: Int)](mkmapview/exchangeoverlay(at:withoverlayat:).md)
  Exchanges the position of two overlay objects at the specified index.
### Removing overlays
- [func removeOverlay(any MKOverlay)](mkmapview/removeoverlay(_:).md)
  Removes a single overlay object from the map.
- [func removeOverlays([any MKOverlay])](mkmapview/removeoverlays(_:).md)
  Removes one or more overlay objects from the map.
### Converting map coordinates
- [func convert(CLLocationCoordinate2D, toPointTo: UIView?) -> CGPoint](mkmapview/convert(_:topointto:).md)
  Converts a map coordinate to a point in the specified view.
- [func convert(CGPoint, toCoordinateFrom: UIView?) -> CLLocationCoordinate2D](mkmapview/convert(_:tocoordinatefrom:).md)
  Converts a point in the specified view’s coordinate system to a map coordinate.
- [func convert(MKCoordinateRegion, toRectTo: UIView?) -> CGRect](mkmapview/convert(_:torectto:).md)
  Converts a map region to a rectangle in the specified view.
- [func convert(CGRect, toRegionFrom: UIView?) -> MKCoordinateRegion](mkmapview/convert(_:toregionfrom:).md)
  Converts a rectangle in the specified view’s coordinate system to a map region.
### Adjusting map regions and rectangles
- [func regionThatFits(MKCoordinateRegion) -> MKCoordinateRegion](mkmapview/regionthatfits(_:).md)
  Adjusts the aspect ratio of the specified region to ensure that it fits in the map view’s frame.
- [func mapRectThatFits(MKMapRect) -> MKMapRect](mkmapview/maprectthatfits(_:).md)
  Returns a centered map rectangle with the same aspect ratio as the map view’s frame.
- [func mapRectThatFits(MKMapRect, edgePadding: UIEdgeInsets) -> MKMapRect](mkmapview/maprectthatfits(_:edgepadding:).md)
  Returns a centered, inset map rectangle with the same aspect ratio as the map view’s frame.
### Instance Properties
- [var selectableMapFeatures: MKMapFeatureOptions](mkmapview/selectablemapfeatures.md)
  The property that describes which selectable features the map responds to.

## Relationships

### Inherits From
- [NSView](../AppKit/NSView.md)
- [UIView](../UIKit/UIView.md)
### Conforms To
- [CALayerDelegate](../QuartzCore/CALayerDelegate.md)
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSAccessibilityElementProtocol](../AppKit/NSAccessibilityElementProtocol.md)
- [NSAccessibilityProtocol](../AppKit/NSAccessibilityProtocol.md)
- [NSAnimatablePropertyContainer](../AppKit/NSAnimatablePropertyContainer.md)
- [NSAppearanceCustomization](../AppKit/NSAppearanceCustomization.md)
- [NSCoding](../Foundation/NSCoding.md)
- [NSDraggingDestination](../AppKit/NSDraggingDestination.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [NSStandardKeyBindingResponding](../AppKit/NSStandardKeyBindingResponding.md)
- [NSTouchBarProvider](../AppKit/NSTouchBarProvider.md)
- [NSUserActivityRestoring](../AppKit/NSUserActivityRestoring.md)
- [NSUserInterfaceItemIdentification](../AppKit/NSUserInterfaceItemIdentification.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)
- [UIAccessibilityIdentification](../UIKit/UIAccessibilityIdentification.md)
- [UIActivityItemsConfigurationProviding](../UIKit/UIActivityItemsConfigurationProviding.md)
- [UIAppearance](../UIKit/UIAppearance.md)
- [UIAppearanceContainer](../UIKit/UIAppearanceContainer.md)
- [UICoordinateSpace](../UIKit/UICoordinateSpace.md)
- [UIDynamicItem](../UIKit/UIDynamicItem.md)
- [UIFocusEnvironment](../UIKit/UIFocusEnvironment.md)
- [UIFocusItem](../UIKit/UIFocusItem.md)
- [UIFocusItemContainer](../UIKit/UIFocusItemContainer.md)
- [UILargeContentViewerItem](../UIKit/UILargeContentViewerItem.md)
- [UIPasteConfigurationSupporting](../UIKit/UIPasteConfigurationSupporting.md)
- [UIPopoverPresentationControllerSourceItem](../UIKit/UIPopoverPresentationControllerSourceItem.md)
- [UIResponderStandardEditActions](../UIKit/UIResponderStandardEditActions.md)
- [UITraitChangeObservable](../UIKit/UITraitChangeObservable-67e94.md)
- [UITraitEnvironment](../UIKit/UITraitEnvironment.md)
- [UIUserActivityRestoring](../UIKit/UIUserActivityRestoring.md)

## See Also

- [Enabling Maps capability in Xcode](enabling-maps-capability-in-xcode.md)
  Configure your routing app to support providing directions.
- [Identifying unique locations with Place IDs](identifying-unique-locations-with-place-ids.md)
  Obtain information about a point of interest that persists over its lifetime.
- [class MKMapItem](mkmapitem.md)
  A point of interest on the map.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkit/mkmapview)*