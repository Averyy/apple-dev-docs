# makePipeline(desc:)

**Framework**: RealityKit  
**Kind**: method

Creates a compute pipeline asynchronously.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
final func makePipeline(desc: LowLevelDeformation.Pipeline.Descriptor) async throws -> LowLevelDeformation.Pipeline
```

#### Discussion

> **Note**: If the descriptor is invalid.

## Parameters

- `desc`: An object that describes the vertex layouts and deformer stages.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/lowleveldeformationcontext/makepipeline(desc:))*