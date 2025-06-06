# init(instigator:petitioner:flags:right_count:rights:instigator_token:petitioner_token:)

**Framework**: Endpoint Security  
**Kind**: init

**Availability**:
- Mac Catalyst ?+
- macOS ?+

## Declaration

```swift
init(instigator: UnsafeMutablePointer<es_process_t>?, petitioner: UnsafeMutablePointer<es_process_t>?, flags: UInt32, right_count: Int, rights: UnsafeMutablePointer<es_string_token_t>?, instigator_token: audit_token_t, petitioner_token: audit_token_t)
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/endpointsecurity/es_event_authorization_petition_t/init(instigator:petitioner:flags:right_count:rights:instigator_token:petitioner_token:))*