# ar_session_request_authorization

**Framework**: ARKit  
**Kind**: func

Requests authorization from the user to use the specified kinds of ARKit data.

**Availability**:
- visionOS 1.0+

## Declaration

```swift
extern void ar_session_request_authorization(ar_session_t session, ar_authorization_type_t authorization_types, ar_authorization_results_handler_tresults_handler);
```

## See Also

- [ar_session_t](ar_session_t.md)
  The main entry point for receiving data from ARKit.
- [ar_session_create](ar_session_create.md)
  Creates a new session.
- [ar_session_query_authorization_results](ar_session_query_authorization_results.md)
  Checks whether the current session is authorized for particular authorization types without requesting authorization.
- [ar_session_query_authorization_results_f](ar_session_query_authorization_results_f.md)
  Checks whether the current session is authorized for particular authorization types without requesting authorization.
- [ar_session_request_authorization_f](ar_session_request_authorization_f.md)
  Requests authorization from the user to use the specified kinds of ARKit data.
- [ar_session_run](ar_session_run.md)
  Runs a session with the data providers you supply.
- [ar_session_set_authorization_update_handler](ar_session_set_authorization_update_handler.md)
  Sets the handler for receiving updates in authorization status for a specific authorization type.
- [ar_session_set_authorization_update_handler_f](ar_session_set_authorization_update_handler_f.md)
  Sets the handler for receiving updates in authorization status for a specific authorization type.
- [ar_session_set_data_provider_state_change_handler](ar_session_set_data_provider_state_change_handler.md)
  Sets the handler for responding to a change in the state of one or more data providers.
- [ar_session_set_data_provider_state_change_handler_f](ar_session_set_data_provider_state_change_handler_f.md)
  Sets the handler for responding to a change in the state of one or more data providers.
- [ar_session_data_provider_state_change_handler_t](ar_session_data_provider_state_change_handler_t.md)
  A handler for receiving updates to data provider states.
- [ar_session_stop](ar_session_stop.md)
  Stops a session.


---

*[View on Apple Developer](https://developer.apple.com/documentation/arkit/ar_session_request_authorization)*