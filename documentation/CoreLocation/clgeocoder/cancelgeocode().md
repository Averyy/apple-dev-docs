# cancelGeocode()

**Framework**: Core Location  
**Kind**: method  
**Role**: Instance Method

Cancels a pending geocoding request.

**Availability**:
- iOS 5.0+ - Deprecated in 26.0
- iPadOS 5.0+ - Deprecated in 26.0
- Mac Catalyst 13.1+ - Deprecated in 26.0
- macOS 10.8+ - Deprecated in 26.0
- tvOS 9.0+ - Deprecated in 26.0
- visionOS 1.0+ - Deprecated in 26.0
- watchOS 2.0+ - Deprecated in 26.0

> **Deprecated**: Use MKGeocodingRequest

## Declaration

```swift
func cancelGeocode()
```

```objc
- (void) cancelGeocode;
```

#### Discussion

You can use this method to cancel a pending request and free up the resources associated with that request. Canceling a pending request causes the completion handler block to be called.

If the request is not pending, because it has already returned or has not yet begun, this method does nothing.

## See Also

### Managing geocoding requests
- [var isGeocoding: Bool](./isgeocoding.md)
  A Boolean value indicating whether the receiver is in the middle of geocoding its value.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corelocation/clgeocoder/cancelgeocode())*