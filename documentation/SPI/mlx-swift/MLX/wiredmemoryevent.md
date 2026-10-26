---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlx/wiredmemoryevent"
framework: "mlx-swift/MLX"
---

# WiredMemoryEvent

**Framework**: mlx-swift/MLX  
**Kind**: struct  
**Role**: Structure

Debug event emitted by [`WiredMemoryManager`](./wiredmemorymanager.md) when coordinating wired memory changes.

## Declaration

```swift
struct WiredMemoryEvent
```

## Mentions

- [Wired Memory Management](./wired-memory.md)

#### Overview

Events are only emitted in DEBUG builds. In release builds the event stream is empty and finishes immediately.

## Topics

### Initializers
- [init(sequence: UInt64, timestamp: Date, kind: WiredMemoryEvent.Kind, ticketID: UUID?, size: Int?, policy: String?, baseline: Int?, desiredLimit: Int?, appliedLimit: Int?, activeCount: Int, waiterCount: Int)](./wiredmemoryevent/init%28sequence,timestamp,kind,ticketid,size,policy,baseline,desiredlimit,appliedlimit,activecount,waitercount%29.md)
### Instance Properties
- [let activeCount: Int](./wiredmemoryevent/activecount.md)
  Number of active tickets at time of emission.
- [let appliedLimit: Int?](./wiredmemoryevent/appliedlimit.md)
  Limit that was actually applied (or attempted).
- [let baseline: Int?](./wiredmemoryevent/baseline.md)
  Baseline wired limit captured before the manager applies any changes.
- [let desiredLimit: Int?](./wiredmemoryevent/desiredlimit.md)
  Desired limit computed by policy aggregation.
- [let kind: WiredMemoryEvent.Kind](./wiredmemoryevent/kind-swift.property.md)
  Event type.
- [let policy: String?](./wiredmemoryevent/policy.md)
  Debug label for the policy group, if applicable.
- [let sequence: UInt64](./wiredmemoryevent/sequence.md)
  Monotonic sequence number assigned by the manager.
- [let size: Int?](./wiredmemoryevent/size.md)
  Ticket size in bytes, if applicable.
- [let ticketID: UUID?](./wiredmemoryevent/ticketid.md)
  Ticket identifier, if the event is associated with a specific ticket.
- [let timestamp: Date](./wiredmemoryevent/timestamp.md)
  Timestamp when the event was emitted.
- [let waiterCount: Int](./wiredmemoryevent/waitercount.md)
  Number of admission waiters at time of emission.
### Enumerations
- [WiredMemoryEvent.Kind](./wiredmemoryevent/kind-swift.enum.md)

## Relationships

### Conforms To
- Swift.Sendable
- Swift.SendableMetatype

## See Also

### Memory
- [enum GPU](./gpu.md)
  API for controlling GPU related features.
- [actor WiredMemoryManager](./wiredmemorymanager.md)
  Central coordinator for process-wide wired memory limits.
- [struct WiredMemoryTicket](./wiredmemoryticket.md)
  Handle for coordinating wired memory changes across concurrent work.
- [protocol WiredMemoryPolicy](./wiredmemorypolicy.md)
  Policy for computing a process-global wired memory limit.


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlx/wiredmemoryevent)*