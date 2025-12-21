# ar_session_set_authorization_update_handler_f

**Framework**: ARKit  
**Kind**: func

Sets the handler for receiving updates in authorization status for a specific authorization type.

**Availability**:
- visionOS 1.0+

## Declaration

```swift
extern void ar_session_set_authorization_update_handler_f(ar_session_t session, dispatch_queue_t authorization_update_queue, void * context, ar_authorization_update_handler_function_t authorization_update_handler_function);
```

## See Also

- [ar_session_t](ar_session_t.md)
  The main entry point for receiving data from ARKit.
- [ar_session_create](ar_session_create.md)
  Creates a new session.
- [ar_session_create_with_device](ar_session_create_with_device.md)
  Create a session connected to the specified device.
- [ar_session_query_authorization_results](ar_session_query_authorization_results.md)
  Checks whether the current session is authorized for particular authorization types without requesting authorization.
- [ar_session_query_authorization_results_f](ar_session_query_authorization_results_f.md)
  Checks whether the current session is authorized for particular authorization types without requesting authorization.
- [ar_session_request_authorization](ar_session_request_authorization.md)
  Requests authorization from the user to use the specified kinds of ARKit data.
- [ar_session_request_authorization_f](ar_session_request_authorization_f.md)
  Requests authorization from the user to use the specified kinds of ARKit data.
- [ar_session_run](ar_session_run.md)
  Runs a session with the data providers you supply.
- [ar_session_set_authorization_update_handler](ar_session_set_authorization_update_handler.md)
  Sets the handler for receiving updates in authorization status for a specific authorization type.
- [ar_session_copy_data_providers](ar_session_copy_data_providers.md)
  Get a copy of the collection of all data providers on this session.
- [ar_session_set_data_provider_state_change_handler](ar_session_set_data_provider_state_change_handler.md)
  Sets the handler for responding to a state change of one or more data providers.
- [ar_session_set_data_provider_state_change_handler_f](ar_session_set_data_provider_state_change_handler_f.md)
  Sets the handler function for responding to a state change of one or more data providers.
- [ar_session_data_provider_state_change_handler_t](ar_session_data_provider_state_change_handler_t.md)
  A handler that the session calls when one or more data providers associated with it change state.
- [ar_session_stop](ar_session_stop.md)
  Stops a session.
- [typealias ar_device_t](ar_device_t.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/arkit/ar_session_set_authorization_update_handler_f)*