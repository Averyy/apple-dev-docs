---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlx/wiredmemoryevent/kind-swift.enum"
framework: "mlx-swift/MLX"
---

# WiredMemoryEvent.Kind

**Framework**: mlx-swift/MLX  
**Kind**: enum  
**Role**: Enumeration

## Declaration

```swift
enum Kind
```

## Topics

### Enumeration Cases
- [WiredMemoryEvent.Kind.admissionCancelled](./kind-swift.enum/admissioncancelled.md)
  A waiting ticket was cancelled.
- [WiredMemoryEvent.Kind.admissionGranted](./kind-swift.enum/admissiongranted.md)
  A waiting ticket was admitted.
- [WiredMemoryEvent.Kind.admissionWait](./kind-swift.enum/admissionwait.md)
  A ticket could not be admitted and will wait for capacity.
- [WiredMemoryEvent.Kind.baselineCaptured](./kind-swift.enum/baselinecaptured.md)
  The baseline wired limit was captured from the system.
- [WiredMemoryEvent.Kind.baselineRestored](./kind-swift.enum/baselinerestored.md)
  The manager restored the baseline when work completed.
- [WiredMemoryEvent.Kind.limitApplied](./kind-swift.enum/limitapplied.md)
  The manager successfully applied a new limit.
- [WiredMemoryEvent.Kind.limitApplyFailed](./kind-swift.enum/limitapplyfailed.md)
  The manager attempted to apply a new limit but failed.
- [WiredMemoryEvent.Kind.limitComputed](./kind-swift.enum/limitcomputed.md)
  The manager computed a desired limit from policy inputs.
- [WiredMemoryEvent.Kind.ticketEndIgnored](./kind-swift.enum/ticketendignored.md)
  A duplicate end was ignored (ticket not active).
- [WiredMemoryEvent.Kind.ticketEnded](./kind-swift.enum/ticketended.md)
  A ticket ended.
- [WiredMemoryEvent.Kind.ticketStartIgnored](./kind-swift.enum/ticketstartignored.md)
  A duplicate start was ignored (ticket already active).
- [WiredMemoryEvent.Kind.ticketStarted](./kind-swift.enum/ticketstarted.md)
  A ticket became active.
### Initializers
- [init?(rawValue: String)](./kind-swift.enum/init%28rawvalue%29.md)
### Default Implementations
- [Equatable Implementations](./kind-swift.enum/equatable-implementations.md)
- [RawRepresentable Implementations](./kind-swift.enum/rawrepresentable-implementations.md)

## Relationships

### Conforms To
- Swift.Equatable
- Swift.Hashable
- Swift.RawRepresentable
- Swift.Sendable
- Swift.SendableMetatype


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlx/wiredmemoryevent/kind-swift.enum)*