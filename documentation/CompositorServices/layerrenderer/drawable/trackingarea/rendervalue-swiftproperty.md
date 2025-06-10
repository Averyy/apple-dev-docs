# renderValue

**Framework**: Compositor Services  
**Kind**: property

Returns the render value for the tracking area.

**Availability**:
- macOS 26.0+ (Beta)
- visionOS 26.0+ (Beta)

## Declaration

```swift
var renderValue: LayerRenderer.Drawable.TrackingArea.RenderValue { get }
```

#### Discussion

Use the returned value in the render pass of [`cp_drawable_get_tracking_areas_texture`](cp_drawable_get_tracking_areas_texture.md) for the pixel value of the tracking area identifier.


---

*[View on Apple Developer](https://developer.apple.com/documentation/compositorservices/layerrenderer/drawable/trackingarea/rendervalue-swift.property)*