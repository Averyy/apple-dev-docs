# cp_layer_renderer_properties_get_view_count

**Framework**: Compositor Services  
**Kind**: func  
**Role**: Function

Returns the number of views that you must fill with content.

**Availability**:
- macOS 26.0+
- visionOS 1.0+

## Declaration

```c
size_t cp_layer_renderer_properties_get_view_count(cp_layer_renderer_properties_t layer_properties);
```

## Return Value

The number of views to fill with content. Fetch the views from the drawable of each frame.

## Discussion

This method tells you how many views you’re responsible for filling with your content. For example, this function returns `1` for a monoscopic display and `2` for a stereoscopic display.

## Parameters

- `layer_properties`: The layer properties to query.

## See Also

### Getting view port information
- [var viewport: MTLViewport](./layerrenderer/drawable/view/texturemap-swift.struct/viewport.md)
  The portion of the texture that the view uses to draw its content.


---

*[View on Apple Developer](https://developer.apple.com/documentation/compositorservices/cp_layer_renderer_properties_get_view_count)*