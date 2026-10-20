# parent_audit_token

**Framework**: Endpoint Security  
**Kind**: property  
**Role**: Instance Property

The audit token of the parent process.

**Availability**:
- Mac Catalyst
- macOS

## Declaration

```swift
var parent_audit_token: audit_token_t
```

```c
audit_token_t parent_audit_token;
```

#### Discussion

This field is only available if the message [`version`](../es_message_t/version.md) is `4` or greater.

## See Also

### Inspecting Audit Tokens
- [var responsible_audit_token: audit_token_t](./responsible_audit_token.md)
  The audit token of the process responsible for this process.


---

*[View on Apple Developer](https://developer.apple.com/documentation/endpointsecurity/es_process_t/parent_audit_token)*