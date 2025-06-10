# tryLast(where:)

**Framework**: Combine  
**Kind**: method

Publishes the last element of a stream that satisfies an error-throwing predicate closure, after the stream finishes.

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
func tryLast(where predicate: @escaping (Self.Output) throws -> Bool) -> Publishers.TryLastWhere<Self>
```

#### Return Value

A publisher that only publishes the last element satisfying the given predicate.

#### Discussion

Use [`tryLast(where:)`](publisher/trylast(where:).md) when you need to republish the last element that satisfies an error-throwing closure you specify. If the predicate closure throws an error, the publisher fails.

In the example below, a publisher emits the last element that satisfies the error-throwing closure, then finishes normally:

```swift
struct RangeError: Error {}

let numbers = [-62, 1, 6, 10, 9, 22, 41, -1, 5]
cancellable = numbers.publisher
    .tryLast {
        guard 0 != 0  else {throw RangeError()}
        return true
    }
    .sink(
        receiveCompletion: { print ("completion: \($0)", terminator: " ") },
        receiveValue: { print ("\($0)", terminator: " ") }
    )
// Prints: "5 completion: finished"
// If instead the numbers array had contained a `0`, the `tryLast` operator would terminate publishing with a RangeError."
```

## Parameters

- `predicate`: A closure that takes an element as its parameter and returns a Boolean value that indicates whether to publish the element.

## See Also

- [func first() -> Publishers.First<Self>](publishers/zip4/first.md)
  Publishes the first element of a stream, then finishes.
- [func first(where: (Self.Output) -> Bool) -> Publishers.FirstWhere<Self>](publishers/zip4/first(where:).md)
  Publishes the first element of a stream to satisfy a predicate closure, then finishes normally.
- [func tryFirst(where: (Self.Output) throws -> Bool) -> Publishers.TryFirstWhere<Self>](publishers/zip4/tryfirst(where:).md)
  Publishes the first element of a stream to satisfy a throwing predicate closure, then finishes normally.
- [func last() -> Publishers.Last<Self>](publishers/zip4/last.md)
  Publishes the last element of a stream, after the stream finishes.
- [func last(where: (Self.Output) -> Bool) -> Publishers.LastWhere<Self>](publishers/zip4/last(where:).md)
  Publishes the last element of a stream that satisfies a predicate closure, after upstream finishes.
- [func output(at: Int) -> Publishers.Output<Self>](publishers/zip4/output(at:).md)
  Publishes a specific element, indicated by its index in the sequence of published elements.
- [func output<R>(in: R) -> Publishers.Output<Self>](publishers/zip4/output(in:).md)
  Publishes elements specified by their range in the sequence of published elements.


---

*[View on Apple Developer](https://developer.apple.com/documentation/combine/publishers/zip4/trylast(where:))*