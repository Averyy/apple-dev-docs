# NSLocationAlwaysUsageDescription

**Framework**: Bundle Resources  
**Kind**: typealias  
**Role**: Property List Key

A message that tells people why the app is requesting access to their location at all times.

**Availability**:
- iOS 8.0+ - Deprecated in 10.0
- iPadOS 8.0+ - Deprecated in 10.0

> **Deprecated**: For apps deployed to targets in iOS 11 and later, use [`NSLocationAlwaysAndWhenInUseUsageDescription`](./nslocationalwaysandwheninuseusagedescription.md) instead.

## Details

- **Name**: `NSLocationAlwaysUsageDescription` (Privacy - Location Always Usage Description)
- **Type**: string

## Discussion

Use this key if your iOS app accesses location information in the background, and you deploy to a target earlier than iOS 11. In that case, add both this key and [`NSLocationAlwaysAndWhenInUseUsageDescription`](./nslocationalwaysandwheninuseusagedescription.md) to your app’s `Info.plist` file with the same message. Apps running on older versions of the OS use the message associated with [`NSLocationAlwaysUsageDescription`](./nslocationalwaysusagedescription.md), while apps running on later versions use the one associated with [`NSLocationAlwaysAndWhenInUseUsageDescription`](./nslocationalwaysandwheninuseusagedescription.md).

If your app only needs location information when in the foreground, use [`NSLocationWhenInUseUsageDescription`](./nslocationwheninuseusagedescription.md) instead. For more information, see [Choosing the  Location Services Authorization to Request](../choosing-the-location-services-authorization-to-request.md).

If you need location information in a macOS app, use [`NSLocationUsageDescription`](./nslocationusagedescription.md) instead.

> ❗ **Important**:  This key is required if your iOS app uses APIs that access the user’s location at all times and deploys to targets earlier than iOS 11.

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
- [NSWidgetWantsLocation](./nswidgetwantslocation.md)
  A Boolean value that indicates a widget uses the user’s location information.
- [NSLocationDefaultAccuracyReduced](./nslocationdefaultaccuracyreduced.md)
  A Boolean value that indicates whether the app requests reduced location accuracy by default.


---

*[View on Apple Developer](https://developer.apple.com/documentation/bundleresources/information-property-list/nslocationalwaysusagedescription)*