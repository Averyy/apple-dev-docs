# subscript(_:_:)

**Framework**: RealityKit  
**Kind**: subscript

Returns the bindable value at the subscripted index.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 26.0+ (Beta)
- visionOS ?+

## Declaration

```swift
@MainActor
@preconcurrency subscript<T>(bindTarget: BindTarget, type: T.Type = T.self) -> BindableValue<T>? where T : BindableData { get set }
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/bindablevaluesreference/subscript(_:_:))*