---
url: "https://swiftpackageindex.com/apple/swift-async-algorithms/main/documentation/asyncalgorithms/asyncthrowingexclusivereductionssequence/share(bufferingpolicy:)"
framework: "swift-async-algorithms/AsyncAlgorithms"
---

# share(bufferingPolicy:)

**Framework**: swift-async-algorithms/AsyncAlgorithms  
**Kind**: method  
**Role**: Instance Method

Creates a shared async sequence that allows multiple concurrent iterations over a single source.

**Availability**:
- iOS 18.0+
- macOS 15.0+
- tvOS 18.0+
- visionOS 2.0+
- watchOS 11.0+

## Declaration

```swift
func share(bufferingPolicy: AsyncBufferSequencePolicy = .bounded(1)) -> some Sendable & AsyncSequence<Self.Element, Self.Failure>
```

Available when `Self` conforms to `SendableMetatype`, `AsyncIterator` conforms to `SendableMetatype`, and `Element` conforms to `Sendable`.

#### Return Value

A sendable async sequence that can be safely shared across multiple concurrent tasks.

#### Discussion

The `share` method transforms an async sequence into a shareable sequence that can be safely iterated by multiple concurrent tasks. This is useful when you want to broadcast elements from a single source to multiple consumers without duplicating work or creating separate iterations.

Each element from the source sequence is delivered to all active iterators. Elements are buffered according to the specified buffering policy to handle timing differences between consumers.

The base sequence is iterated in it’s own task to ensure that cancellation is not polluted from one side of iteration to another.

#### Example Usage

```swift
let numbers = [1, 2, 3, 4, 5].async.map {
 try? await Task.sleep(for: .seconds(1))
 return $0
}

let shared = numbers.share()

// Multiple tasks can iterate concurrently
let consumer1 = Task {
  for await value in shared {
    print("Consumer 1: \(value)")
  }
}

let consumer2 = Task {
  for await value in shared {
    print("Consumer 2: \(value)")
  }
}

await consumer1.value
await consumer2.value
```

## Parameters

- `bufferingPolicy`: The policy controlling how elements are enqueued to the shared buffer. Defaults to `.bounded(1)`.

  - `.bounded(n)`: Limits the buffer to `n` elements, applying backpressure to the source when that limit is reached
  - `.bufferingOldest(n)`: Keeps the oldest `n` elements, discarding newer ones when full
  - `.bufferingNewest(n)`: Keeps the newest `n` elements, discarding older ones when full
  - `.unbounded`: Allows unlimited buffering (use with caution)


---

*[View on Swift Package Index](https://swiftpackageindex.com/apple/swift-async-algorithms/main/documentation/asyncalgorithms/asyncthrowingexclusivereductionssequence/share(bufferingpolicy:))*