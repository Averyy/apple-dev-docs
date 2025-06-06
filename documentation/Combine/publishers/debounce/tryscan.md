# tryScan(_:_:)

**Framework**: Combine  
**Kind**: method

Transforms elements from the upstream publisher by providing the current element to an error-throwing closure along with the last value returned by the closure.

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
func tryScan<T>(_ initialResult: T, _ nextPartialResult: @escaping (T, Self.Output) throws -> T) -> Publishers.TryScan<Self, T>
```

#### Return Value

A publisher that transforms elements by applying a closure that receives its previous return value and the next element from the upstream publisher.

#### Discussion

Use [`tryScan(_:_:)`](publisher/tryscan(_:_:).md) to accumulate all previously-published values into a single value, which you then combine with each newly-published value. If your accumulator closure throws an error, the publisher terminates with the error.

In the example below, [`tryScan(_:_:)`](publisher/tryscan(_:_:).md) calls a division function on elements of a collection publisher. The [`Publishers.TryScan`](publishers/tryscan.md) publisher publishes each result until the function encounters a `DivisionByZeroError`, which terminates the publisher.

```swift
struct DivisionByZeroError: Error {}

/// A function that throws a DivisionByZeroError if `current` provided by the TryScan publisher is zero.
func myThrowingFunction(_ lastValue: Int, _ currentValue: Int) throws -> Int {
    guard currentValue != 0 else { throw DivisionByZeroError() }
    return (lastValue + currentValue) / currentValue
 }

let numbers = [1,2,3,4,5,0,6,7,8,9]
cancellable = numbers.publisher
    .tryScan(10) { try myThrowingFunction($0, $1) }
    .sink(
        receiveCompletion: { print ("\($0)") },
        receiveValue: { print ("\($0)", terminator: " ") }
     )

// Prints: "11 6 3 1 1 -1 failure(DivisionByZeroError())".
```

If the closure throws an error, the publisher fails with the error.

## Parameters

- `initialResult`: The previous result returned by the   closure.
- `nextPartialResult`: An error-throwing closure that takes as its arguments the previous value returned by the closure and the next element emitted from the upstream publisher.

## See Also

- [func map<T>((Self.Output) -> T) -> Publishers.Map<Self, T>](publishers/debounce/map(_:)-3qccr.md)
  Transforms all elements from the upstream publisher with a provided closure.
- [func tryMap<T>((Self.Output) throws -> T) -> Publishers.TryMap<Self, T>](publishers/debounce/trymap(_:).md)
  Transforms all elements from the upstream publisher with a provided error-throwing closure.
- [func mapError<E>((Self.Failure) -> E) -> Publishers.MapError<Self, E>](publishers/debounce/maperror(_:).md)
  Converts any failure from the upstream publisher into a new error.
- [func replaceNil<T>(with: T) -> Publishers.Map<Self, T>](publishers/debounce/replacenil(with:).md)
  Replaces nil elements in the stream with the provided element.
- [func scan<T>(T, (T, Self.Output) -> T) -> Publishers.Scan<Self, T>](publishers/debounce/scan(_:_:).md)
  Transforms elements from the upstream publisher by providing the current element to a closure along with the last value returned by the closure.
- [func setFailureType<E>(to: E.Type) -> Publishers.SetFailureType<Self, E>](publishers/debounce/setfailuretype(to:).md)
  Changes the failure type declared by the upstream publisher.


---

*[View on Apple Developer](https://developer.apple.com/documentation/combine/publishers/debounce/tryscan(_:_:))*