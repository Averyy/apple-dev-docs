---
url: "https://swiftpackageindex.com/apple/swift-async-algorithms/main/documentation/asyncalgorithms/asyncthrowingchannel/buffer(policy:)"
framework: "swift-async-algorithms/AsyncAlgorithms"
---

# buffer(policy:)

**Framework**: swift-async-algorithms/AsyncAlgorithms  
**Kind**: method  
**Role**: Instance Method

Creates an asynchronous sequence that buffers elements.

**Availability**:
- iOS 13.0+
- macOS 10.15+
- tvOS 13.0+
- watchOS 6.0+

## Declaration

```swift
func buffer(policy: AsyncBufferSequencePolicy) -> AsyncBufferSequence<Self>
```

Available when `Self` conforms to `Sendable`.

## Return Value

An asynchronous sequence that buffers elements up to a given limit.

## Discussion

The buffering behaviour is dictated by the policy:

- bounded: will buffer elements until the limit is reached. Then it will suspend the upstream async sequence.
- unbounded: will buffer elements without limit.
- bufferingNewest: will buffer elements until the limit is reached. Then it will discard the oldest elements.
- bufferingOldest: will buffer elements until the limit is reached. Then it will discard the newest elements.

## Parameters

- `policy`: A policy that drives the behaviour of the [`AsyncBufferSequence`](../asyncbuffersequence.md)


---

*[View on Swift Package Index](https://swiftpackageindex.com/apple/swift-async-algorithms/main/documentation/asyncalgorithms/asyncthrowingchannel/buffer(policy:))*