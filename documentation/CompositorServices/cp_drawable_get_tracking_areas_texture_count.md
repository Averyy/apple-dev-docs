# cp_drawable_get_tracking_areas_texture_count

**Framework**: Compositor Services  
**Kind**: func  
**Role**: Function

Returns the number of tracking areas textures available in the drawable.

**Availability**:
- macOS 26.0+
- visionOS 26.0+

## Declaration

```c
size_t cp_drawable_get_tracking_areas_texture_count(cp_drawable_t drawable);
```

## Return Value

The number of textures available for drawing. For example, a return value of `2` indicates there are two tracking areas textures available.

## Discussion

Use the returned value as the maximum number of textures to retrieve from the [`cp_drawable_get_tracking_areas_texture`](./cp_drawable_get_tracking_areas_texture.md)function. This will be equal to [`cp_drawable_get_texture_count`](./cp_drawable_get_texture_count.md) when tracking areas textures are enabled through the configuration otherwise will be 0.

## Parameters

- `drawable`: The drawable for a frame.


---

*[View on Apple Developer](https://developer.apple.com/documentation/compositorservices/cp_drawable_get_tracking_areas_texture_count)*