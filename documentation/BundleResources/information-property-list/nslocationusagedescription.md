# NSLocationUsageDescription

**Framework**: Bundle Resources  
**Kind**: typealias

A message that tells people why the app is requesting access to their location information.

**Availability**:
- iOS 6.0+
- iPadOS 6.0+
- macOS 10.14+

#### Discussion

Use this key in a macOS app that accesses the user’s location information. In an iOS app, use [`NSLocationWhenInUseUsageDescription`](information-property-list/nslocationwheninuseusagedescription.md) or [`NSLocationAlwaysAndWhenInUseUsageDescription`](information-property-list/nslocationalwaysandwheninuseusagedescription.md) instead.

> ❗ **Important**:  This key is required if your macOS app uses APIs that access the user’s location information.

## See Also

- [Choosing the  Location Services Authorization to Request](choosing-the-location-services-authorization-to-request.md)
  Determine the authorization your app needs to access location data.
- [NSLocationAlwaysAndWhenInUseUsageDescription](information-property-list/nslocationalwaysandwheninuseusagedescription.md)
  A message that tells people why the app is requesting access to their location information at all times.
- [NSLocationWhenInUseUsageDescription](information-property-list/nslocationwheninuseusagedescription.md)
  A message that tells people why the app is requesting access to their location information while the app is running in the foreground.
- [NSLocationTemporaryUsageDescriptionDictionary](information-property-list/nslocationtemporaryusagedescriptiondictionary.md)
  A collection of messages that explain why the app is requesting temporary access to their location.
- [NSLocationAlwaysUsageDescription](information-property-list/nslocationalwaysusagedescription.md)
  A message that tells people why the app is requesting access to their location at all times.
- [NSWidgetWantsLocation](information-property-list/nswidgetwantslocation.md)
  A Boolean value that indicates a widget uses the user’s location information.
- [NSLocationDefaultAccuracyReduced](information-property-list/nslocationdefaultaccuracyreduced.md)
  A Boolean value that indicates whether the app requests reduced location accuracy by default.


---

*[View on Apple Developer](https://developer.apple.com/documentation/bundleresources/information-property-list/nslocationusagedescription)*