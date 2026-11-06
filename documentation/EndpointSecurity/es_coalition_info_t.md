# es_coalition_info_t

**Framework**: Endpoint Security  
**Kind**: struct  
**Role**: Structure

**Availability**:
- Mac Catalyst
- macOS

## Declaration

```swift
struct es_coalition_info_t
```

```c
typedef struct { ... } es_coalition_info_t;
```

## Overview

The coalition identity of a process.

```
   jetsam coalition.
```

Coalitions are described in mach/coalition.h.  A resource coalition groups processes for resource accounting; a jetsam coalition groups a leader (typically an application) with the XPC services and extensions launched on its behalf, for memory-pressure and lifecycle decisions.

## Topics

### Initializers
- [init()](./es_coalition_info_t/init%28%29.md)
- [init(resource_id: UInt64, jetsam: UnsafeMutablePointer<es_coalition_jetsam_t>?)](./es_coalition_info_t/init%28resource_id,jetsam%29.md)
### Instance Properties
- [var jetsam: UnsafeMutablePointer<es_coalition_jetsam_t>?](./es_coalition_info_t/jetsam.md)
- [var resource_id: UInt64](./es_coalition_info_t/resource_id.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/bitwisecopyable.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/endpointsecurity/es_coalition_info_t)*