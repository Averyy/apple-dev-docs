# init(audit_token:ppid:original_ppid:group_id:session_id:codesigning_flags:is_platform_binary:is_es_client:cdhash:signing_id:team_id:executable:tty:start_time:responsible_audit_token:parent_audit_token:cs_validation_category:)

**Framework**: Endpoint Security  
**Kind**: init

**Availability**:
- Mac Catalyst ?+
- macOS ?+

## Declaration

```swift
init(audit_token: audit_token_t, ppid: pid_t, original_ppid: pid_t, group_id: pid_t, session_id: pid_t, codesigning_flags: UInt32, is_platform_binary: Bool, is_es_client: Bool, cdhash: es_cdhash_t, signing_id: es_string_token_t, team_id: es_string_token_t, executable: UnsafeMutablePointer<es_file_t>, tty: UnsafeMutablePointer<es_file_t>?, start_time: timeval, responsible_audit_token: audit_token_t, parent_audit_token: audit_token_t, cs_validation_category: es_cs_validation_category_t)
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/endpointsecurity/es_process_t/init(audit_token:ppid:original_ppid:group_id:session_id:codesigning_flags:is_platform_binary:is_es_client:cdhash:signing_id:team_id:executable:tty:start_time:responsible_audit_token:parent_audit_token:cs_validation_category:))*