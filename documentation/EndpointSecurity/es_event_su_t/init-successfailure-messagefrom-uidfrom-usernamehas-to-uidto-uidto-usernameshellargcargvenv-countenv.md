# init(success:failure_message:from_uid:from_username:has_to_uid:to_uid:to_username:shell:argc:argv:env_count:env:)

**Framework**: Endpoint Security  
**Kind**: init

**Availability**:
- Mac Catalyst ?+
- macOS ?+

## Declaration

```swift
init(success: Bool, failure_message: es_string_token_t, from_uid: uid_t, from_username: es_string_token_t, has_to_uid: Bool, to_uid: es_event_su_t.__Unnamed_union_to_uid, to_username: es_string_token_t, shell: es_string_token_t, argc: Int, argv: UnsafeMutablePointer<es_string_token_t>?, env_count: Int, env: UnsafeMutablePointer<es_string_token_t>?)
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/endpointsecurity/es_event_su_t/init(success:failure_message:from_uid:from_username:has_to_uid:to_uid:to_username:shell:argc:argv:env_count:env:))*