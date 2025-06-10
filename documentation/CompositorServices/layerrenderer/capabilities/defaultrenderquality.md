# defaultRenderQuality

**Framework**: Compositor Services  
**Kind**: property

Returns default render quality allowed for drawing on this platform.

**Availability**:
- macOS 26.0+ (Beta)
- visionOS 26.0+ (Beta)

## Declaration

```swift
var defaultRenderQuality: LayerRenderer.RenderQuality { get }
```

#### Discussion

This should be used as a base value for the platform quality for drawing.

Use to set max render quality, see `LayerRenderer.Configuration.maxRenderQuality`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/compositorservices/layerrenderer/capabilities/defaultrenderquality)*