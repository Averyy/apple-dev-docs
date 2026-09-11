# makePipeline(_:)

**Framework**: RealityKit  
**Kind**: method

Creates a compute pipeline synchronously.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- tvOS 27.0+
- visionOS 27.0+

## Declaration

```swift
final func makePipeline(_ descriptor: LowLevelDeformation.Pipeline.Descriptor) throws -> LowLevelDeformation.Pipeline
```

#### Discussion

> **Note**: If the descriptor is invalid.

## Parameters

- `descriptor`: An object that describes the vertex layouts and deformer stages.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/lowleveldeformationcontext/makepipeline(_:))*