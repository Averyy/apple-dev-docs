# NETWORK_ERROR

**Framework**: CloudKit JS  
**Kind**: var

A network error occurred, such as a connection time out.

**Availability**:
- CloudKit JS 1.0+

## Declaration

```
const String NETWORK_ERROR;
```

## See Also

### Constants
- [ACCESS_DENIED](./access_denied.md)
  You don’t have permission to access the endpoint, record, zone, or database.
- [ATOMIC_ERROR](./atomic_error.md)
  An atomic batch operation failed.
- [AUTH_PERSIST_ERROR](./auth_persist_error.md)
- [AUTHENTICATION_FAILED](./authentication_failed.md)
  Authentication was rejected.
- [AUTHENTICATION_REQUIRED](./authentication_required.md)
  The request requires authentication but none was provided.
- [BAD_REQUEST](./bad_request.md)
  The request was not valid.
- [CONFIGURATION_ERROR](./configuration_error.md)
  CloudKit JS configuration error. For example, no containers are configured.
- [CONFLICT](./conflict.md)
  The `recordChangeTag` value expired. (Retry the request with the latest tag.)
- [EXISTS](./exists.md)
  The resource that you attempted to create already exists.
- [INTERNAL_ERROR](./internal_error.md)
  An internal error occurred.
- [INVALID_ARGUMENTS](./invalid_arguments.md)
  The parameters you provided for this method are invalid.
- [NOT_FOUND](./not_found.md)
  The resource was not found.
- [QUOTA_EXCEEDED](./quota_exceeded.md)
  If accessing the public database, you  exceeded the app’s quota. If accessing the private database, you exceeded the user’s iCloud quota.
- [SERVICE_UNAVAILABLE](./service_unavailable.md)
  The CloudKit service could not be reached.
- [SHARE_UI_TIMEOUT](./share_ui_timeout.md)
  The share UI failed to load and timed out.


---

*[View on Apple Developer](https://developer.apple.com/documentation/cloudkitjs/cloudkit.ckerror/network_error)*