# Errors

**Framework**: CloudKit JS

The errors that may occur when posting requests.

## Topics

### Constants
- [ACCESS_DENIED](cloudkit.ckerror/access_denied.md)
  You don’t have permission to access the endpoint, record, zone, or database.
- [ATOMIC_ERROR](cloudkit.ckerror/atomic_error.md)
  An atomic batch operation failed.
- [AUTH_PERSIST_ERROR](cloudkit.ckerror/auth_persist_error.md)
- [AUTHENTICATION_FAILED](cloudkit.ckerror/authentication_failed.md)
  Authentication was rejected.
- [AUTHENTICATION_REQUIRED](cloudkit.ckerror/authentication_required.md)
  The request requires authentication but none was provided.
- [BAD_REQUEST](cloudkit.ckerror/bad_request.md)
  The request was not valid.
- [CONFIGURATION_ERROR](cloudkit.ckerror/configuration_error.md)
  CloudKit JS configuration error. For example, no containers are configured.
- [CONFLICT](cloudkit.ckerror/conflict.md)
  The `recordChangeTag` value expired. (Retry the request with the latest tag.)
- [EXISTS](cloudkit.ckerror/exists.md)
  The resource that you attempted to create already exists.
- [INTERNAL_ERROR](cloudkit.ckerror/internal_error.md)
  An internal error occurred.
- [INVALID_ARGUMENTS](cloudkit.ckerror/invalid_arguments.md)
  The parameters you provided for this method are invalid.
- [NETWORK_ERROR](cloudkit.ckerror/network_error.md)
  A network error occurred, such as a connection time out.
- [NOT_FOUND](cloudkit.ckerror/not_found.md)
  The resource was not found.
- [QUOTA_EXCEEDED](cloudkit.ckerror/quota_exceeded.md)
  If accessing the public database, you  exceeded the app’s quota. If accessing the private database, you exceeded the user’s iCloud quota.
- [SERVICE_UNAVAILABLE](cloudkit.ckerror/service_unavailable.md)
  The CloudKit service could not be reached.
- [SHARE_UI_TIMEOUT](cloudkit.ckerror/share_ui_timeout.md)
  The share UI failed to load and timed out.
- [SIGN_IN_FAILED](cloudkit.ckerror/sign_in_failed.md)
  The user failed to sign in.
- [THROTTLED](cloudkit.ckerror/throttled.md)
  The request was throttled. Try the request again later.
- [TRY_AGAIN_LATER](cloudkit.ckerror/try_again_later.md)
  An internal error occurred. Try the request again.
- [UNEXPECTED_SERVER_RESPONSE](cloudkit.ckerror/unexpected_server_response.md)
  CloudKit JS was not able to decode the server response.
- [UNIQUE_FIELD_ERROR](cloudkit.ckerror/unique_field_error.md)
  The server rejected the request because there was a conflict with a unique field.
- [UNKNOWN_ERROR](cloudkit.ckerror/unknown_error.md)
  An unknown error occurred. For example, if the server returns an error that is not recognized by the version of CloudKit JS you are using.
- [VALIDATING_REFERENCE_ERROR](cloudkit.ckerror/validating_reference_error.md)
  The request violates a validating reference constraint.
- [ZONE_NOT_FOUND](cloudkit.ckerror/zone_not_found.md)
  The zone specified in the request was not found.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cloudkitjs/errors)*