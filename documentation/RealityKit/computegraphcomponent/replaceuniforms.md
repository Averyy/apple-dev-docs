# replaceUniforms(_:)

**Framework**: RealityKit  
**Kind**: method

Replaces the entire uniform buffer with the given data.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- macOS 27.0+
- tvOS 27.0+
- visionOS 27.0+

## Declaration

```swift
mutating func replaceUniforms(_ data: Data)
```

#### Discussion

You can query `pipelines.assembly.uniformBufferSize` for the required size. If too few bytes are provided, the remaining bytes retain their previous values.

## Parameters

- `data`: Raw bytes to write into the uniform buffer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/computegraphcomponent/replaceuniforms(_:))*