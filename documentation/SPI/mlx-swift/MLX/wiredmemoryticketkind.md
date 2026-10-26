---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlx/wiredmemoryticketkind"
framework: "mlx-swift/MLX"
---

# WiredMemoryTicketKind

**Framework**: mlx-swift/MLX  
**Kind**: enum  
**Role**: Enumeration

Describes whether a ticket represents active work or a long-lived reservation.

## Declaration

```swift
enum WiredMemoryTicketKind
```

#### Overview

Reservation tickets participate in admission and limit calculation, but do not keep the wired limit elevated on their own. This allows modeling long-lived weights without wiring memory while the system is idle.

## Topics

### Enumeration Cases
- [WiredMemoryTicketKind.active](./wiredmemoryticketkind/active.md)
  Active work that should drive limit updates (e.g. inference).
- [WiredMemoryTicketKind.reservation](./wiredmemoryticketkind/reservation.md)
  Passive reservation that should be considered for admission but should not keep the wired limit elevated on its own.
### Default Implementations
- [Equatable Implementations](./wiredmemoryticketkind/equatable-implementations.md)

## Relationships

### Conforms To
- Swift.Equatable
- Swift.Hashable
- Swift.Sendable
- Swift.SendableMetatype


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlx/wiredmemoryticketkind)*