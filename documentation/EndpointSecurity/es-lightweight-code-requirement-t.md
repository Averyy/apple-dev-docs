# es_lightweight_code_requirement_t

**Framework**: Endpoint Security  
**Kind**: struct

**Availability**:
- Mac Catalyst ?+
- macOS ?+

## Declaration

```swift
struct es_lightweight_code_requirement_t
```

#### Overview

Identity facts cached from a service’s Lightweight Code Requirement (LWCR) — the code-signing constraint launchd was told to enforce when the service binary spawns.

Used as a nullable pointer on the JOB arm of `es_event_bootstrap_look_up_t.target`: NULL means launchd had no LWCR cached for this service, distinct from “LWCR was present but carried no team_id / signing_id” (which would be a non-NULL pointer with the corresponding string token’s `data` field set to NULL).

The PROCESS arm omits this struct entirely — the receiving process’s actual code-signing identity is available via `target.process.target->signing_id` / `->team_id` (kernel-sourced from cs_ops on the audit token).

Both string token fields preserve the three-state distinction common to optional ES strings: `data == NULL` (the LWCR did not carry this fact), `data != NULL && length == 0` (carried an empty value), and `data != NULL && length > 0` (carried a value).

```None
               is NULL when the LWCR did not carry this fact.
```

```None
               `data` is NULL when the LWCR did not carry this
               fact.
```

## Topics

### Initializers
- [init()](es_lightweight_code_requirement_t/init.md)
- [init(team_id: es_string_token_t, signing_id: es_string_token_t)](es_lightweight_code_requirement_t/init(team_id:signing_id:).md)
### Instance Properties
- [var signing_id: es_string_token_t](es_lightweight_code_requirement_t/signing_id.md)
- [var team_id: es_string_token_t](es_lightweight_code_requirement_t/team_id.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../swift/bitwisecopyable.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/endpointsecurity/es_lightweight_code_requirement_t)*