# ar_environment_probe_anchor_get_origin_from_anchor_transform_with_correction

**Framework**: ARKit  
**Kind**: func  
**Role**: Function

Get the transform from an anchor to the origin coordinate system.

**Availability**:
- visionOS 27.0+

## Declaration

```c
extern simd_float4x4 ar_environment_probe_anchor_get_origin_from_anchor_transform_with_correction(ar_environment_probe_anchor_t anchor, ar_transform_correction_t transform_correction);
```

#### Return Value

The origin from anchor transform.

## Parameters

- `anchor`: The anchor.
- `transform_correction`: The transform correction that should be applied.

## See Also

### Environment probe functions
- [ar_environment_probe_anchor_get_environment_texture](./ar_environment_probe_anchor_get_environment_texture.md)
- [ar_environment_probe_anchor_get_identifier](./ar_environment_probe_anchor_get_identifier.md)
- [ar_environment_probe_anchor_get_origin_from_anchor_transform](./ar_environment_probe_anchor_get_origin_from_anchor_transform.md)
- [ar_environment_probe_anchor_get_timestamp](./ar_environment_probe_anchor_get_timestamp.md)
- [ar_environment_probe_anchor_is_equal_to_environment_probe_anchor](./ar_environment_probe_anchor_is_equal_to_environment_probe_anchor.md)
- [ar_environment_probe_anchors_enumerate_anchors](./ar_environment_probe_anchors_enumerate_anchors.md)
- [ar_environment_probe_anchors_enumerate_anchors_f](./ar_environment_probe_anchors_enumerate_anchors_f.md)
- [ar_environment_probe_anchors_get_count](./ar_environment_probe_anchors_get_count.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/arkit/ar_environment_probe_anchor_get_origin_from_anchor_transform_with_correction)*