# geocodeAddressString(_:inRegionCenteredAt:inRegionRadius:preferredLocale:completionHandler:)

**Framework**: Core Location  
**Kind**: method  
**Role**: Instance Method

**Availability**:
- visionOS 1.0+ - Deprecated in 26.0

> **Deprecated**: Use MKGeocodingRequest

## Declaration

```swift
func geocodeAddressString(_ addressString: String, inRegionCenteredAt centroid: CLLocationCoordinate2D, inRegionRadius radius: CLLocationDistance, preferredLocale locale: Locale?, completionHandler: @escaping @Sendable ([CLPlacemark]?, (any Error)?) -> Void)
```

```swift
func geocodeAddressString(_ addressString: String, inRegionCenteredAt centroid: CLLocationCoordinate2D, inRegionRadius radius: CLLocationDistance, preferredLocale locale: Locale?) async throws -> [CLPlacemark]
```

```objc
- (void) geocodeAddressString:(NSString *) addressString inRegionCenteredAt:(CLLocationCoordinate2D) centroid inRegionRadius:(CLLocationDistance) radius preferredLocale:(NSLocale *) locale completionHandler:(CLGeocodeCompletionHandler) completionHandler;
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/corelocation/clgeocoder/geocodeaddressstring(_:inregioncenteredat:inregionradius:preferredlocale:completionhandler:))*