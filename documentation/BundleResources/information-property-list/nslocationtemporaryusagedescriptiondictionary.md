# NSLocationTemporaryUsageDescriptionDictionary

**Framework**: Bundle Resources  
**Kind**: dictionary

A collection of messages that explain why the app is requesting temporary access to their location.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- macOS 11.0+
- visionOS 1.0+

#### Discussion

Use this key if your app needs temporary access to full accuracy location information. Provide a dictionary of messages that address different use cases, keyed by strings that you define. For example, if your app suggests nearby coffee shops in one part of the app, and finds nearby friends in another, you could include two entries:

![A screenshot of the NSLocationTemporaryUsageDescriptionDictionary item in the Xcode property list editor showing two entries. The first entry has the key friends and a value that says your location is used to connect with nearby friends. The second entry has the key coffee and a value that says your location is used to find the closest coffee shop.](https://docs-assets.developer.apple.com/published/9f8690a62d7d5ae92fb5f59a3410620a/media-3729482%402x.png)

When you request access, select among the messages at run time by providing the associated key to the [`requestTemporaryFullAccuracyAuthorization(withPurposeKey:)`](https://developer.apple.com/documentation/CoreLocation/CLLocationManager/requestTemporaryFullAccuracyAuthorization(withPurposeKey:)) method:

```swift
// Request location access to find coffee shops.
manager.requestTemporaryFullAccuracyAuthorization(withPurposeKey: "coffee")
```

## See Also

- [Choosing the  Location Services Authorization to Request](choosing-the-location-services-authorization-to-request.md)
  Determine the authorization your app needs to access location data.
- [NSLocationAlwaysAndWhenInUseUsageDescription](information-property-list/nslocationalwaysandwheninuseusagedescription.md)
  A message that tells people why the app is requesting access to their location information at all times.
- [NSLocationUsageDescription](information-property-list/nslocationusagedescription.md)
  A message that tells people why the app is requesting access to their location information.
- [NSLocationWhenInUseUsageDescription](information-property-list/nslocationwheninuseusagedescription.md)
  A message that tells people why the app is requesting access to their location information while the app is running in the foreground.
- [NSLocationAlwaysUsageDescription](information-property-list/nslocationalwaysusagedescription.md)
  A message that tells people why the app is requesting access to their location at all times.
- [NSWidgetWantsLocation](information-property-list/nswidgetwantslocation.md)
  A Boolean value that indicates a widget uses the user’s location information.
- [NSLocationDefaultAccuracyReduced](information-property-list/nslocationdefaultaccuracyreduced.md)
  A Boolean value that indicates whether the app requests reduced location accuracy by default.


---

*[View on Apple Developer](https://developer.apple.com/documentation/bundleresources/information-property-list/nslocationtemporaryusagedescriptiondictionary)*