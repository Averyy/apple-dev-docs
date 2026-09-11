# ComputeNodeGraph.Assembly.TextureBinding

**Framework**: Compute Graph  
**Kind**: struct

Describes how a Metal texture is bound to a compute pipeline stage.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- tvOS 27.0+
- visionOS 27.0+
- Reality Composer Pro ?+

## Declaration

```swift
struct TextureBinding
```

#### Overview

A texture binding pairs an [`ComputeNodeGraph.Assembly.Attachment`](computenodegraph/assembly/attachment.md) (how the texture is connected to the graph) with an optional `MTLTextureType` indicating the texture’s dimensionality.

## Topics

### Initializers
- [init(attachment: ComputeNodeGraph.Assembly.Attachment, type: MTLTextureType?)](computenodegraph/assembly/texturebinding/init(attachment:type:).md)
### Instance Properties
- [var attachment: ComputeNodeGraph.Assembly.Attachment](computenodegraph/assembly/texturebinding/attachment.md)
  The attachment point that provides this texture.
- [var type: MTLTextureType?](computenodegraph/assembly/texturebinding/type.md)
  The texture type (e.g. `.type2D`, `.typeCube`), or `nil` if unspecified.

## Relationships

### Conforms To
- [Equatable](../swift/equatable.md)
- [Sendable](../swift/sendable.md)
- [SendableMetatype](../swift/sendablemetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/computegraph/computenodegraph/assembly/texturebinding)*