# defaultRenderQuality

**Framework**: Compositor Services  
**Kind**: property

The default render quality used on this platform.

**Availability**:
- macOS 26.0+ (Beta)
- visionOS 26.0+ (Beta)

## Declaration

```swift
var defaultRenderQuality: LayerRenderer.RenderQuality { get }
```

#### Discussion

This should be used as the base render quality value for the platform.

Use it to decide your maximum render quality, see `LayerRenderer.Configuration.maxRenderQuality`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/compositorservices/layerrenderer/capabilities/defaultrenderquality)*