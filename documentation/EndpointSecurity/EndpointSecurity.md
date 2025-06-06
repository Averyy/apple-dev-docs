# Endpoint Security

**Framework**: Endpoint Security  
**Kind**: module

Develop system extensions that enhance user security.

**Availability**:
- Mac Catalyst 13.0+
- macOS 10.15+

#### Overview

Endpoint Security is a C API for monitoring system events for potentially malicious activity. You can write your client in any language that supports native calls. Your client registers with Endpoint Security to authorize pending events, or receive notifications of events that already occurred. These events include process executions, mounting file systems, forking processes, and raising signals.

Develop your system extension with Endpoint Security and package it in an app that uses the [`System Extensions`](https://developer.apple.com/documentation/SystemExtensions) framework to install and upgrade the extension on the user’s Mac.

## Topics

### Event Monitoring
- [Client](client.md)
  An opaque type that maintains Endpoint Security client state, and functions related to this type.
- [Message](message.md)
  A type used by Endpoint Security to notify your client when a monitored action occurs.
- [Event Types](event-types.md)
  Types used by messages to deliver details specific to different kinds of Endpoint Security events.
- [Monitoring System Events with Endpoint Security](monitoring-system-events-with-endpoint-security.md)
  Receive notifications and authorization requests for sensitive operations by creating an Endpoint Security client for your app.
### Entitlements
- [com.apple.developer.endpoint-security.client](../BundleResources/Entitlements/com.apple.developer.endpoint-security.client.md)
  The entitlement required to monitor system events for potentially malicious activity.
### Reference
- [EndpointSecurity Constants](endpointsecurity-constants.md)
- [EndpointSecurity Data Types](endpointsecurity-data-types.md)
- [EndpointSecurity Functions](endpointsecurity-functions.md)
- [EndpointSecurity Structures](endpointsecurity-structures.md)
- [EndpointSecurity Enumerations](endpointsecurity-enumerations.md)
### Structures
- [struct es_event_tcc_modify_t](es_event_tcc_modify_t.md)
- [struct es_tcc_authorization_reason_t](es_tcc_authorization_reason_t.md)
  ess_tcc_authorization_reason_t
- [struct es_tcc_authorization_right_t](es_tcc_authorization_right_t.md)
  ess_tcc_authorization_right_t
- [struct es_tcc_event_type_t](es_tcc_event_type_t.md)
- [struct es_tcc_identity_type_t](es_tcc_identity_type_t.md)
  es_tcc_identity_type_t
### Variables
- [var ES_EVENT_TYPE_NOTIFY_TCC_MODIFY: es_event_type_t](es_event_type_notify_tcc_modify.md)
- [var ES_TCC_AUTHORIZATION_REASON_APP_TYPE_POLICY: es_tcc_authorization_reason_t](es_tcc_authorization_reason_app_type_policy.md)
  A system process changed the authorization right
- [var ES_TCC_AUTHORIZATION_REASON_ENTITLED: es_tcc_authorization_reason_t](es_tcc_authorization_reason_entitled.md)
  A system process changed the authorization right
- [var ES_TCC_AUTHORIZATION_REASON_ERROR: es_tcc_authorization_reason_t](es_tcc_authorization_reason_error.md)
- [var ES_TCC_AUTHORIZATION_REASON_MDM_POLICY: es_tcc_authorization_reason_t](es_tcc_authorization_reason_mdm_policy.md)
  A system process changed the authorization right
- [var ES_TCC_AUTHORIZATION_REASON_MISSING_USAGE_STRING: es_tcc_authorization_reason_t](es_tcc_authorization_reason_missing_usage_string.md)
  A system process changed the authorization right
- [var ES_TCC_AUTHORIZATION_REASON_NONE: es_tcc_authorization_reason_t](es_tcc_authorization_reason_none.md)
- [var ES_TCC_AUTHORIZATION_REASON_PREFLIGHT_UNKNOWN: es_tcc_authorization_reason_t](es_tcc_authorization_reason_preflight_unknown.md)
  A system process changed the authorization right
- [var ES_TCC_AUTHORIZATION_REASON_PROMPT_CANCEL: es_tcc_authorization_reason_t](es_tcc_authorization_reason_prompt_cancel.md)
  A system process changed the authorization right
- [var ES_TCC_AUTHORIZATION_REASON_PROMPT_TIMEOUT: es_tcc_authorization_reason_t](es_tcc_authorization_reason_prompt_timeout.md)
  A system process changed the authorization right
- [var ES_TCC_AUTHORIZATION_REASON_SERVICE_OVERRIDE_POLICY: es_tcc_authorization_reason_t](es_tcc_authorization_reason_service_override_policy.md)
  A system process changed the authorization right
- [var ES_TCC_AUTHORIZATION_REASON_SERVICE_POLICY: es_tcc_authorization_reason_t](es_tcc_authorization_reason_service_policy.md)
  A system process changed the authorization right
- [var ES_TCC_AUTHORIZATION_REASON_SYSTEM_SET: es_tcc_authorization_reason_t](es_tcc_authorization_reason_system_set.md)
  User changed the authorization right via Preferences
- [var ES_TCC_AUTHORIZATION_REASON_USER_CONSENT: es_tcc_authorization_reason_t](es_tcc_authorization_reason_user_consent.md)
- [var ES_TCC_AUTHORIZATION_REASON_USER_SET: es_tcc_authorization_reason_t](es_tcc_authorization_reason_user_set.md)
  User answered a prompt
- [var ES_TCC_AUTHORIZATION_RIGHT_ADD_MODIFY_ADDED: es_tcc_authorization_right_t](es_tcc_authorization_right_add_modify_added.md)
- [var ES_TCC_AUTHORIZATION_RIGHT_ALLOWED: es_tcc_authorization_right_t](es_tcc_authorization_right_allowed.md)
- [var ES_TCC_AUTHORIZATION_RIGHT_DENIED: es_tcc_authorization_right_t](es_tcc_authorization_right_denied.md)
- [var ES_TCC_AUTHORIZATION_RIGHT_LEARN_MORE: es_tcc_authorization_right_t](es_tcc_authorization_right_learn_more.md)
- [var ES_TCC_AUTHORIZATION_RIGHT_LIMITED: es_tcc_authorization_right_t](es_tcc_authorization_right_limited.md)
- [var ES_TCC_AUTHORIZATION_RIGHT_SESSION_PID: es_tcc_authorization_right_t](es_tcc_authorization_right_session_pid.md)
- [var ES_TCC_AUTHORIZATION_RIGHT_UNKNOWN: es_tcc_authorization_right_t](es_tcc_authorization_right_unknown.md)
- [var ES_TCC_EVENT_TYPE_CREATE: es_tcc_event_type_t](es_tcc_event_type_create.md)
- [var ES_TCC_EVENT_TYPE_DELETE: es_tcc_event_type_t](es_tcc_event_type_delete.md)
- [var ES_TCC_EVENT_TYPE_MODIFY: es_tcc_event_type_t](es_tcc_event_type_modify.md)
- [var ES_TCC_EVENT_TYPE_UNKNOWN: es_tcc_event_type_t](es_tcc_event_type_unknown.md)
- [var ES_TCC_IDENTITY_TYPE_BUNDLE_ID: es_tcc_identity_type_t](es_tcc_identity_type_bundle_id.md)
- [var ES_TCC_IDENTITY_TYPE_EXECUTABLE_PATH: es_tcc_identity_type_t](es_tcc_identity_type_executable_path.md)
- [var ES_TCC_IDENTITY_TYPE_FILE_PROVIDER_DOMAIN_ID: es_tcc_identity_type_t](es_tcc_identity_type_file_provider_domain_id.md)
- [var ES_TCC_IDENTITY_TYPE_POLICY_ID: es_tcc_identity_type_t](es_tcc_identity_type_policy_id.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/EndpointSecurity)*