# setUniformData(_:for:)

**Framework**: RealityKit  
**Kind**: method

Sets the value of a uniform to raw bytes.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- macOS 27.0+
- tvOS 27.0+
- visionOS 27.0+

## Declaration

```swift
mutating func setUniformData(_ data: RawSpan, for handle: ComputeGraphComponent.UniformHandle)
```

## Parameters

- `data`: Raw bytes to write into the uniform.
- `handle`: The handle identifying the target uniform.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/computegraphcomponent/setuniformdata(_:for:))*