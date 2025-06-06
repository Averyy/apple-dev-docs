# subscript(_:_:)

**Framework**: RealityKit  
**Kind**: subscript

Provides a bindable value for the given name.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- visionOS ?+

## Declaration

```swift
@MainActor
@preconcurrency subscript<T>(name: String, type: T.Type = T.self) -> BindableValue<T>? where T : BindableData { get set }
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/parameterset/subscript(_:_:))*