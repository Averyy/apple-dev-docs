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

- [func first() -> Just<Output>](just/first.md)
- [func first(where: (Output) -> Bool) -> Optional<Output>.Publisher](just/first(where:).md)
- [func tryFirst(where: (Self.Output) throws -> Bool) -> Publishers.TryFirstWhere<Self>](just/tryfirst(where:).md)
  Publishes the first element of a stream to satisfy a throwing predicate closure, then finishes normally.
- [func last() -> Just<Output>](just/last.md)
- [func last(where: (Output) -> Bool) -> Optional<Output>.Publisher](just/last(where:).md)
- [func output(at: Int) -> Optional<Output>.Publisher](just/output(at:).md)
- [func output<R>(in: R) -> Optional<Output>.Publisher](just/output(in:).md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/combine/just/trylast(where:))*