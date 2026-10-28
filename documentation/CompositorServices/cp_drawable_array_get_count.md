# cp_drawable_array_get_count

**Framework**: Compositor Services  
**Kind**: func  
**Role**: Function

Returns the number of drawables in the array.

**Availability**:
- macOS 26.0+
- visionOS 26.0+

## Declaration

```c
size_t cp_drawable_array_get_count(cp_drawable_array_t drawable_array);
```

## Return Value

The number of drawables available for drawing. For example, a return value of `2` indicates there are two drawables for this frame.

## Discussion

Use the returned value as the maximum number of textures to retrieve from the [`cp_drawable_array_get_drawable`](./cp_drawable_array_get_drawable.md) functions.

## Parameters

- `drawable_array`: The drawable array for a frame.


---

*[View on Apple Developer](https://developer.apple.com/documentation/compositorservices/cp_drawable_array_get_count)*