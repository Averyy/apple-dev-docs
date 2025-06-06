# ar_authorization_type_t

**Framework**: ARKit  
**Kind**: enum

The authorization types you can request from ARKit.

## Declaration

```swift
typedef enum { ... } ar_authorization_type_t;
```

## Topics

### Requesting authorization
- [ar_authorization_type_hand_tracking](ar_authorization_type_t/ar_authorization_type_hand_tracking.md)
  The authorization for access to detailed hand-tracking data.
- [ar_authorization_type_world_sensing](ar_authorization_type_t/ar_authorization_type_world_sensing.md)
  The authorization for access to plane detection, scene reconstruction, and image tracking.
- [ar_authorization_type_camera_access](ar_authorization_type_t/ar_authorization_type_camera_access.md)
  The authorization for camera access.
- [ar_authorization_type_none](ar_authorization_type_t/ar_authorization_type_none.md)
  There isn’t an authorization type.

## See Also

- [ar_authorization_status_t](ar_authorization_status_t.md)
  The authorization states for a type of ARKit data.
- [ar_authorization_result_get_authorization_type](ar_authorization_result_get_authorization_type.md)
  Gets the authorization type associated with an authorization result.
- [ar_authorization_result_get_status](ar_authorization_result_get_status.md)
  Gets the authorization status associated with an authorization result.
- [ar_authorization_results_enumerate_results](ar_authorization_results_enumerate_results.md)
  Enumerates a collection of authorization results.
- [ar_authorization_results_enumerate_results_f](ar_authorization_results_enumerate_results_f.md)
  Enumerates a collection of authorization results.
- [ar_authorization_results_get_count](ar_authorization_results_get_count.md)
  Gets the number of authorization results in a collection.
- [ar_authorization_status_allowed](ar_authorization_status_t/ar_authorization_status_allowed.md)
  Your app has permission to use the associated kind of ARKit data.
- [ar_authorization_status_denied](ar_authorization_status_t/ar_authorization_status_denied.md)
  Your app doesn’t have permission to use the associated kind of ARKit data.
- [ar_authorization_status_not_determined](ar_authorization_status_t/ar_authorization_status_not_determined.md)
  Permission for your app to use the associated kind of ARKit data is undetermined.
- [ar_authorization_result_t](ar_authorization_result_t.md)
  An authorization result.
- [ar_authorization_results_enumerator_t](ar_authorization_results_enumerator_t.md)
  A handler for enumerating a collection of authorization results.
- [ar_authorization_results_handler_t](ar_authorization_results_handler_t.md)
  A handler to call upon completion of an authorization request.
- [ar_authorization_results_t](ar_authorization_results_t.md)
  A collection of authorization results.
- [ar_authorization_update_handler_t](ar_authorization_update_handler_t.md)
  A handler for receiving updates in authorization status for a specific authorization type.
- [ar_authorization_results_handler_function_t](ar_authorization_results_handler_function_t.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/arkit/ar_authorization_type_t)*