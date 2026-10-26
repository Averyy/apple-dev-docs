---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlx/wiredmemorymanager"
framework: "mlx-swift/MLX"
---

# WiredMemoryManager

**Framework**: mlx-swift/MLX  
**Kind**: class  
**Role**: Class

Central coordinator for process-wide wired memory limits.

## Declaration

```swift
actor WiredMemoryManager
```

## Mentions

- [Wired Memory Management](./wired-memory.md)

#### Overview

The wired limit is a global resource. This manager serializes updates, performs admission control, and restores the baseline when work completes. Use the shared singleton in production; multiple managers are undefined.

## Topics

### Instance Methods
- [func end(id: UUID, policy: any WiredMemoryPolicy) -> Int](./wiredmemorymanager/end%28id,policy%29.md)
  Releases a ticket and recomputes the limit.
- [func events() -> AsyncStream<WiredMemoryEvent>](./wiredmemorymanager/events%28%29.md)
  Debug-only event stream describing admission and limit changes.
- [func start(id: UUID, size: Int, policy: any WiredMemoryPolicy, kind: WiredMemoryTicketKind) async -> Int](./wiredmemorymanager/start%28id,size,policy,kind%29.md)
  Main entry point for ticket admission.
- [func updateConfiguration((inout WiredMemoryManagerConfiguration) -> Void)](./wiredmemorymanager/updateconfiguration%28_%29.md)
  Update configuration when no tickets or waiters are active.
### Type Properties
- [static let shared: WiredMemoryManager](./wiredmemorymanager/shared.md)
  Shared singleton used by default for tickets.
### Type Methods
- [static func configureShared(WiredMemoryManagerConfiguration) async](./wiredmemorymanager/configureshared%28_%29.md)
  Replace the shared manager configuration when no tickets or waiters exist.
- [static func makeForTesting(configuration: WiredMemoryManagerConfiguration) -> WiredMemoryManager](./wiredmemorymanager/makefortesting%28configuration%29.md)
  Test-only factory to create isolated managers.
### Default Implementations
- [Actor Implementations](./wiredmemorymanager/actor-implementations.md)

## Relationships

### Conforms To
- Swift.Sendable
- Swift.SendableMetatype
- _Concurrency.Actor

## See Also

### Memory
- [enum GPU](./gpu.md)
  API for controlling GPU related features.
- [struct WiredMemoryTicket](./wiredmemoryticket.md)
  Handle for coordinating wired memory changes across concurrent work.
- [protocol WiredMemoryPolicy](./wiredmemorypolicy.md)
  Policy for computing a process-global wired memory limit.
- [struct WiredMemoryEvent](./wiredmemoryevent.md)
  Debug event emitted by [`WiredMemoryManager`](./wiredmemorymanager.md) when coordinating wired memory changes.


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlx/wiredmemorymanager)*