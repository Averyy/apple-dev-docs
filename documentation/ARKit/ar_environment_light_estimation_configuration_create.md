# ar_environment_light_estimation_configuration_create

**Framework**: ARKit  
**Kind**: func  
**Role**: Function

Create an environment light estimation configuration.

**Availability**:
- visionOS 2.0+

## Declaration

```c
extern ar_environment_light_estimation_configuration_tar_environment_light_estimation_configuration_create();
```

## Return Value

An instance of `ar_environment_light_estimation_configuration_t`.

## Discussion

> **Note**: This type supports ARC. In non-ARC files, use `ar_retain()` and `ar_release()` to retain and release the object.

## See Also

### Environment lighting estimation functions
- [ar_environment_light_estimation_provider_create](./ar_environment_light_estimation_provider_create.md)
  Create an environment light estimation provider.
- [ar_environment_light_estimation_provider_get_required_authorization_type](./ar_environment_light_estimation_provider_get_required_authorization_type.md)
  Get the authorization type required by the environment light estimation provider.
- [ar_environment_light_estimation_provider_is_supported](./ar_environment_light_estimation_provider_is_supported.md)
  Determines whether this device supports the environment light estimation provider.
- [ar_environment_light_estimation_provider_set_update_handler](./ar_environment_light_estimation_provider_set_update_handler.md)
  Set the handler for receiving environment light estimation updates.
- [ar_environment_light_estimation_provider_set_update_handler_f](./ar_environment_light_estimation_provider_set_update_handler_f.md)
  Set the function for receiving environment light estimation updates.


---

*[View on Apple Developer](https://developer.apple.com/documentation/arkit/ar_environment_light_estimation_configuration_create)*