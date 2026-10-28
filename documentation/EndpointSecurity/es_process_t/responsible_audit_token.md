# responsible_audit_token

**Framework**: Endpoint Security  
**Kind**: property  
**Role**: Instance Property

The audit token of the process responsible for this process.

**Availability**:
- Mac Catalyst
- macOS

## Declaration

```swift
var responsible_audit_token: audit_token_t
```

```c
audit_token_t responsible_audit_token;
```

## Discussion

The responsible process may be this process itself, if there’s no responsible process or the responsible process already exited.

This field is only available if the message [`version`](../es_message_t/version.md) is `4` or greater.

## See Also

### Inspecting Audit Tokens
- [var parent_audit_token: audit_token_t](./parent_audit_token.md)
  The audit token of the parent process.


---

*[View on Apple Developer](https://developer.apple.com/documentation/endpointsecurity/es_process_t/responsible_audit_token)*