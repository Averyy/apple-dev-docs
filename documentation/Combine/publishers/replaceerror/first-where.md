# first(where:)

**Framework**: Combine  
**Kind**: method

Publishes the first element of a stream to satisfy a predicate closure, then finishes normally.

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
func first(where predicate: @escaping (Self.Output) -> Bool) -> Publishers.FirstWhere<Self>
```

#### Return Value

A publisher that only publishes the first element of a stream that satisfies the predicate.

#### Discussion

Use [`first(where:)`](publisher/first(where:).md) to republish only the first element of a stream that satisfies a closure you specify. The publisher ignores all elements after the first element that satisfies the closure and finishes normally. If this publisher doesn’t receive any elements, it finishes without publishing.

In the example below, the provided closure causes the [`Publishers.FirstWhere`](publishers/firstwhere.md) publisher to republish the first received element that’s greater than `0`, then finishes normally.

```swift
let numbers = (-10...10)
cancellable = numbers.publisher
    .first { $0 > 0 }
    .sink { print("\($0)") }

// Prints: "1"
```

## Parameters

- `predicate`: A closure that takes an element as a parameter and returns a Boolean value that indicates whether to publish the element.

## See Also

- [func first() -> Publishers.First<Self>](publishers/replaceerror/first.md)
  Publishes the first element of a stream, then finishes.
- [func tryFirst(where: (Self.Output) throws -> Bool) -> Publishers.TryFirstWhere<Self>](publishers/replaceerror/tryfirst(where:).md)
  Publishes the first element of a stream to satisfy a throwing predicate closure, then finishes normally.
- [func last() -> Publishers.Last<Self>](publishers/replaceerror/last.md)
  Publishes the last element of a stream, after the stream finishes.
- [func last(where: (Self.Output) -> Bool) -> Publishers.LastWhere<Self>](publishers/replaceerror/last(where:).md)
  Publishes the last element of a stream that satisfies a predicate closure, after upstream finishes.
- [func tryLast(where: (Self.Output) throws -> Bool) -> Publishers.TryLastWhere<Self>](publishers/replaceerror/trylast(where:).md)
  Publishes the last element of a stream that satisfies an error-throwing predicate closure, after the stream finishes.
- [func output(at: Int) -> Publishers.Output<Self>](publishers/replaceerror/output(at:).md)
  Publishes a specific element, indicated by its index in the sequence of published elements.
- [func output<R>(in: R) -> Publishers.Output<Self>](publishers/replaceerror/output(in:).md)
  Publishes elements specified by their range in the sequence of published elements.


---

*[View on Apple Developer](https://developer.apple.com/documentation/combine/publishers/replaceerror/first(where:))*