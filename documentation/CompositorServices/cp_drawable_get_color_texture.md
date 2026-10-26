# cp_drawable_get_color_texture

**Framework**: Compositor Services  
**Kind**: func  
**Role**: Function

Returns the color texture at the specified index in the drawable.

**Availability**:
- macOS 26.0+
- visionOS 1.0+

## Declaration

```c
id<MTLTexture>cp_drawable_get_color_texture(cp_drawable_t drawable, size_t index);
```

#### Return Value

The Metal color texture at the specified index.

#### Discussion

Use the returned texture in your render pipeline to store the pixels you want to appear. The layer’s texture topology determines the total number of textures, and the layout and content for each texture. Use the drawable’s views to map your content into specific portions of the textures.

## Parameters

- `drawable`: The drawable for a frame.
- `index`: The index of the color texture you want. The index must be greater than or equal to `0` and less than the value that [`cp_drawable_get_texture_count`](./cp_drawable_get_texture_count.md) returns.

## See Also

### Getting the render textures
- [cp_drawable_get_texture_count](./cp_drawable_get_texture_count.md)
  Returns the number of color and depth textures available in the drawable.
- [cp_drawable_get_depth_texture](./cp_drawable_get_depth_texture.md)
  Returns the depth texture at the specified index in the drawable.


---

*[View on Apple Developer](https://developer.apple.com/documentation/compositorservices/cp_drawable_get_color_texture)*