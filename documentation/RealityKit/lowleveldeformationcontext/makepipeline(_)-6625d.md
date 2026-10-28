# makePipeline(_:)

**Framework**: RealityKit  
**Kind**: method  
**Role**: Instance Method

Creates a compute pipeline asynchronously.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- tvOS 27.0+
- visionOS 27.0+

## Declaration

```swift
nonisolated(nonsending)
final func makePipeline(_ descriptor: LowLevelDeformation.Pipeline.Descriptor) async throws -> LowLevelDeformation.Pipeline
```

**Other overloads**:

```swift
final func makePipeline(_ descriptor: LowLevelDeformation.Pipeline.Descriptor) throws -> LowLevelDeformation.Pipeline
```

## Discussion

> **Throws**: If the descriptor is invalid.

## Parameters

- `descriptor`: An object that describes the vertex layouts and deformer stages.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/lowleveldeformationcontext/makepipeline(_:)-6625d)*