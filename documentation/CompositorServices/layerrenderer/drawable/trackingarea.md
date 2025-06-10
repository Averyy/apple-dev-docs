# LayerRenderer.Drawable.TrackingArea

**Framework**: Compositor Services  
**Kind**: struct

**Availability**:
- macOS 26.0+ (Beta)
- visionOS 26.0+ (Beta)

## Declaration

```swift
struct TrackingArea
```

## Topics

### Structures
- [LayerRenderer.Drawable.TrackingArea.HoverEffect](layerrenderer/drawable/trackingarea/hovereffect.md)
  Hover effect that will be automatically rendered by CompositorServices, when the area is looked at.
- [LayerRenderer.Drawable.TrackingArea.Identifier](layerrenderer/drawable/trackingarea/identifier-swift.struct.md)
  An identifier for the tracking area.
- [LayerRenderer.Drawable.TrackingArea.RenderValue](layerrenderer/drawable/trackingarea/rendervalue-swift.struct.md)
  A value used when rendering a tracking area.
### Initializers
- [init()](layerrenderer/drawable/trackingarea/init.md)
### Instance Properties
- [var identifier: LayerRenderer.Drawable.TrackingArea.Identifier](layerrenderer/drawable/trackingarea/identifier-swift.property.md)
  Returns the identifier for the tracking area.
- [var renderValue: LayerRenderer.Drawable.TrackingArea.RenderValue](layerrenderer/drawable/trackingarea/rendervalue-swift.property.md)
  Returns the render value for the tracking area.
### Instance Methods
- [func addHoverEffect(LayerRenderer.Drawable.TrackingArea.HoverEffect)](layerrenderer/drawable/trackingarea/addhovereffect(_:).md)
  Add an hover effect for this tracking area. No hover effect will be rendered if this isn’t called.

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/compositorservices/layerrenderer/drawable/trackingarea)*