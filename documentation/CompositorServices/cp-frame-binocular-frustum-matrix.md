# cp_frame_binocular_frustum_matrix

**Framework**: Compositor Services  
**Kind**: func

**Availability**:
- macOS ?+
- visionOS 2.0+

## Declaration

```swift
simd_float4x4 cp_frame_binocular_frustum_matrix(cp_frame_t frame, cp_axis_direction_convention convention, simd_float4 increase_tangents, simd_float2 depth_range);
```

## See Also

- [cp_drawable_compute_projection](cp_drawable_compute_projection.md)
- [cp_frame_monocular_frustum_matrix](cp_frame_monocular_frustum_matrix.md)
- [cp_frame_timing_get_trackable_anchor_time](cp_frame_timing_get_trackable_anchor_time.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/compositorservices/cp_frame_binocular_frustum_matrix)*