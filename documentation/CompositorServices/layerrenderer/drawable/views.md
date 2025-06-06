# views

**Framework**: Compositor Services  
**Kind**: property

An array of viewports that tell you how to draw to the drawable’s textures

**Availability**:
- visionOS 1.0+

## Declaration

```swift
var views: [LayerRenderer.Drawable.View] { get }
```

#### Discussion

The drawable provides one view for each distinct image you need to render. For example, a stereoscopic display contains a separate view for each eye.

## See Also

- [LayerRenderer.Drawable.View](layerrenderer/drawable/view.md)
  A type that provides information on how to render content into the frame’s textures.


---

*[View on Apple Developer](https://developer.apple.com/documentation/compositorservices/layerrenderer/drawable/views)*