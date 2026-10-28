# es_deadline_miss_mode_t

**Framework**: Endpoint Security  
**Kind**: struct  
**Role**: Structure

Deadline miss mode for ES clients

**Availability**:
- Mac Catalyst
- macOS

## Declaration

```swift
struct es_deadline_miss_mode_t
```

```c
typedef enum { ... } es_deadline_miss_mode_t;
```

## Overview

Determines how the system responds when a client fails to respond to an auth event within the deadline.

## Topics

### Initializers
- [init(UInt32)](./es_deadline_miss_mode_t/init%28_%29.md)
- [init(rawValue: UInt32)](./es_deadline_miss_mode_t/init%28rawvalue%29.md)
### Instance Properties
- [var rawValue: UInt32](./es_deadline_miss_mode_t/rawvalue.md)
### Enumeration Cases
- [ES_DEADLINE_MISS_MODE_FAIL_CLOSED](./es_deadline_miss_mode_fail_closed.md)
  Deny the operation when client fails to respond, but don’t kill the client
- [ES_DEADLINE_MISS_MODE_FAIL_OPEN](./es_deadline_miss_mode_fail_open.md)
  Allow the operation when client fails to respond, but don’t kill the client
- [ES_DEADLINE_MISS_MODE_KILL](./es_deadline_miss_mode_kill.md)
  Kill the client when it fails to respond to an auth event (default behavior)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/bitwisecopyable.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [RawRepresentable](../Swift/rawrepresentable.md)
- [Sendable](../Swift/sendable.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/endpointsecurity/es_deadline_miss_mode_t)*