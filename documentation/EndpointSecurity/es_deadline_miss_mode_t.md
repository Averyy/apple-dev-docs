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

#### Overview

Determines how the system responds when a client fails to respond to an auth event within the deadline.

## Topics

### Initializers
- [init(UInt32)](./es_deadline_miss_mode_t/init%28_%29.md)
- [init(rawValue: UInt32)](./es_deadline_miss_mode_t/init%28rawvalue%29.md)
### Instance Properties
- [var rawValue: UInt32](./es_deadline_miss_mode_t/rawvalue.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/bitwisecopyable.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [RawRepresentable](../Swift/rawrepresentable.md)
- [Sendable](../Swift/sendable.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/endpointsecurity/es_deadline_miss_mode_t)*