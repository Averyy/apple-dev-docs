# ar_environment_light_estimation_provider_is_supported

**Framework**: ARKit  
**Kind**: func  
**Role**: Function

Determines whether this device supports the environment light estimation provider.

**Availability**:
- visionOS 2.0+

## Declaration

```c
extern bool ar_environment_light_estimation_provider_is_supported();
```

## Return Value

Returns `true` if the environment light estimation provider is supported on this device, `false` otherwise.

## See Also

### Environment lighting estimation functions
- [ar_environment_light_estimation_configuration_create](./ar_environment_light_estimation_configuration_create.md)
  Create an environment light estimation configuration.
- [ar_environment_light_estimation_provider_create](./ar_environment_light_estimation_provider_create.md)
  Create an environment light estimation provider.
- [ar_environment_light_estimation_provider_get_required_authorization_type](./ar_environment_light_estimation_provider_get_required_authorization_type.md)
  Get the authorization type required by the environment light estimation provider.
- [ar_environment_light_estimation_provider_set_update_handler](./ar_environment_light_estimation_provider_set_update_handler.md)
  Set the handler for receiving environment light estimation updates.
- [ar_environment_light_estimation_provider_set_update_handler_f](./ar_environment_light_estimation_provider_set_update_handler_f.md)
  Set the function for receiving environment light estimation updates.


---

*[View on Apple Developer](https://developer.apple.com/documentation/arkit/ar_environment_light_estimation_provider_is_supported)*