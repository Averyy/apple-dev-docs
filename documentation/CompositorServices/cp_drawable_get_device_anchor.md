# cp_drawable_get_device_anchor

**Framework**: Compositor Services  
**Kind**: func  
**Role**: Function

Returns the position and orientation you specified for the frame.

**Availability**:
- macOS 26.0+
- visionOS 1.0+

## Declaration

```c
ar_device_anchor_tcp_drawable_get_device_anchor(cp_drawable_t drawable);
```

## Return Value

The current position and orientation for the frame, or `nil` if you didn’t specify this information.

## Parameters

- `drawable`: The drawable for a frame.

## See Also

### Accessing the device orientation
- [cp_drawable_set_device_anchor](./cp_drawable_set_device_anchor.md)
  Specifies the world position and orientation to apply to the current frame.


---

*[View on Apple Developer](https://developer.apple.com/documentation/compositorservices/cp_drawable_get_device_anchor)*