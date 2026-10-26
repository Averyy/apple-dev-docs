# cp_drawable_get_view

**Framework**: Compositor Services  
**Kind**: func  
**Role**: Function

Returns the specified view from the drawable.

**Availability**:
- macOS 26.0+
- visionOS 1.0+

## Declaration

```c
cp_view_tcp_drawable_get_view(cp_drawable_t drawable, size_t index);
```

#### Return Value

The view at the specified index.

#### Discussion

The drawable provides one view for each distinct image you need to render. For example, a stereoscopic display contains a separate view for each eye.

## Parameters

- `drawable`: The drawable for a frame.
- `index`: The zero-based index of the view you want. The index must be greater than or equal to 0 and less than the value that [`cp_drawable_get_view_count`](./cp_drawable_get_view_count.md) returns.

## See Also

### Getting the views
- [cp_drawable_get_view_count](./cp_drawable_get_view_count.md)
  Returns the number of separate views to draw for the frame.


---

*[View on Apple Developer](https://developer.apple.com/documentation/compositorservices/cp_drawable_get_view)*