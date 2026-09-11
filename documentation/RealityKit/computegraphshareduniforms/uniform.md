# uniform(_:)

**Framework**: RealityKit  
**Kind**: method

Returns the stored uniform value for the given type, or `nil` if none has been set.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- macOS 27.0+
- tvOS 27.0+
- visionOS 27.0+

## Declaration

```swift
func uniform<V>(_ type: V.Type) -> V? where V : BitwiseCopyable
```

#### Return Value

The stored value, or `nil`.

## Parameters

- `type`: The `BitwiseCopyable` type to retrieve.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/computegraphshareduniforms/uniform(_:))*