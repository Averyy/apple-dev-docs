# ar_camera_frame_provider_set_update_handler

**Framework**: ARKit  
**Kind**: func  
**Role**: Function

Set the handler for receiving camera frame updates for the given video format.

**Availability**:
- visionOS 2.0+

## Declaration

```c
extern void ar_camera_frame_provider_set_update_handler(ar_camera_frame_provider_t camera_frame_provider, ar_camera_video_format_t camera_video_format, dispatch_queue_t camera_frame_update_queue, ar_camera_frame_update_handler_t camera_frame_update_handler);
```

## Discussion

An enterprise license and/or entitlement is required to receive camera frames, and will otherwise be a no-op.

> **Note**: Setting this handler will override the function set using `ar_camera_frame_provider_set_update_handler_f` for given `ar_camera_video_format_t`.

## Parameters

- `camera_frame_provider`: The camera frame provider.
- `camera_video_format`: The camera video format.
- `camera_frame_update_queue`: The camera frame update queue. Passing `NULL` will default to the main queue.
- `camera_frame_update_handler`: The camera frame update handler.

## See Also

### Camera functions
- [ar_camera_video_format_copy_supported_video_formats](./ar_camera_video_format_copy_supported_video_formats.md)
  Returns a collection of supported video formats for a given camera type and position.
- [ar_camera_frame_get_primary_frame_sample](./ar_camera_frame_get_primary_frame_sample.md)
  Get the primary frame sample for this camera frame.
- [ar_camera_video_format_get_maximum_frame_duration](./ar_camera_video_format_get_maximum_frame_duration.md)
  Get the maximum frame duration for this video format.
- [ar_camera_video_format_get_minimum_frame_duration](./ar_camera_video_format_get_minimum_frame_duration.md)
  Get the minimum frame duration for this video format.
- [ar_camera_frame_is_equal_to_camera_frame](./ar_camera_frame_is_equal_to_camera_frame.md)
  Returns a bool value that indicates whether the two camera frames are equal.
- [ar_camera_frame_parameters_get_camera_position](./ar_camera_frame_parameters_get_camera_position.md)
  Get the camera position.
- [ar_camera_frame_parameters_get_camera_type](./ar_camera_frame_parameters_get_camera_type.md)
  Get the camera type.
- [ar_camera_frame_parameters_get_capture_timestamp](./ar_camera_frame_parameters_get_capture_timestamp.md)
  Get the frame capture timestamp.
- [ar_camera_frame_parameters_get_color_temperature](./ar_camera_frame_parameters_get_color_temperature.md)
  Get the white balance correlated color temperature in kelvin.
- [ar_camera_frame_parameters_get_exposure_duration](./ar_camera_frame_parameters_get_exposure_duration.md)
  Get the frame exposure duration.
- [ar_camera_frame_parameters_get_extrinsics](./ar_camera_frame_parameters_get_extrinsics.md)
  Get the camera extrinsics.
- [ar_camera_frame_parameters_get_intrinsics](./ar_camera_frame_parameters_get_intrinsics.md)
  Get the camera intrinsics.
- [ar_camera_frame_parameters_get_mid_exposure_timestamp](./ar_camera_frame_parameters_get_mid_exposure_timestamp.md)
  Get the frame mid exposure timestamp.
- [ar_camera_frame_parameters_is_equal_to_camera_frame_parameters](./ar_camera_frame_parameters_is_equal_to_camera_frame_parameters.md)
  Returns a bool value that indicates whether the two camera frame parameters are equal.
- [ar_camera_frame_provider_create](./ar_camera_frame_provider_create.md)
  Create a camera frame provider.


---

*[View on Apple Developer](https://developer.apple.com/documentation/arkit/ar_camera_frame_provider_set_update_handler)*