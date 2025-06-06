# init(success:reject_info:has_from_uid:from_uid:from_username:has_to_uid:to_uid:to_username:command:)

**Framework**: Endpoint Security  
**Kind**: init

**Availability**:
- Mac Catalyst ?+
- macOS ?+

## Declaration

```swift
init(success: Bool, reject_info: UnsafeMutablePointer<es_sudo_reject_info_t>?, has_from_uid: Bool, from_uid: es_event_sudo_t.__Unnamed_union_from_uid, from_username: es_string_token_t, has_to_uid: Bool, to_uid: es_event_sudo_t.__Unnamed_union_to_uid, to_username: es_string_token_t, command: es_string_token_t)
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/endpointsecurity/es_event_sudo_t/init(success:reject_info:has_from_uid:from_uid:from_username:has_to_uid:to_uid:to_username:command:))*