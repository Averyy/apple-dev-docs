# ar_environment_light_estimation_provider_set_update_handler

**Framework**: ARKit  
**Kind**: func  
**Role**: Function

Set the handler for receiving environment light estimation updates.

**Availability**:
- visionOS 2.0+

## Declaration

```c
extern void ar_environment_light_estimation_provider_set_update_handler(ar_environment_light_estimation_provider_t environment_light_estimation_provider, dispatch_queue_t environment_light_estimation_anchor_updates_queue, ar_environment_light_estimation_update_handler_t environment_light_estimation_update_handler);
```

## Discussion

> **Note**: Setting this function will override the handler set using `ar_environment_light_estimation_provider_set_probe_update_handler_f`.

## Parameters

- `environment_light_estimation_provider`: Environment light estimation provider.
- `environment_light_estimation_anchor_updates_queue`: Queue on which the handler will be executed, sending `NULL` will default to the main queue.
- `environment_light_estimation_update_handler`: Handler to be triggered when new data arrives.

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
- [ar_environment_light_estimation_provider_set_update_handler_f](./ar_environment_light_estimation_provider_set_update_handler_f.md)
  Set the function for receiving environment light estimation updates.


---

*[View on Apple Developer](https://developer.apple.com/documentation/arkit/ar_environment_light_estimation_provider_set_update_handler)*