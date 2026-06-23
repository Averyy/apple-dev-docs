# es_event_bootstrap_look_up_t

**Framework**: Endpoint Security  
**Kind**: struct

**Availability**:
- Mac Catalyst ?+
- macOS ?+

## Declaration

```swift
struct es_event_bootstrap_look_up_t
```

#### Overview

A process called `bootstrap_look_up()` to resolve a named service port registered with launchd. launchd returns a send right to that port; subsequent `mach_msg()` calls to it are delivered to the owner of the corresponding receive right.

```None
   Submitted by launchd on behalf of the instigator.

   Because launchd is the submitter, the enclosing message's
   `es_message_t.process` describes launchd, not the process that
   called `bootstrap_look_up()`. The actual caller is reported as
   `instigator` / `instigator_token` below.
```

```None
                    `bootstrap_look_up()`. Best-effort; may be null
                    if the instigator exited before the event was
                    constructed.
```

```None
                    launchd at RPC time. Always present.
```

```None
                    between a running owner (PROCESS) and a
                    lazy-launched owner (JOB).
```

```None
                    messages sent to the returned port if the
                    lookup is allowed.

                    On the PROCESS arm, `target` (es_process_t)
                    carries the live owner's full process info
                    including code-signing identity
                    (target->signing_id, target->team_id) sourced
                    from the kernel. No identity from launchd's
                    cached Lightweight Code Requirement (LWCR) is
                    reported on this arm — read it from the
                    es_process_t.

                    On the JOB arm there is no live process, so
                    the only available identity is the LWCR
                    launchd had configured (if any). `lwcr` is a
                    nullable pointer: NULL when no LWCR was cached
                    for this service.
```

> **Note**: This event type does not support caching.

## Topics

### Initializers
- [init()](es_event_bootstrap_look_up_t/init.md)
- [init(instigator: UnsafeMutablePointer<es_process_t>?, instigator_token: audit_token_t, service_name: es_string_token_t, target_type: es_bootstrap_target_type_t, target: es_event_bootstrap_look_up_t.__Unnamed_union_target)](es_event_bootstrap_look_up_t/init(instigator:instigator_token:service_name:target_type:target:).md)
### Instance Properties
- [var instigator: UnsafeMutablePointer<es_process_t>?](es_event_bootstrap_look_up_t/instigator.md)
- [var instigator_token: audit_token_t](es_event_bootstrap_look_up_t/instigator_token.md)
- [var service_name: es_string_token_t](es_event_bootstrap_look_up_t/service_name.md)
- [var target: es_event_bootstrap_look_up_t.__Unnamed_union_target](es_event_bootstrap_look_up_t/target.md)
- [var target_type: es_bootstrap_target_type_t](es_event_bootstrap_look_up_t/target_type.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/endpointsecurity/es_event_bootstrap_look_up_t)*