# cp_drawable_set_device_anchor

**Framework**: Compositor Services  
**Kind**: func  
**Role**: Function

Specifies the world position and orientation to apply to the current frame.

**Availability**:
- macOS 26.0+
- visionOS 1.0+

## Declaration

```c
void cp_drawable_set_device_anchor(cp_drawable_t drawable, ar_device_anchor_t device_anchor);
```

## Mentions

- [Drawing fully immersive content using Metal](./drawing-fully-immersive-content-using-metal.md)

#### Discussion

During rendering, match the camera position in your scene to the device anchor to create a better experience. In a visionOS app, the device anchor corresponds to the movements of someone’s head. If your camera movements aren’t synchronized to the device movements, the person might experience discomfort while viewing your content.

Because you encode your drawing commands before the final rendered frame appears, you must predict the device anchor in advance. ARKit provides the [`ar_world_tracking_provider_query_device_anchor_at_timestamp`](../ARKit/ar_world_tracking_provider_query_device_anchor_at_timestamp.md) function to help you determine this information. Use the value from the [`cp_frame_timing_get_presentation_time`](./cp_frame_timing_get_presentation_time.md) function as the time for the request. Start the prediction process at some point after the time the [`cp_frame_timing_get_optimal_input_time`](./cp_frame_timing_get_optimal_input_time.md) function returns.

At display time, Compositor Services compares your predicted device anchor with the actual position and orientation of the device at that time. If the two values don’t match, Compositor Services adjusts the pixels of your frame to align it with the hardware. If you don’t want it to make this adjustment, specify `nil` for the `device_anchor` parameter or don’t call this function.

## Parameters

- `drawable`: The drawable for a frame.
- `device_anchor`: The anchor that specifies the 3D rotation, translation, and scaling factors you applied to your content when you rendered the frame. If you specify `nil`, Compositor Services doesn’t adjust your content to match the actual display-time position and orientation of the device.

## See Also

### Accessing the device orientation
- [cp_drawable_get_device_anchor](./cp_drawable_get_device_anchor.md)
  Returns the position and orientation you specified for the frame.


---

*[View on Apple Developer](https://developer.apple.com/documentation/compositorservices/cp_drawable_set_device_anchor)*