# NSLocationDefaultAccuracyReduced

**Framework**: Bundle Resources  
**Kind**: typealias

A Boolean value that indicates whether the app requests reduced location accuracy by default.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- visionOS 1.0+
- watchOS 7.0+

#### Discussion

Include this key in your information property list to set your app’s default behavior for location accuracy when it calls the Core Location framework. Set the key value to `true` to prompt the user for reduced accuracy by default; set it to `false` to prompt for full location accuracy. If you don’t include that key in your `Info.plist`, that’s equivalent to setting it to `false`.

Include the key pair in your `Info.plist` file as shown:

```xml
<!-- Info.plist -->
<key>NSLocationDefaultAccuracyReduced</key>
<true/>
```

When this key is set to `true`, all Core Location services (location updates, visit monitoring, significant location change, fence monitoring) receive service at the reduced-accuracy service level.  Users will see that your app is asking for reduced accuracy because the location authorization prompt will show a map with an approximate location, and your app will have the Precise Location toggled off in Settings > Privacy > Location Services . These indicators of an app’s improved privacy are ones that users may value.

If you want to leverage the reduced-accuracy feature to improve privacy in a particular operation without setting this key, use the [`desiredAccuracy`](https://developer.apple.com/documentation/CoreLocation/CLLocationManager/desiredAccuracy) constant [`kCLLocationAccuracyReduced`](https://developer.apple.com/documentation/CoreLocation/kCLLocationAccuracyReduced). This constant causes [`startUpdatingLocation()`](https://developer.apple.com/documentation/CoreLocation/CLLocationManager/startUpdatingLocation()) to deliver results as if the app were authorized for approximate location until you change the [`desiredAccuracy`](https://developer.apple.com/documentation/CoreLocation/CLLocationManager/desiredAccuracy) constant again.

Setting [`NSLocationDefaultAccuracyReduced`](information-property-list/nslocationdefaultaccuracyreduced.md) determines the default type of authorization your app gets, but users can override it any time in Settings. Users always control the level of location accuracy they want to share, and can change precision settings in Settings > Privacy > Location Services by selecting Precise Location for your app.

## See Also

- [Choosing the  Location Services Authorization to Request](choosing-the-location-services-authorization-to-request.md)
  Determine the authorization your app needs to access location data.
- [NSLocationAlwaysAndWhenInUseUsageDescription](information-property-list/nslocationalwaysandwheninuseusagedescription.md)
  A message that tells the user why the app is requesting access to the user’s location information at all times.
- [NSLocationUsageDescription](information-property-list/nslocationusagedescription.md)
  A message that tells the user why the app is requesting access to the user’s location information.
- [NSLocationWhenInUseUsageDescription](information-property-list/nslocationwheninuseusagedescription.md)
  A message that tells the user why the app is requesting access to the user’s location information while the app is running in the foreground.
- [NSLocationTemporaryUsageDescriptionDictionary](information-property-list/nslocationtemporaryusagedescriptiondictionary.md)
  A collection of messages that explain why the app is requesting temporary access to the user’s location.
- [NSLocationAlwaysUsageDescription](information-property-list/nslocationalwaysusagedescription.md)
  A message that tells the user why the app is requesting access to the user’s location at all times.
- [NSWidgetWantsLocation](information-property-list/nswidgetwantslocation.md)
  A Boolean value that indicates a widget uses the user’s location information.


---

*[View on Apple Developer](https://developer.apple.com/documentation/bundleresources/information-property-list/nslocationdefaultaccuracyreduced)*