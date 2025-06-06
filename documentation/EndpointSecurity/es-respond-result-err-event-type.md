# ES_RESPOND_RESULT_ERR_EVENT_TYPE

**Framework**: Endpoint Security  
**Kind**: var

The caller performed an inappropriate response to the event.

**Availability**:
- Mac Catalyst ?+
- macOS ?+

## Declaration

```swift
var ES_RESPOND_RESULT_ERR_EVENT_TYPE: es_respond_result_t { get }
```

#### Discussion

Authorization events require the client to respond with an appropriate result using either [`es_respond_auth_result(_:_:_:_:)`](es_respond_auth_result(_:_:_:_:).md) or [`es_respond_flags_result(_:_:_:_:)`](es_respond_flags_result(_:_:_:_:).md). This error occurs if the client attempts to respond to an authorization event using the wrong interface. It also occurs when the client performs any response to a notification-only event.

## See Also

- [var ES_RESPOND_RESULT_ERR_DUPLICATE_RESPONSE: es_respond_result_t](es_respond_result_err_duplicate_response.md)
  The caller responded to a message that already received a response.
- [var ES_RESPOND_RESULT_ERR_INTERNAL: es_respond_result_t](es_respond_result_err_internal.md)
  Communication with the Endpoint Security system failed.
- [var ES_RESPOND_RESULT_ERR_INVALID_ARGUMENT: es_respond_result_t](es_respond_result_err_invalid_argument.md)
  The caller provided one or more invalid arguments.
- [var ES_RESPOND_RESULT_NOT_FOUND: es_respond_result_t](es_respond_result_not_found.md)
  The system couldn’t find the message that the caller sent this response to.


---

*[View on Apple Developer](https://developer.apple.com/documentation/endpointsecurity/es_respond_result_err_event_type)*