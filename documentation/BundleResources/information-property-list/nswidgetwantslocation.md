# NSWidgetWantsLocation

**Framework**: Bundle Resources  
**Kind**: typealias

A Boolean value that indicates a widget uses the user’s location information.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- macOS 11.0+

#### Discussion

To access the user’s location information from a widget, set the value to [`true`](https://developer.apple.com/documentation/Swift/true) in the widget extension’s `Info.plist` file.

Before a widget can access location information, the containing app must request authorization from the user. The containing app’s `Info.plist` file must also contain relevant purpose strings. For more information, see [`Requesting authorization to use location services`](https://developer.apple.com/documentation/CoreLocation/requesting-authorization-to-use-location-services).

## See Also

- [Choosing the  Location Services Authorization to Request](choosing-the-location-services-authorization-to-request.md)
  Determine the authorization your app needs to access location data.
- [NSLocationAlwaysAndWhenInUseUsageDescription](information-property-list/nslocationalwaysandwheninuseusagedescription.md)
  A message that tells people why the app is requesting access to their location information at all times.
- [NSLocationUsageDescription](information-property-list/nslocationusagedescription.md)
  A message that tells people why the app is requesting access to their location information.
- [NSLocationWhenInUseUsageDescription](information-property-list/nslocationwheninuseusagedescription.md)
  A message that tells people why the app is requesting access to their location information while the app is running in the foreground.
- [NSLocationTemporaryUsageDescriptionDictionary](information-property-list/nslocationtemporaryusagedescriptiondictionary.md)
  A collection of messages that explain why the app is requesting temporary access to their location.
- [NSLocationAlwaysUsageDescription](information-property-list/nslocationalwaysusagedescription.md)
  A message that tells people why the app is requesting access to their location at all times.
- [NSLocationDefaultAccuracyReduced](information-property-list/nslocationdefaultaccuracyreduced.md)
  A Boolean value that indicates whether the app requests reduced location accuracy by default.


---

*[View on Apple Developer](https://developer.apple.com/documentation/bundleresources/information-property-list/nswidgetwantslocation)*