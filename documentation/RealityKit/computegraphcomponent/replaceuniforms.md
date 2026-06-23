# replaceUniforms(_:)

**Framework**: RealityKit  
**Kind**: method

Replaces the entire uniform buffer with the given data.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

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