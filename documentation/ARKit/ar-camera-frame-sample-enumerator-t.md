# ar_camera_frame_sample_enumerator_t

**Framework**: ARKit  
**Kind**: typealias

Handler for enumerating camera frame samples.

**Availability**:
- visionOS 26.0+

## Declaration

```swift
typedef _Bool (^)(NSObject<OS_ar_camera_frame_sample> *) ar_camera_frame_sample_enumerator_t;
```

#### Return Value

`true` to continue enumerating, or `false` to stop enumerating.

## Parameters

- `camera_frame_sample`: The camera frame sample.

## See Also

- [ar_camera_frame_sample_enumerator_function_t](ar_camera_frame_sample_enumerator_function_t.md)
  Function for enumerating camera frame samples.
- [ar_camera_frame_samples_t](ar_camera_frame_samples_t.md)
- [ar_camera_frame_get_frame_samples](ar_camera_frame_get_frame_samples.md)
  Get the collection of camera frame samples for this camera frame.
- [ar_camera_frame_samples_enumerate_frame_samples](ar_camera_frame_samples_enumerate_frame_samples.md)
  Enumerate all camera frame samples in this collection.
- [ar_camera_frame_samples_enumerate_frame_samples_f](ar_camera_frame_samples_enumerate_frame_samples_f.md)
  Enumerate all supported camera frame samples for this configuration using a function.
- [ar_camera_frame_samples_get_count](ar_camera_frame_samples_get_count.md)
  Get the count of camera frame samples in the collection.
- [ar_camera_video_format_get_camera_rectification_type](ar_camera_video_format_get_camera_rectification_type.md)
  Get the camera rectification type for this video format.
- [ar_camera_rectification_type_t](ar_camera_rectification_type_t.md)
  A value describing the type of rectification applied to a video format.


---

*[View on Apple Developer](https://developer.apple.com/documentation/arkit/ar_camera_frame_sample_enumerator_t)*