# NSLocationWhenInUseUsageDescription

**Framework**: Bundle Resources  
**Kind**: typealias

A message that tells people why the app is requesting access to their location information while the app is running in the foreground.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- visionOS 1.0+

#### Discussion

Use this key if your iOS app accesses location information only when running in the foreground. If your app needs location information when in the background, use [`NSLocationAlwaysAndWhenInUseUsageDescription`](information-property-list/nslocationalwaysandwheninuseusagedescription.md) instead. For more information, see [`Choosing the  Location Services Authorization to Request`](choosing-the-location-services-authorization-to-request.md).

If you need location information in a macOS app, use [`NSLocationUsageDescription`](information-property-list/nslocationusagedescription.md) instead.

> ❗ **Important**:  This key is required if your iOS app uses APIs that access the user’s location information while the app is in use.

## See Also

- [Choosing the  Location Services Authorization to Request](choosing-the-location-services-authorization-to-request.md)
  Determine the authorization your app needs to access location data.
- [NSLocationAlwaysAndWhenInUseUsageDescription](information-property-list/nslocationalwaysandwheninuseusagedescription.md)
  A message that tells people why the app is requesting access to their location information at all times.
- [NSLocationUsageDescription](information-property-list/nslocationusagedescription.md)
  A message that tells people why the app is requesting access to their location information.
- [NSLocationTemporaryUsageDescriptionDictionary](information-property-list/nslocationtemporaryusagedescriptiondictionary.md)
  A collection of messages that explain why the app is requesting temporary access to their location.
- [NSLocationAlwaysUsageDescription](information-property-list/nslocationalwaysusagedescription.md)
  A message that tells people why the app is requesting access to their location at all times.
- [NSWidgetWantsLocation](information-property-list/nswidgetwantslocation.md)
  A Boolean value that indicates a widget uses the user’s location information.
- [NSLocationDefaultAccuracyReduced](information-property-list/nslocationdefaultaccuracyreduced.md)
  A Boolean value that indicates whether the app requests reduced location accuracy by default.


---

*[View on Apple Developer](https://developer.apple.com/documentation/bundleresources/information-property-list/nslocationwheninuseusagedescription)*