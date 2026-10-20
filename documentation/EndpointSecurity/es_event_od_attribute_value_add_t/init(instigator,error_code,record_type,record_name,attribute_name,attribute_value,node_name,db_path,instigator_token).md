# init(instigator:error_code:record_type:record_name:attribute_name:attribute_value:node_name:db_path:instigator_token:)

**Framework**: Endpoint Security  
**Kind**: init

**Availability**:
- Mac Catalyst ?+
- macOS ?+

## Declaration

```swift
init(instigator: UnsafeMutablePointer<es_process_t>?, error_code: Int32, record_type: es_od_record_type_t, record_name: es_string_token_t, attribute_name: es_string_token_t, attribute_value: es_string_token_t, node_name: es_string_token_t, db_path: es_string_token_t, instigator_token: audit_token_t)
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/endpointsecurity/es_event_od_attribute_value_add_t/init(instigator:error_code:record_type:record_name:attribute_name:attribute_value:node_name:db_path:instigator_token:))*