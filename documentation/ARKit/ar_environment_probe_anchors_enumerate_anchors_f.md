# ar_environment_probe_anchors_enumerate_anchors_f

**Framework**: ARKit  
**Kind**: func  
**Role**: Function

Enumerates a collection of environment probe anchors using a function.

**Availability**:
- visionOS 2.0+

## Declaration

```c
extern void ar_environment_probe_anchors_enumerate_anchors_f(ar_environment_probe_anchors_t environment_probe_anchors, void *context, ar_environment_probe_anchors_enumerator_function_t environment_probe_anchors_enumerator_function);
```

## Parameters

- `environment_probe_anchors`: The collection of environment probe anchors.
- `context`: The application-defined context parameter to pass to the function.
- `environment_probe_anchors_enumerator_function`: The enumerator function.

## See Also

### Environment probe functions
- [ar_environment_probe_anchor_get_environment_texture](./ar_environment_probe_anchor_get_environment_texture.md)
  Get the environment texture of an environment probe anchor.
- [ar_environment_probe_anchor_get_identifier](./ar_environment_probe_anchor_get_identifier.md)
  Get the identifier of an anchor.
- [ar_environment_probe_anchor_get_origin_from_anchor_transform](./ar_environment_probe_anchor_get_origin_from_anchor_transform.md)
  Get the transform from an anchor to the origin coordinate system.
- [ar_environment_probe_anchor_get_timestamp](./ar_environment_probe_anchor_get_timestamp.md)
  Get the timestamp corresponding to an anchor.
- [ar_environment_probe_anchor_is_equal_to_environment_probe_anchor](./ar_environment_probe_anchor_is_equal_to_environment_probe_anchor.md)
  Returns a bool value that indicates whether the two environment probe anchors are equal.
- [ar_environment_probe_anchors_enumerate_anchors](./ar_environment_probe_anchors_enumerate_anchors.md)
  Enumerates a collection of environment probe anchors.
- [ar_environment_probe_anchors_get_count](./ar_environment_probe_anchors_get_count.md)
  Get the count of environment probe anchors in the collection.
- [ar_environment_probe_anchor_get_origin_from_anchor_transform_with_correction](./ar_environment_probe_anchor_get_origin_from_anchor_transform_with_correction.md)
  Get the transform from an anchor to the origin coordinate system.


---

*[View on Apple Developer](https://developer.apple.com/documentation/arkit/ar_environment_probe_anchors_enumerate_anchors_f)*