# subscript(_:_:)

**Framework**: RealityKit  
**Kind**: subscript

Accessor for the parameters, returns a bindable value.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 26.0+ (Beta)

## Declaration

```swift
@MainActor
@preconcurrency subscript<T>(name: String, type: T.Type = T.self) -> BindableValue<T>? where T : BindableData { get set }
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/entity/parameterset-3cp4c/subscript(_:_:))*