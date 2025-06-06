# reduce(_:_:)

**Framework**: Combine  
**Kind**: method

Applies a closure that collects each element of a stream and publishes a final result upon completion.

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
func reduce<T>(_ initialResult: T, _ nextPartialResult: @escaping (T, Self.Output) -> T) -> Publishers.Reduce<Self, T>
```

#### Return Value

A publisher that applies the closure to all received elements and produces an accumulated value when the upstream publisher finishes. If [`reduce(_:_:)`](publisher/reduce(_:_:).md) receives an error from the upstream publisher, the operator delivers it to the downstream subscriber, the publisher terminates and publishes no value.

#### Discussion

Use [`reduce(_:_:)`](publisher/reduce(_:_:).md) to collect a stream of elements and produce an accumulated value based on a closure you provide.

In the following example, the [`reduce(_:_:)`](publisher/reduce(_:_:).md) operator collects all the integer values it receives from its upstream publisher:

```swift
let numbers = (0...10)
cancellable = numbers.publisher
    .reduce(0, { accum, next in accum + next })
    .sink { print("\($0)") }

// Prints: "55"
```

## Parameters

- `initialResult`: The value that the closure receives the first time it’s called.
- `nextPartialResult`: A closure that produces a new value by taking the previously-accumulated value and the next element it receives from the upstream publisher.


---

*[View on Apple Developer](https://developer.apple.com/documentation/combine/just/reduce(_:_:)-11pp5)*