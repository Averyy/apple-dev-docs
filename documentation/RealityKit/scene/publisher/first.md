# first()

**Framework**: RealityKit  
**Kind**: method

Publishes the first element of a stream, then finishes.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst ?+
- macOS 10.15+
- tvOS 13.0+
- visionOS ?+
- watchOS 6.0+

## Declaration

```swift
func first() -> Publishers.First<Self>
```

#### Return Value

A publisher that only publishes the first element of a stream.

#### Discussion

Use [`first()`](scene/publisher/first().md) to publish just the first element from an upstream publisher, then finish normally. The [`first()`](scene/publisher/first().md) operator requests `Subscribers/Demand/unlimited` from its upstream as soon as downstream requests at least one element. If the upstream completes before [`first()`](scene/publisher/first().md) receives any elements, it completes without emitting any values.

In this example, the [`first()`](scene/publisher/first().md) publisher republishes the first element received from the sequence publisher, `-10`, then finishes normally.

```None
let numbers = (-10...10)
cancellable = numbers.publisher
    .first()
    .sink { print("\($0)") }

// Print: "-10"
```

## See Also

- [func first(where: (Self.Output) -> Bool) -> Publishers.FirstWhere<Self>](scene/publisher/first(where:).md)
  Publishes the first element of a stream to satisfy a predicate closure, then finishes normally.
- [func tryFirst(where: (Self.Output) throws -> Bool) -> Publishers.TryFirstWhere<Self>](scene/publisher/tryfirst(where:).md)
  Publishes the first element of a stream to satisfy a throwing predicate closure, then finishes normally.
- [func last() -> Publishers.Last<Self>](scene/publisher/last.md)
  Publishes the last element of a stream, after the stream finishes.
- [func last(where: (Self.Output) -> Bool) -> Publishers.LastWhere<Self>](scene/publisher/last(where:).md)
  Publishes the last element of a stream that satisfies a predicate closure, after upstream finishes.
- [func tryLast(where: (Self.Output) throws -> Bool) -> Publishers.TryLastWhere<Self>](scene/publisher/trylast(where:).md)
  Publishes the last element of a stream that satisfies an error-throwing predicate closure, after the stream finishes.
- [func output(at: Int) -> Publishers.Output<Self>](scene/publisher/output(at:).md)
  Publishes a specific element, indicated by its index in the sequence of published elements.
- [func output<R>(in: R) -> Publishers.Output<Self>](scene/publisher/output(in:).md)
  Publishes elements specified by their range in the sequence of published elements.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/scene/publisher/first())*