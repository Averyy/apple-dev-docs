# isGeocoding

**Framework**: Core Location  
**Kind**: property  
**Role**: Instance Property

A Boolean value indicating whether the receiver is in the middle of geocoding its value.

**Availability**:
- iOS 5.0+ - Deprecated in 26.0
- iPadOS 5.0+ - Deprecated in 26.0
- Mac Catalyst 13.1+ - Deprecated in 26.0
- macOS 10.8+ - Deprecated in 26.0
- tvOS 9.0+ - Deprecated in 26.0
- visionOS 1.0+ - Deprecated in 26.0
- watchOS 2.0+ - Deprecated in 26.0

> **Deprecated**: Use MapKit

## Declaration

```swift
var isGeocoding: Bool { get }
```

```objc
@property (nonatomic, readonly, getter=isGeocoding) BOOL geocoding;
```

## Discussion

This property contains the value [`true`](../../Swift/true.md) if the process is ongoing or [`false`](../../Swift/false.md) if the process is done or has not yet been initiated.

## See Also

### Managing geocoding requests
- [func cancelGeocode()](./cancelgeocode%28%29.md)
  Cancels a pending geocoding request.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corelocation/clgeocoder/isgeocoding)*