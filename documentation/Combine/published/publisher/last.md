# last()

**Framework**: Combine  
**Kind**: method

Publishes the last element of a stream, after the stream finishes.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- macOS 10.15+
- tvOS 13.0+
- visionOS 1.0+
- watchOS 6.0+

## Declaration

```swift
func last() -> Publishers.Last<Self>
```

#### Return Value

A publisher that only publishes the last element of a stream.

#### Discussion

Use [`last()`](published/publisher/last().md) when you need to emit only the last element from an upstream publisher.

In the example below, the range publisher only emits the last element from the sequence publisher, `10`, then finishes normally.

```swift
let numbers = (-10...10)
cancellable = numbers.publisher
    .last()
    .sink { print("\($0)") }

// Prints: "10"
```

## See Also

- [func first() -> Publishers.First<Self>](published/publisher/first.md)
  Publishes the first element of a stream, then finishes.
- [func first(where: (Self.Output) -> Bool) -> Publishers.FirstWhere<Self>](published/publisher/first(where:).md)
  Publishes the first element of a stream to satisfy a predicate closure, then finishes normally.
- [func tryFirst(where: (Self.Output) throws -> Bool) -> Publishers.TryFirstWhere<Self>](published/publisher/tryfirst(where:).md)
  Publishes the first element of a stream to satisfy a throwing predicate closure, then finishes normally.
- [func last(where: (Self.Output) -> Bool) -> Publishers.LastWhere<Self>](published/publisher/last(where:).md)
  Publishes the last element of a stream that satisfies a predicate closure, after upstream finishes.
- [func tryLast(where: (Self.Output) throws -> Bool) -> Publishers.TryLastWhere<Self>](published/publisher/trylast(where:).md)
  Publishes the last element of a stream that satisfies an error-throwing predicate closure, after the stream finishes.
- [func output(at: Int) -> Publishers.Output<Self>](published/publisher/output(at:).md)
  Publishes a specific element, indicated by its index in the sequence of published elements.
- [func output<R>(in: R) -> Publishers.Output<Self>](published/publisher/output(in:).md)
  Publishes elements specified by their range in the sequence of published elements.


---

*[View on Apple Developer](https://developer.apple.com/documentation/combine/published/publisher/last())*