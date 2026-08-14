# es_event_bootstrap_check_in_t

**Framework**: Endpoint Security  
**Kind**: struct

**Availability**:
- Mac Catalyst ?+
- macOS ?+

## Declaration

```swift
struct es_event_bootstrap_check_in_t
```

#### Overview

A process called `bootstrap_check_in()` to register a named service port with launchd. Subsequent `bootstrap_look_up()` calls from other processes will resolve the registered name into a send right to this port.

```None
   Submitted by launchd on behalf of the instigator.

   Because launchd is the submitter, the enclosing message's
   `es_message_t.process` describes launchd, not the process that
   called `bootstrap_check_in()`. The actual caller is reported as
   `instigator` / `instigator_token` below.
```

```None
                    `bootstrap_check_in()`. Best-effort; may be null if
                    the instigator exited before the event was
                    constructed.
```

```None
                    at RPC time. Always present.
```

> **Note**: This event type does not support caching.

## Topics

### Initializers
- [init()](es_event_bootstrap_check_in_t/init.md)
- [init(instigator: UnsafeMutablePointer<es_process_t>?, instigator_token: audit_token_t, service_name: es_string_token_t)](es_event_bootstrap_check_in_t/init(instigator:instigator_token:service_name:).md)
### Instance Properties
- [var instigator: UnsafeMutablePointer<es_process_t>?](es_event_bootstrap_check_in_t/instigator.md)
- [var instigator_token: audit_token_t](es_event_bootstrap_check_in_t/instigator_token.md)
- [var service_name: es_string_token_t](es_event_bootstrap_check_in_t/service_name.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../swift/bitwisecopyable.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/endpointsecurity/es_event_bootstrap_check_in_t)*