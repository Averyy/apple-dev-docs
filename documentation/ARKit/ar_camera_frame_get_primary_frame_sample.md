# ar_camera_frame_get_primary_frame_sample

**Framework**: ARKit  
**Kind**: func  
**Role**: Function

Get the primary frame sample for this camera frame.

**Availability**:
- visionOS 2.0+

## Declaration

```c
extern ar_camera_frame_sample_tar_camera_frame_get_primary_frame_sample(ar_camera_frame_t camera_frame);
```

## Return Value

An instance of `ar_camera_frame_sample_t`.

## Parameters

- `camera_frame`: The camera frame.

## See Also

### Camera functions
- [ar_camera_video_format_copy_supported_video_formats](./ar_camera_video_format_copy_supported_video_formats.md)
  Returns a collection of supported video formats for a given camera type and position.
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
- [ar_camera_frame_provider_get_required_authorization_type](./ar_camera_frame_provider_get_required_authorization_type.md)
  Get the authorization type required by the camera frame provider.


---

*[View on Apple Developer](https://developer.apple.com/documentation/arkit/ar_camera_frame_get_primary_frame_sample)*