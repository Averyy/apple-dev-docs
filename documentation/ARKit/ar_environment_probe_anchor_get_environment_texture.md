# ar_environment_probe_anchor_get_environment_texture

**Framework**: ARKit  
**Kind**: func  
**Role**: Function

Get the environment texture of an environment probe anchor.

**Availability**:
- visionOS 2.0+

## Declaration

```c
extern id<MTLTexture>ar_environment_probe_anchor_get_environment_texture(ar_environment_probe_anchor_t environment_probe);
```

## Return Value

Returns a `MTLTextureTypeCube`.

## Discussion

The texture is provided as a cube using MTLTextureTypeCube, containing rgb floating point linear high-dynamic range values in P3 color space.

> **Note**: Textures could be `nil` if the person is not in a well-lit environment. The lifetime of this texture is tied to the lifetime of the `ar_environment_probe_anchor_t`.

## Parameters

- `environment_probe`: An environment probe anchor.

## See Also

### Environment probe functions
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
- [ar_environment_probe_anchors_enumerate_anchors_f](./ar_environment_probe_anchors_enumerate_anchors_f.md)
  Enumerates a collection of environment probe anchors using a function.
- [ar_environment_probe_anchors_get_count](./ar_environment_probe_anchors_get_count.md)
  Get the count of environment probe anchors in the collection.
- [ar_environment_probe_anchor_get_origin_from_anchor_transform_with_correction](./ar_environment_probe_anchor_get_origin_from_anchor_transform_with_correction.md)
  Get the transform from an anchor to the origin coordinate system.


---

*[View on Apple Developer](https://developer.apple.com/documentation/arkit/ar_environment_probe_anchor_get_environment_texture)*