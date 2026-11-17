# ar_camera_video_format_enumerator_t

**Framework**: ARKit  
**Kind**: typealias  
**Role**: Type Alias

Handler for enumerating camera video formats.

**Availability**:
- visionOS 2.0+

## Declaration

```c
typedef _Bool (^)(NSObject<OS_ar_camera_video_format> *) ar_camera_video_format_enumerator_t;
```

## Return Value

`true` to continue enumerating, or `false` to stop enumerating.

## Parameters

- `camera_video_format`: The camera video format.

## See Also

### Camera data types
- [ar_camera_frame_parameters_t](./ar_camera_frame_parameters_t.md)
  Parameters for a camera frame including intrinsics, extrinsics, and timestamps.
- [ar_camera_frame_provider_t](./ar_camera_frame_provider_t.md)
  A data provider that delivers camera frames.
- [ar_camera_frame_sample_t](./ar_camera_frame_sample_t.md)
  A single camera frame sample with pixel buffer and metadata.
- [ar_camera_frame_t](./ar_camera_frame_t.md)
  A camera frame containing one or more camera frame samples.
- [ar_camera_frame_update_handler_function_t](./ar_camera_frame_update_handler_function_t.md)
  Function for observing an updated camera frame.
- [ar_camera_frame_update_handler_t](./ar_camera_frame_update_handler_t.md)
  Handler for observing an updated camera frame.
- [ar_camera_video_format_enumerator_function_t](./ar_camera_video_format_enumerator_function_t.md)
  Function for enumerating camera video formats.
- [ar_camera_video_format_t](./ar_camera_video_format_t.md)
  Describes a camera video format with frame rate, size, and pixel format.
- [ar_camera_video_formats_t](./ar_camera_video_formats_t.md)
  A collection of camera video formats.


---

*[View on Apple Developer](https://developer.apple.com/documentation/arkit/ar_camera_video_format_enumerator_t)*