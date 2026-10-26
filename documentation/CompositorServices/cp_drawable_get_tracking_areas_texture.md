# cp_drawable_get_tracking_areas_texture

**Framework**: Compositor Services  
**Kind**: func  
**Role**: Function

Returns the tracking areas texture at the specified index in the drawable.

**Availability**:
- macOS 26.0+
- visionOS 26.0+

## Declaration

```c
id<MTLTexture>cp_drawable_get_tracking_areas_texture(cp_drawable_t drawable, size_t index);
```

#### Return Value

The Metal object index texture at the specified index.

#### Discussion

Use the returned texture in your render pipeline to store the tracking areas ID used for hover effects and indirect gestures. The layer’s texture topology determines the layout and content for each texture. The drawable’s views contain information about how those views map to the textures.

## Parameters

- `drawable`: The drawable for a frame.
- `index`: The index of the texture you want. The index must be greater than or equal to `0` and less than the value that [`cp_drawable_get_tracking_areas_texture_count`](./cp_drawable_get_tracking_areas_texture_count.md) returns.


---

*[View on Apple Developer](https://developer.apple.com/documentation/compositorservices/cp_drawable_get_tracking_areas_texture)*