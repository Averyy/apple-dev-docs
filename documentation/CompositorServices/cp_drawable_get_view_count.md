# cp_drawable_get_view_count

**Framework**: Compositor Services  
**Kind**: func  
**Role**: Function

Returns the number of separate views to draw for the frame.

**Availability**:
- macOS 26.0+
- visionOS 1.0+

## Declaration

```c
size_t cp_drawable_get_view_count(cp_drawable_t drawable);
```

#### Return Value

The number of separate views to draw.

#### Discussion

The number of views corresponds to the number of separate versions of your scene you create for the frame. For a device with stereoscopic video, you render two views — one for each eye. The actual number of views can vary based on the drawing environment or your app’s configuration. For example, you typically render only one view in Simulator.

Fetch the actual views using the [`cp_drawable_get_view`](./cp_drawable_get_view.md) function.

## Parameters

- `drawable`: The drawable for a frame.

## See Also

### Getting the views
- [cp_drawable_get_view](./cp_drawable_get_view.md)
  Returns the specified view from the drawable.


---

*[View on Apple Developer](https://developer.apple.com/documentation/compositorservices/cp_drawable_get_view_count)*