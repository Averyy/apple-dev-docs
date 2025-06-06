# init(instigator:app:item:executable_path:instigator_token:app_token:)

**Framework**: Endpoint Security  
**Kind**: init

**Availability**:
- Mac Catalyst ?+
- macOS ?+

## Declaration

```swift
init(instigator: UnsafeMutablePointer<es_process_t>?, app: UnsafeMutablePointer<es_process_t>?, item: UnsafeMutablePointer<es_btm_launch_item_t>, executable_path: es_string_token_t, instigator_token: UnsafeMutablePointer<audit_token_t>?, app_token: UnsafeMutablePointer<audit_token_t>?)
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/endpointsecurity/es_event_btm_launch_item_add_t/init(instigator:app:item:executable_path:instigator_token:app_token:))*