# isGeocoding

**Framework**: Core Location  
**Kind**: property

A Boolean value indicating whether the receiver is in the middle of geocoding its value.

**Availability**:
- iOS 5.0+
- iPadOS 5.0+
- Mac Catalyst 13.1+
- macOS 10.8+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
var isGeocoding: Bool { get }
```

#### Discussion

This property contains the value [`true`](https://developer.apple.com/documentation/Swift/true) if the process is ongoing or [`false`](https://developer.apple.com/documentation/Swift/false) if the process is done or has not yet been initiated.

## See Also

- [func cancelGeocode()](clgeocoder/cancelgeocode.md)
  Cancels a pending geocoding request.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corelocation/clgeocoder/isgeocoding)*