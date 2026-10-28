# NSWidgetWantsLocation

**Framework**: Bundle Resources  
**Kind**: typealias  
**Role**: Property List Key

A Boolean value that indicates a widget uses the user’s location information.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- macOS 11.0+

## Details

- **Name**: `NSWidgetWantsLocation` (Widget Wants Location)
- **Type**: boolean

## Discussion

To access the user’s location information from a widget, set the value to [`true`](../../Swift/true.md) in the widget extension’s `Info.plist` file.

Before a widget can access location information, the containing app must request authorization from the user. The containing app’s `Info.plist` file must also contain relevant purpose strings. For more information, see [Requesting authorization to use location services](../../CoreLocation/requesting-authorization-to-use-location-services.md).

## See Also

### Location
- [Choosing the  Location Services Authorization to Request](../choosing-the-location-services-authorization-to-request.md)
  Determine the authorization your app needs to access location data.
- [NSLocationAlwaysAndWhenInUseUsageDescription](./nslocationalwaysandwheninuseusagedescription.md)
  A message that tells people why the app is requesting access to their location information at all times.
- [NSLocationUsageDescription](./nslocationusagedescription.md)
  A message that tells people why the app is requesting access to their location information.
- [NSLocationWhenInUseUsageDescription](./nslocationwheninuseusagedescription.md)
  A message that tells people why the app is requesting access to their location information while the app is running in the foreground.
- [NSLocationTemporaryUsageDescriptionDictionary](./nslocationtemporaryusagedescriptiondictionary.md)
  A collection of messages that explain why the app is requesting temporary access to their location.
- [NSLocationAlwaysUsageDescription](./nslocationalwaysusagedescription.md)
  A message that tells people why the app is requesting access to their location at all times.
- [NSLocationDefaultAccuracyReduced](./nslocationdefaultaccuracyreduced.md)
  A Boolean value that indicates whether the app requests reduced location accuracy by default.


---

*[View on Apple Developer](https://developer.apple.com/documentation/bundleresources/information-property-list/nswidgetwantslocation)*