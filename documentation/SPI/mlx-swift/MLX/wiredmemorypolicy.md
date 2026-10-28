---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlx/wiredmemorypolicy"
framework: "mlx-swift/MLX"
---

# WiredMemoryPolicy

**Framework**: mlx-swift/MLX  
**Kind**: protocol  
**Role**: Protocol

Policy for computing a process-global wired memory limit.

## Declaration

```swift
protocol WiredMemoryPolicy : Identifiable, Sendable where Self.ID == AnyHashable
```

## Mentions

- [Wired Memory Management](./wired-memory.md)

## Overview

Policies are grouped by their `id` so that multiple tickets can coordinate through a shared policy instance. The manager computes one limit per policy group, then uses the maximum across groups to avoid double-counting and to allow heterogeneous strategies to coexist. For reference-type policies, provide a stable `id` to define grouping semantics.

## Topics

### Instance Methods
- [func canAdmit(baseline: Int, activeSizes: [Int], newSize: Int) -> Bool](./wiredmemorypolicy/canadmit%28baseline,activesizes,newsize%29.md)
  Decide whether a new ticket can be admitted. Defaults to allowing all tickets.
- [func limit(baseline: Int, activeSizes: [Int]) -> Int](./wiredmemorypolicy/limit%28baseline,activesizes%29.md)
  Compute the desired wired limit in bytes for the current active set.
- [func ticket(size: Int, manager: WiredMemoryManager, kind: WiredMemoryTicketKind) -> WiredMemoryTicket](./wiredmemorypolicy/ticket%28size,manager,kind%29.md)
  Convenience to create a ticket bound to a policy and manager.

## Relationships

### Inherits From
- Swift.Identifiable
- Swift.Sendable
- Swift.SendableMetatype
### Conforming Types
- [WiredMaxPolicy](./wiredmaxpolicy.md)
- [WiredSumPolicy](./wiredsumpolicy.md)

## See Also

### Memory
- [enum GPU](./gpu.md)
  API for controlling GPU related features.
- [actor WiredMemoryManager](./wiredmemorymanager.md)
  Central coordinator for process-wide wired memory limits.
- [struct WiredMemoryTicket](./wiredmemoryticket.md)
  Handle for coordinating wired memory changes across concurrent work.
- [struct WiredMemoryEvent](./wiredmemoryevent.md)
  Debug event emitted by [`WiredMemoryManager`](./wiredmemorymanager.md) when coordinating wired memory changes.


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlx/wiredmemorypolicy)*