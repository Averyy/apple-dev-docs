# isLoading

**Framework**: MapKit  
**Kind**: property  
**Role**: Instance Property

A Boolean value that indicates whether the current reverse geocoding request is in a loading state.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- tvOS 26.0+
- visionOS 26.0+
- watchOS 26.0+

## Declaration

```swift
var isLoading: Bool { get }
```

```objc
@property (nonatomic, readonly, getter=isLoading) BOOL loading;
```

## See Also

### Getting the reverse geocoder’s state
- [var isCancelled: Bool](./iscancelled.md)
  A Boolean value that indicates whether the current reverse geocoding request is in a cancelled state.
- [var location: CLLocation](./location.md)
  The location provided to the initializer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkit/mkreversegeocodingrequest/isloading)*