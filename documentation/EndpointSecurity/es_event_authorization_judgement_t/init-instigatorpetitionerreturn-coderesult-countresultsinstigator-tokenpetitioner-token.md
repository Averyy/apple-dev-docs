# init(instigator:petitioner:return_code:result_count:results:instigator_token:petitioner_token:)

**Framework**: Endpoint Security  
**Kind**: init

**Availability**:
- Mac Catalyst ?+
- macOS ?+

## Declaration

```swift
init(instigator: UnsafeMutablePointer<es_process_t>?, petitioner: UnsafeMutablePointer<es_process_t>?, return_code: Int32, result_count: Int, results: UnsafeMutablePointer<es_authorization_result_t>?, instigator_token: audit_token_t, petitioner_token: audit_token_t)
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/endpointsecurity/es_event_authorization_judgement_t/init(instigator:petitioner:return_code:result_count:results:instigator_token:petitioner_token:))*