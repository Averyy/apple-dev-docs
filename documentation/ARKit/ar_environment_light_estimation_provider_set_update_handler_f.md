# ar_environment_light_estimation_provider_set_update_handler_f

**Framework**: ARKit  
**Kind**: func  
**Role**: Function

Set the function for receiving environment light estimation updates.

**Availability**:
- visionOS 2.0+

## Declaration

```c
extern void ar_environment_light_estimation_provider_set_update_handler_f(ar_environment_light_estimation_provider_t environment_light_estimation_provider, dispatch_queue_t environment_light_estimation_anchor_updates_queue, void *context, ar_environment_light_estimation_update_handler_function_t environment_light_estimation_update_handler_function);
```

## Discussion

> **Note**: Setting this function will override the handler set using `ar_environment_light_estimation_provider_set_probe_update_handler`.

## Parameters

- `environment_light_estimation_provider`: The environment light estimation provider.
- `environment_light_estimation_anchor_updates_queue`: The queue on which the function will be called. Passing `NULL` will default to the main queue.
- `context`: The application-defined context parameter to pass to the function.
- `environment_light_estimation_update_handler_function`: The function to be called when new data arrives.

## See Also

### Environment lighting estimation functions
- [ar_environment_light_estimation_configuration_create](./ar_environment_light_estimation_configuration_create.md)
  Create an environment light estimation configuration.
- [ar_environment_light_estimation_provider_create](./ar_environment_light_estimation_provider_create.md)
  Create an environment light estimation provider.
- [ar_environment_light_estimation_provider_get_required_authorization_type](./ar_environment_light_estimation_provider_get_required_authorization_type.md)
  Get the authorization type required by the environment light estimation provider.
- [ar_environment_light_estimation_provider_is_supported](./ar_environment_light_estimation_provider_is_supported.md)
  Determines whether this device supports the environment light estimation provider.
- [ar_environment_light_estimation_provider_set_update_handler](./ar_environment_light_estimation_provider_set_update_handler.md)
  Set the handler for receiving environment light estimation updates.


---

*[View on Apple Developer](https://developer.apple.com/documentation/arkit/ar_environment_light_estimation_provider_set_update_handler_f)*