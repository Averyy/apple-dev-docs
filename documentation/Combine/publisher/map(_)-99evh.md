# map(_:)

**Framework**: Combine  
**Kind**: method  
**Role**: Instance Method

Transforms all elements from the upstream publisher with a provided closure.

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
func map<T>(_ transform: @escaping (Self.Output) -> T) -> Publishers.Map<Self, T>
```

## Mentions

- [Receiving and Handling Events with Combine](../receiving-and-handling-events-with-combine.md)

## Return Value

A publisher that uses the provided closure to map elements from the upstream publisher to new elements that it then publishes.

## Discussion

Combine’s [`map(_:)`](./map%28_%29-99evh.md) operator performs a function similar to that of [`map(_:)`](../../Swift/sequence/map%28_%29.md) in the Swift standard library: it uses a closure to transform each element it receives from the upstream publisher. You use [`map(_:)`](./map%28_%29-99evh.md) to transform from one kind of element to another.

The following example uses an array of numbers as the source for a collection based publisher. A [`map(_:)`](./map%28_%29-99evh.md) operator consumes each integer from the publisher and uses a dictionary to transform it from its Arabic numeral to a Roman equivalent, as a [`String`](../../Swift/string.md). If the [`map(_:)`](./map%28_%29-99evh.md)’s closure fails to look up a Roman numeral, it returns the string `(unknown)`.

```swift
let numbers = [5, 4, 3, 2, 1, 0]
let romanNumeralDict: [Int : String] =
   [1:"I", 2:"II", 3:"III", 4:"IV", 5:"V"]
cancellable = numbers.publisher
    .map { romanNumeralDict[$0] ?? "(unknown)" }
    .sink { print("\($0)", terminator: " ") }

// Prints: "V IV III II I (unknown)"
```

If your closure can throw an error, use Combine’s [`tryMap(_:)`](./trymap%28_%29.md) operator instead.

## Parameters

- `transform`: A closure that takes one element as its parameter and returns a new element.

## See Also

### Mapping elements
- [func tryMap<T>((Self.Output) throws -> T) -> Publishers.TryMap<Self, T>](./trymap%28_%29.md)
  Transforms all elements from the upstream publisher with a provided error-throwing closure.
- [func mapError<E>((Self.Failure) -> E) -> Publishers.MapError<Self, E>](./maperror%28_%29.md)
  Converts any failure from the upstream publisher into a new error.
- [func replaceNil<T>(with: T) -> Publishers.Map<Self, T>](./replacenil%28with%29.md)
  Replaces nil elements in the stream with the provided element.
- [func scan<T>(T, (T, Self.Output) -> T) -> Publishers.Scan<Self, T>](./scan%28_,_%29.md)
  Transforms elements from the upstream publisher by providing the current element to a closure along with the last value returned by the closure.
- [func tryScan<T>(T, (T, Self.Output) throws -> T) -> Publishers.TryScan<Self, T>](./tryscan%28_,_%29.md)
  Transforms elements from the upstream publisher by providing the current element to an error-throwing closure along with the last value returned by the closure.
- [func setFailureType<E>(to: E.Type) -> Publishers.SetFailureType<Self, E>](./setfailuretype%28to%29.md)
  Changes the failure type declared by the upstream publisher.


---

*[View on Apple Developer](https://developer.apple.com/documentation/combine/publisher/map(_:)-99evh)*