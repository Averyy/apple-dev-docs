# tryReduce(_:_:)

**Framework**: Swift  
**Kind**: method

Applies an error-throwing closure that collects each element of a stream and publishes a final result upon completion.

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
func tryReduce<T>(_ initialResult: T, _ nextPartialResult: @escaping (T, Self.Output) throws -> T) -> Publishers.TryReduce<Self, T>
```

#### Return Value

A publisher that applies the closure to all received elements and produces an accumulated value when the upstream publisher finishes.

#### Discussion

Use [`tryReduce(_:_:)`](optional/publisher-swift.struct/tryreduce(_:_:).md) to collect a stream of elements and produce an accumulated value based on an error-throwing closure you provide. If the closure throws an error, the publisher fails and passes the error to its subscriber.

In the example below, the publisher’s `0` element causes the `myDivide(_:_:)` function to throw an error and publish the [`nan`](Double/nan.md) result:

```swift
struct DivisionByZeroError: Error {}
func myDivide(_ dividend: Double, _ divisor: Double) throws -> Double {
    guard divisor != 0 else { throw DivisionByZeroError() }
    return dividend / divisor
}

var numbers: [Double] = [5, 4, 3, 2, 1, 0]
numbers.publisher
    .tryReduce(numbers.first!, { accum, next in try myDivide(accum, next) })
    .catch({ _ in Just(Double.nan) })
    .sink { print("\($0)") }
```

## Parameters

- `initialResult`: The value that the closure receives the first time it’s called.
- `nextPartialResult`: An error-throwing closure that takes the previously-accumulated value and the next element from the upstream publisher to produce a new value.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/optional/publisher-swift.struct/tryreduce(_:_:))*