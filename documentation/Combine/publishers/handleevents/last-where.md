# last(where:)

**Framework**: Combine  
**Kind**: method

Publishes the last element of a stream that satisfies a predicate closure, after upstream finishes.

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
func last(where predicate: @escaping (Self.Output) -> Bool) -> Publishers.LastWhere<Self>
```

#### Return Value

A publisher that only publishes the last element satisfying the given predicate.

#### Discussion

Use [`last(where:)`](publisher/last(where:).md) when you need to republish only the last element of a stream that satisfies a closure you specify.

In the example below, a range publisher emits the last element that satisfies the closure’s criteria, then finishes normally:

```swift
let numbers = (-10...10)
cancellable = numbers.publisher
    .last { $0 < 6 }
    .sink { print("\($0)") }

// Prints: "5"
```

## Parameters

- `predicate`: A closure that takes an element as its parameter and returns a Boolean value that indicates whether to publish the element.

## See Also

- [func first() -> Publishers.First<Self>](publishers/handleevents/first.md)
  Publishes the first element of a stream, then finishes.
- [func first(where: (Self.Output) -> Bool) -> Publishers.FirstWhere<Self>](publishers/handleevents/first(where:).md)
  Publishes the first element of a stream to satisfy a predicate closure, then finishes normally.
- [func tryFirst(where: (Self.Output) throws -> Bool) -> Publishers.TryFirstWhere<Self>](publishers/handleevents/tryfirst(where:).md)
  Publishes the first element of a stream to satisfy a throwing predicate closure, then finishes normally.
- [func last() -> Publishers.Last<Self>](publishers/handleevents/last.md)
  Publishes the last element of a stream, after the stream finishes.
- [func tryLast(where: (Self.Output) throws -> Bool) -> Publishers.TryLastWhere<Self>](publishers/handleevents/trylast(where:).md)
  Publishes the last element of a stream that satisfies an error-throwing predicate closure, after the stream finishes.
- [func output(at: Int) -> Publishers.Output<Self>](publishers/handleevents/output(at:).md)
  Publishes a specific element, indicated by its index in the sequence of published elements.
- [func output<R>(in: R) -> Publishers.Output<Self>](publishers/handleevents/output(in:).md)
  Publishes elements specified by their range in the sequence of published elements.


---

*[View on Apple Developer](https://developer.apple.com/documentation/combine/publishers/handleevents/last(where:))*