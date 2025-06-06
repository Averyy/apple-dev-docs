# output(at:)

**Framework**: Combine  
**Kind**: method

Publishes a specific element, indicated by its index in the sequence of published elements.

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
func output(at index: Int) -> Publishers.Output<Self>
```

#### Return Value

A publisher that publishes a specific indexed element.

#### Discussion

Use [`output(at:)`](publisher/output(at:).md) when you need to republish a specific element specified by its position in the stream. If the publisher completes normally or with an error before publishing the specified element, then the publisher doesn’t produce any elements.

In the example below, the array publisher emits the fifth element in the sequence of published elements:

```swift
let numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
numbers.publisher
    .output(at: 5)
    .sink { print("\($0)") }

// Prints: "6"
```

## Parameters

- `index`: The index that indicates the element to publish.

## See Also

- [func first() -> Publishers.First<Self>](publishers/prefixwhile/first.md)
  Publishes the first element of a stream, then finishes.
- [func first(where: (Self.Output) -> Bool) -> Publishers.FirstWhere<Self>](publishers/prefixwhile/first(where:).md)
  Publishes the first element of a stream to satisfy a predicate closure, then finishes normally.
- [func tryFirst(where: (Self.Output) throws -> Bool) -> Publishers.TryFirstWhere<Self>](publishers/prefixwhile/tryfirst(where:).md)
  Publishes the first element of a stream to satisfy a throwing predicate closure, then finishes normally.
- [func last() -> Publishers.Last<Self>](publishers/prefixwhile/last.md)
  Publishes the last element of a stream, after the stream finishes.
- [func last(where: (Self.Output) -> Bool) -> Publishers.LastWhere<Self>](publishers/prefixwhile/last(where:).md)
  Publishes the last element of a stream that satisfies a predicate closure, after upstream finishes.
- [func tryLast(where: (Self.Output) throws -> Bool) -> Publishers.TryLastWhere<Self>](publishers/prefixwhile/trylast(where:).md)
  Publishes the last element of a stream that satisfies an error-throwing predicate closure, after the stream finishes.
- [func output<R>(in: R) -> Publishers.Output<Self>](publishers/prefixwhile/output(in:).md)
  Publishes elements specified by their range in the sequence of published elements.


---

*[View on Apple Developer](https://developer.apple.com/documentation/combine/publishers/prefixwhile/output(at:))*