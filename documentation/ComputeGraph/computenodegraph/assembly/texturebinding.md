# ComputeNodeGraph.Assembly.TextureBinding

**Framework**: Compute Graph  
**Kind**: struct  
**Role**: Structure

Describes how a Metal texture is bound to a compute pipeline stage.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- tvOS 27.0+
- visionOS 27.0+
- Reality Composer Pro

## Declaration

```swift
struct TextureBinding
```

## Overview

A texture binding pairs an [`ComputeNodeGraph.Assembly.Attachment`](./attachment.md) (how the texture is connected to the graph) with an optional `MTLTextureType` indicating the texture’s dimensionality.

## Topics

### Initializers
- [init(attachment: ComputeNodeGraph.Assembly.Attachment, type: MTLTextureType?)](./texturebinding/init%28attachment,type%29.md)
### Instance Properties
- [var attachment: ComputeNodeGraph.Assembly.Attachment](./texturebinding/attachment.md)
  The attachment point that provides this texture.
- [var type: MTLTextureType?](./texturebinding/type.md)
  The texture type (e.g. `.type2D`, `.typeCube`), or `nil` if unspecified.

## Relationships

### Conforms To
- [Equatable](../../../Swift/equatable.md)
- [Sendable](../../../Swift/sendable.md)
- [SendableMetatype](../../../Swift/sendablemetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/computegraph/computenodegraph/assembly/texturebinding)*