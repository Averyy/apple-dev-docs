---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlx/wiredmemoryticket"
framework: "mlx-swift/MLX"
---

# WiredMemoryTicket

**Framework**: mlx-swift/MLX  
**Kind**: struct  
**Role**: Structure

Handle for coordinating wired memory changes across concurrent work.

## Declaration

```swift
struct WiredMemoryTicket
```

## Mentions

- [Wired Memory Management](./wired-memory.md)

#### Overview

A ticket represents a single unit of memory demand. Tickets are started and ended explicitly and are safe to start/end multiple times (extra calls are ignored). Use `withWiredLimit` to ensure cancellation-safe pairing.

## Topics

### Initializers
- [init(id: UUID, size: Int, policy: any WiredMemoryPolicy, manager: WiredMemoryManager, kind: WiredMemoryTicketKind)](./wiredmemoryticket/init%28id,size,policy,manager,kind%29.md)
  Creates a ticket bound to a policy and manager.
### Instance Properties
- [let id: UUID](./wiredmemoryticket/id.md)
  Unique identifier for this ticket.
- [let kind: WiredMemoryTicketKind](./wiredmemoryticket/kind.md)
  Whether this ticket represents active work or a reservation.
- [let manager: WiredMemoryManager](./wiredmemoryticket/manager.md)
  Manager responsible for coordinating the ticket.
- [let policy: any WiredMemoryPolicy](./wiredmemoryticket/policy.md)
  Policy that controls admission and limit computation.
- [let size: Int](./wiredmemoryticket/size.md)
  Requested size in bytes.
### Instance Methods
- [func end() async -> Int](./wiredmemoryticket/end%28%29.md)
  Ends the ticket and returns the applied limit.
- [func start() async -> Int](./wiredmemoryticket/start%28%29.md)
  Starts the ticket and returns the applied limit.
- [func withWiredLimit<R>(() async throws -> R) async rethrows -> R](./wiredmemoryticket/withwiredlimit%28_%29.md)
  Convenience overload for using an instance directly.
### Type Methods
- [static func withWiredLimit<R>(WiredMemoryTicket, () async throws -> R) async rethrows -> R](./wiredmemoryticket/withwiredlimit%28_,_%29.md)
  Keeps the ticket active until the body returns or throws, including during cancellation.

## Relationships

### Conforms To
- Swift.Identifiable
- Swift.Sendable
- Swift.SendableMetatype

## See Also

### Memory
- [enum GPU](./gpu.md)
  API for controlling GPU related features.
- [actor WiredMemoryManager](./wiredmemorymanager.md)
  Central coordinator for process-wide wired memory limits.
- [protocol WiredMemoryPolicy](./wiredmemorypolicy.md)
  Policy for computing a process-global wired memory limit.
- [struct WiredMemoryEvent](./wiredmemoryevent.md)
  Debug event emitted by [`WiredMemoryManager`](./wiredmemorymanager.md) when coordinating wired memory changes.


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlx/wiredmemoryticket)*