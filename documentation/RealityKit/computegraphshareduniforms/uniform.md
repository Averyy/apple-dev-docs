# uniform(_:)

**Framework**: RealityKit  
**Kind**: method

Returns the stored uniform value for the given type, or `nil` if none has been set.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

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