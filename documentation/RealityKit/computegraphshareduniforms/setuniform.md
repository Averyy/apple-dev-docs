# setUniform(_:)

**Framework**: RealityKit  
**Kind**: method

Stores a uniform value, replacing any previously stored value of the same type.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
func setUniform<V>(_ value: borrowing V) where V : BitwiseCopyable
```

## Parameters

- `value`: The value to store. Must conform to `BitwiseCopyable`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/computegraphshareduniforms/setuniform(_:))*