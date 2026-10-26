---
url: "https://swiftpackageindex.com/apple/swift-async-algorithms/main/documentation/asyncalgorithms/asyncbuffersequencepolicy"
framework: "swift-async-algorithms/AsyncAlgorithms"
---

# AsyncBufferSequencePolicy

**Framework**: swift-async-algorithms/AsyncAlgorithms  
**Kind**: struct  
**Role**: Structure

A policy dictating the buffering behaviour of an [`AsyncBufferSequence`](./asyncbuffersequence.md)

**Availability**:
- iOS 13.0+
- macOS 10.15+
- tvOS 13.0+
- watchOS 6.0+

## Declaration

```swift
struct AsyncBufferSequencePolicy
```

## Topics

### Type Properties
- [static var unbounded: AsyncBufferSequencePolicy](./asyncbuffersequencepolicy/unbounded.md)
  A policy for buffering elements without limit.
### Type Methods
- [static func bounded(Int) -> AsyncBufferSequencePolicy](./asyncbuffersequencepolicy/bounded%28_%29.md)
  A policy for buffering elements until the limit is reached. Then consumption of the upstream `AsyncSequence` will be paused until elements are consumed from the buffer. If the limit is zero then no buffering policy is applied.
- [static func bufferingLatest(Int) -> AsyncBufferSequencePolicy](./asyncbuffersequencepolicy/bufferinglatest%28_%29.md)
  A policy for buffering elements until the limit is reached. After the limit is reached and a new element is produced by the upstream, the oldest buffered element will be discarded. If the limit is zero then no buffering policy is applied.
- [static func bufferingOldest(Int) -> AsyncBufferSequencePolicy](./asyncbuffersequencepolicy/bufferingoldest%28_%29.md)
  A policy for buffering elements until the limit is reached. After the limit is reached and a new element is produced by the upstream, the latest buffered element will be discarded. If the limit is zero then no buffering policy is applied.

## Relationships

### Conforms To
- Swift.Sendable
- Swift.SendableMetatype


---

*[View on Swift Package Index](https://swiftpackageindex.com/apple/swift-async-algorithms/main/documentation/asyncalgorithms/asyncbuffersequencepolicy)*