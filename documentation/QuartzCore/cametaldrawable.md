# CAMetalDrawable

**Framework**: Core Animation  
**Kind**: protocol

A Metal drawable associated with a Core Animation layer.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- tvOS ?+
- visionOS ?+

## Declaration

```swift
protocol CAMetalDrawable : MTLDrawable
```

#### Overview

A [`CAMetalLayer`](cametallayer.md) instance owns any instance that implements this protocol. Don’t implement this protocol yourself. See the [`CAMetalLayer`](cametallayer.md) reference for information on how to request drawable objects.

## Topics

### Getting the Drawable’s Texture
- [var texture: any MTLTexture](cametaldrawable/texture.md)
  A Metal texture object that contains the drawable’s contents.
### Getting the Owning Layer
- [var layer: CAMetalLayer](cametaldrawable/layer.md)
  The layer that owns this drawable object.

## Relationships

### Inherits From
- [MTLDrawable](../Metal/MTLDrawable.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [class CAMetalLayer](cametallayer.md)
  A Core Animation layer that Metal can render into, typically displayed onscreen.
- [class CAEAGLLayer](caeagllayer.md)
  A layer that supports drawing OpenGL content in iOS and tvOS applications.
- [class CAEDRMetadata](caedrmetadata.md)
  Metadata describing how extended dynamic range (EDR) values should be tone mapped.
- [class CAOpenGLLayer](caopengllayer.md)
  A layer that provides a layer suitable for rendering OpenGL content.
- [class CARenderer](carenderer.md)
  A layer that allows an application to render a layer tree into a Core OpenGL context.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quartzcore/cametaldrawable)*