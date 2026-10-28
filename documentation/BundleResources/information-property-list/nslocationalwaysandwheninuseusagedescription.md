# NSLocationAlwaysAndWhenInUseUsageDescription

**Framework**: Bundle Resources  
**Kind**: typealias  
**Role**: Property List Key

A message that tells people why the app is requesting access to their location information at all times.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- visionOS 1.0+

## Details

- **Name**: `NSLocationAlwaysAndWhenInUseUsageDescription` (Privacy - Location Always and When In Use Usage Description)
- **Type**: string

## Discussion

Use this key if your iOS app accesses location information while running in the background. If your app only needs location information when in the foreground, use [`NSLocationWhenInUseUsageDescription`](./nslocationwheninuseusagedescription.md) instead. For more information, see [Choosing the  Location Services Authorization to Request](../choosing-the-location-services-authorization-to-request.md).

If you need location information in a macOS app, use [`NSLocationUsageDescription`](./nslocationusagedescription.md) instead. If your iOS app deploys to versions earlier than iOS 11, see [`NSLocationAlwaysUsageDescription`](./nslocationalwaysusagedescription.md).

> ❗ **Important**:  This key is required if your iOS app uses APIs that access the user’s location information at all times.

## See Also

### Location
- [Choosing the  Location Services Authorization to Request](../choosing-the-location-services-authorization-to-request.md)
  Determine the authorization your app needs to access location data.
- [NSLocationUsageDescription](./nslocationusagedescription.md)
  A message that tells people why the app is requesting access to their location information.
- [NSLocationWhenInUseUsageDescription](./nslocationwheninuseusagedescription.md)
  A message that tells people why the app is requesting access to their location information while the app is running in the foreground.
- [NSLocationTemporaryUsageDescriptionDictionary](./nslocationtemporaryusagedescriptiondictionary.md)
  A collection of messages that explain why the app is requesting temporary access to their location.
- [NSLocationAlwaysUsageDescription](./nslocationalwaysusagedescription.md)
  A message that tells people why the app is requesting access to their location at all times.
- [NSWidgetWantsLocation](./nswidgetwantslocation.md)
  A Boolean value that indicates a widget uses the user’s location information.
- [NSLocationDefaultAccuracyReduced](./nslocationdefaultaccuracyreduced.md)
  A Boolean value that indicates whether the app requests reduced location accuracy by default.


---

*[View on Apple Developer](https://developer.apple.com/documentation/bundleresources/information-property-list/nslocationalwaysandwheninuseusagedescription)*