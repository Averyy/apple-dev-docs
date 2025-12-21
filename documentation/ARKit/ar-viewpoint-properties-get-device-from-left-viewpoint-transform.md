# ar_viewpoint_properties_get_device_from_left_viewpoint_transform

**Framework**: ARKit  
**Kind**: func

Get the transformation matrix that converts from the left viewpoint to the device’s coordinate space.

**Availability**:
- visionOS 2.4+

## Declaration

```swift
extern simd_float4x4 ar_viewpoint_properties_get_device_from_left_viewpoint_transform(ar_viewpoint_properties_t viewpoint_properties);
```

#### Return Value

The transform from the left viewpoint to the device origin.

## Parameters

- `viewpoint_properties`: The viewpoint properties.

## See Also

- [ar_stereo_properties_configuration_t](ar_stereo_properties_configuration_t.md)
- [ar_stereo_properties_provider_t](ar_stereo_properties_provider_t.md)
- [ar_stereo_properties_configuration_create](ar_stereo_properties_configuration_create.md)
  Create a stereo properties configuration object.
- [ar_stereo_properties_provider_create](ar_stereo_properties_provider_create.md)
  Create a stereo properties provider.
- [ar_stereo_properties_provider_get_required_authorization_type](ar_stereo_properties_provider_get_required_authorization_type.md)
  Get the authorization type required by the stereo properties provider.
- [ar_stereo_properties_provider_get_viewpoint_properties](ar_stereo_properties_provider_get_viewpoint_properties.md)
  Returns the latest viewpoint properties.
- [ar_stereo_properties_provider_is_supported](ar_stereo_properties_provider_is_supported.md)
  Determines whether this device supports the stereo properties provider.
- [ar_viewpoint_properties_create](ar_viewpoint_properties_create.md)
  Create an `ar_viewpoint_properties_t`.
- [ar_viewpoint_properties_get_device_from_right_viewpoint_transform](ar_viewpoint_properties_get_device_from_right_viewpoint_transform.md)
  Get the transformation matrix that converts from the right viewpoint to the device’s coordinate space.
- [ar_viewpoint_properties_t](ar_viewpoint_properties_t.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/arkit/ar_viewpoint_properties_get_device_from_left_viewpoint_transform)*