# mapError(_:)

**Framework**: Combine  
**Kind**: method

Converts any failure from the upstream publisher into a new error.

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
func mapError<E>(_ transform: @escaping (Self.Failure) -> E) -> Publishers.MapError<Self, E> where E : Error
```

#### Return Value

A publisher that replaces any upstream failure with a new error produced by the `transform` closure.

#### Discussion

Use the [`mapError(_:)`](publisher/maperror(_:).md) operator when you need to replace one error type with another, or where a downstream operator needs the error types of its inputs to match.

The following example uses a [`tryMap(_:)`](publisher/trymap(_:).md) operator to divide `1` by each element produced by a sequence publisher. When the publisher produces a `0`, the [`tryMap(_:)`](publisher/trymap(_:).md) fails with a `DivisionByZeroError`. The [`mapError(_:)`](publisher/maperror(_:).md) operator converts this into a `MyGenericError`.

```swift
struct DivisionByZeroError: Error {}
struct MyGenericError: Error { var wrappedError: Error }

func myDivide(_ dividend: Double, _ divisor: Double) throws -> Double {
       guard divisor != 0 else { throw DivisionByZeroError() }
       return dividend / divisor
   }

let divisors: [Double] = [5, 4, 3, 2, 1, 0]
divisors.publisher
    .tryMap { try myDivide(1, $0) }
    .mapError { MyGenericError(wrappedError: $0) }
    .sink(
        receiveCompletion: { print ("completion: \($0)") ,
        receiveValue: { print ("value: \($0)", terminator: " ") }
     )

// Prints: "0.2 0.25 0.3333333333333333 0.5 1.0 completion: failure(MyGenericError(wrappedError: DivisionByZeroError()))"
```

## Parameters

- `transform`: A closure that takes the upstream failure as a parameter and returns a new error for the publisher to terminate with.

## See Also

- [func map<T>((Self.Output) -> T) -> Publishers.Map<Self, T>](publishers/concatenate/map(_:)-392xi.md)
  Transforms all elements from the upstream publisher with a provided closure.
- [func tryMap<T>((Self.Output) throws -> T) -> Publishers.TryMap<Self, T>](publishers/concatenate/trymap(_:).md)
  Transforms all elements from the upstream publisher with a provided error-throwing closure.
- [func replaceNil<T>(with: T) -> Publishers.Map<Self, T>](publishers/concatenate/replacenil(with:).md)
  Replaces nil elements in the stream with the provided element.
- [func scan<T>(T, (T, Self.Output) -> T) -> Publishers.Scan<Self, T>](publishers/concatenate/scan(_:_:).md)
  Transforms elements from the upstream publisher by providing the current element to a closure along with the last value returned by the closure.
- [func tryScan<T>(T, (T, Self.Output) throws -> T) -> Publishers.TryScan<Self, T>](publishers/concatenate/tryscan(_:_:).md)
  Transforms elements from the upstream publisher by providing the current element to an error-throwing closure along with the last value returned by the closure.
- [func setFailureType<E>(to: E.Type) -> Publishers.SetFailureType<Self, E>](publishers/concatenate/setfailuretype(to:).md)
  Changes the failure type declared by the upstream publisher.


---

*[View on Apple Developer](https://developer.apple.com/documentation/combine/publishers/concatenate/maperror(_:))*