# cp_drawable_get_rasterization_rate_map_count

**Framework**: Compositor Services  
**Kind**: func  
**Role**: Function

Returns the number of rasterization rate maps associated with the drawable.

**Availability**:
- macOS 26.0+
- visionOS 1.0+

## Declaration

```c
size_t cp_drawable_get_rasterization_rate_map_count(cp_drawable_t drawable);
```

#### Return Value

The number of rasterization rate maps available for drawing.

#### Discussion

Use the returned value as the maximum number of rate maps to retrieve from the [`cp_drawable_get_rasterization_rate_map`](./cp_drawable_get_rasterization_rate_map.md) function.

## Parameters

- `drawable`: The drawable for a frame.

## See Also

### Getting the rasterization rate map
- [cp_drawable_get_rasterization_rate_map](./cp_drawable_get_rasterization_rate_map.md)
  Returns the rasterization rate map at the specified index in the drawable.
- [cp_drawable_get_flipped_rasterization_rate_map](./cp_drawable_get_flipped_rasterization_rate_map.md)
  Returns the flipped rasterization rate map at the specified index in the drawable.


---

*[View on Apple Developer](https://developer.apple.com/documentation/compositorservices/cp_drawable_get_rasterization_rate_map_count)*