# scan(_:_:)

**Framework**: Combine  
**Kind**: method

Transforms elements from the upstream publisher by providing the current element to a closure along with the last value returned by the closure.

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
func scan<T>(_ initialResult: T, _ nextPartialResult: @escaping (T, Self.Output) -> T) -> Publishers.Scan<Self, T>
```

#### Return Value

A publisher that transforms elements by applying a closure that receives its previous return value and the next element from the upstream publisher.

#### Discussion

Use [`scan(_:_:)`](publisher/scan(_:_:).md) to accumulate all previously-published values into a single value, which you then combine with each newly-published value.

The following example logs a running total of all values received from the sequence publisher.

```swift
let range = (0...5)
cancellable = range.publisher
    .scan(0) { return $0 + $1 }
    .sink { print ("\($0)", terminator: " ") }
 // Prints: "0 1 3 6 10 15 ".
```

## Parameters

- `initialResult`: The previous result returned by the   closure.
- `nextPartialResult`: A closure that takes as its arguments the previous value returned by the closure and the next element emitted from the upstream publisher.

## See Also

- [func map<T>((Self.Output) -> T) -> Publishers.Map<Self, T>](publishers/assertnofailure/map(_:)-7csfa.md)
  Transforms all elements from the upstream publisher with a provided closure.
- [func tryMap<T>((Self.Output) throws -> T) -> Publishers.TryMap<Self, T>](publishers/assertnofailure/trymap(_:).md)
  Transforms all elements from the upstream publisher with a provided error-throwing closure.
- [func mapError<E>((Self.Failure) -> E) -> Publishers.MapError<Self, E>](publishers/assertnofailure/maperror(_:).md)
  Converts any failure from the upstream publisher into a new error.
- [func replaceNil<T>(with: T) -> Publishers.Map<Self, T>](publishers/assertnofailure/replacenil(with:).md)
  Replaces nil elements in the stream with the provided element.
- [func tryScan<T>(T, (T, Self.Output) throws -> T) -> Publishers.TryScan<Self, T>](publishers/assertnofailure/tryscan(_:_:).md)
  Transforms elements from the upstream publisher by providing the current element to an error-throwing closure along with the last value returned by the closure.
- [func setFailureType<E>(to: E.Type) -> Publishers.SetFailureType<Self, E>](publishers/assertnofailure/setfailuretype(to:).md)
  Changes the failure type declared by the upstream publisher.


---

*[View on Apple Developer](https://developer.apple.com/documentation/combine/publishers/assertnofailure/scan(_:_:))*