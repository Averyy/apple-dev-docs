# NSLocationAlwaysUsageDescription

**Framework**: Bundle Resources  
**Kind**: typealias

A message that tells the user why the app is requesting access to the user’s location at all times.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+

#### Discussion

Use this key if your iOS app accesses location information in the background, and you deploy to a target earlier than iOS 11. In that case, add both this key and [`NSLocationAlwaysAndWhenInUseUsageDescription`](information-property-list/nslocationalwaysandwheninuseusagedescription.md) to your app’s `Info.plist` file with the same message. Apps running on older versions of the OS use the message associated with [`NSLocationAlwaysUsageDescription`](information-property-list/nslocationalwaysusagedescription.md), while apps running on later versions use the one associated with [`NSLocationAlwaysAndWhenInUseUsageDescription`](information-property-list/nslocationalwaysandwheninuseusagedescription.md).

If your app only needs location information when in the foreground, use [`NSLocationWhenInUseUsageDescription`](information-property-list/nslocationwheninuseusagedescription.md) instead. For more information, see [`Choosing the  Location Services Authorization to Request`](choosing-the-location-services-authorization-to-request.md).

If you need location information in a macOS app, use [`NSLocationUsageDescription`](information-property-list/nslocationusagedescription.md) instead.

> ❗ **Important**:  This key is required if your iOS app uses APIs that access the user’s location at all times and deploys to targets earlier than iOS 11.

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
- [NSWidgetWantsLocation](information-property-list/nswidgetwantslocation.md)
  A Boolean value that indicates a widget uses the user’s location information.
- [NSLocationDefaultAccuracyReduced](information-property-list/nslocationdefaultaccuracyreduced.md)
  A Boolean value that indicates whether the app requests reduced location accuracy by default.


---

*[View on Apple Developer](https://developer.apple.com/documentation/bundleresources/information-property-list/nslocationalwaysusagedescription)*