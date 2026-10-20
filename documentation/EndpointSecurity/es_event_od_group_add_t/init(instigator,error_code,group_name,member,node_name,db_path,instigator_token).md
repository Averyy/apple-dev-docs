# init(instigator:error_code:group_name:member:node_name:db_path:instigator_token:)

**Framework**: Endpoint Security  
**Kind**: init

**Availability**:
- Mac Catalyst ?+
- macOS ?+

## Declaration

```swift
init(instigator: UnsafeMutablePointer<es_process_t>?, error_code: Int32, group_name: es_string_token_t, member: UnsafeMutablePointer<es_od_member_id_t>, node_name: es_string_token_t, db_path: es_string_token_t, instigator_token: audit_token_t)
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/endpointsecurity/es_event_od_group_add_t/init(instigator:error_code:group_name:member:node_name:db_path:instigator_token:))*