# setUniformValue(_:for:)

**Framework**: RealityKit  
**Kind**: method

Sets the value of a uniform to a `BitwiseCopyable` typed value.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- macOS 27.0+
- tvOS 27.0+
- visionOS 27.0+

## Declaration

```swift
mutating func setUniformValue<V>(_ value: V, for handle: ComputeGraphComponent.UniformHandle) where V : BitwiseCopyable
```

## Parameters

- `value`: The value to write.
- `handle`: The handle identifying the target uniform.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/computegraphcomponent/setuniformvalue(_:for:))*