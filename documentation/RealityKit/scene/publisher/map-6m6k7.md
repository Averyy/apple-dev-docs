# map(_:)

**Framework**: RealityKit  
**Kind**: method

Transforms all elements from the upstream publisher with a provided closure.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst ?+
- macOS 10.15+
- tvOS 13.0+
- visionOS ?+
- watchOS 6.0+

## Declaration

```swift
func map<T>(_ transform: @escaping (Self.Output) -> T) -> Publishers.Map<Self, T>
```

#### Return Value

A publisher that uses the provided closure to map elements from the upstream publisher to new elements that it then publishes.

#### Discussion

Combine’s `Publisher/map(_:)-99evh` operator performs a function similar to that of [`map(_:)`](https://developer.apple.com/documentation/Swift/Sequence/map(_:)) in the Swift standard library: it uses a closure to transform each element it receives from the upstream publisher. You use `Publisher/map(_:)-99evh` to transform from one kind of element to another.

The following example uses an array of numbers as the source for a collection based publisher. A `Publisher/map(_:)-99evh` operator consumes each integer from the publisher and uses a dictionary to transform it from its Arabic numeral to a Roman equivalent, as a [`String`](https://developer.apple.com/documentation/Swift/String). If the `Publisher/map(_:)-99evh`’s closure fails to look up a Roman numeral, it returns the string `(unknown)`.

```None
let numbers = [5, 4, 3, 2, 1, 0]
let romanNumeralDict: [Int : String] =
   [1:"I", 2:"II", 3:"III", 4:"IV", 5:"V"]
cancellable = numbers.publisher
    .map { romanNumeralDict[$0] ?? "(unknown)" }
    .sink { print("\($0)", terminator: " ") }

// Prints: "V IV III II I (unknown)"
```

If your closure can throw an error, use Combine’s [`tryMap(_:)`](scene/publisher/trymap(_:).md) operator instead.

## Parameters

- `transform`: A closure that takes one element as its parameter and returns a new element.

## See Also

- [func tryMap<T>((Self.Output) throws -> T) -> Publishers.TryMap<Self, T>](scene/publisher/trymap(_:).md)
  Transforms all elements from the upstream publisher with a provided error-throwing closure.
- [func flatMap<T, P>(maxPublishers: Subscribers.Demand, (Self.Output) -> P) -> Publishers.FlatMap<P, Self>](scene/publisher/flatmap(maxpublishers:_:)-9f9ie.md)
  Transforms all elements from an upstream publisher into a new publisher up to a maximum number of publishers you specify.
- [func mapError<E>((Self.Failure) -> E) -> Publishers.MapError<Self, E>](scene/publisher/maperror(_:).md)
  Converts any failure from the upstream publisher into a new error.
- [func replaceNil<T>(with: T) -> Publishers.Map<Self, T>](scene/publisher/replacenil(with:).md)
  Replaces nil elements in the stream with the provided element.
- [func scan<T>(T, (T, Self.Output) -> T) -> Publishers.Scan<Self, T>](scene/publisher/scan(_:_:).md)
  Transforms elements from the upstream publisher by providing the current element to a closure along with the last value returned by the closure.
- [func tryScan<T>(T, (T, Self.Output) throws -> T) -> Publishers.TryScan<Self, T>](scene/publisher/tryscan(_:_:).md)
  Transforms elements from the upstream publisher by providing the current element to an error-throwing closure along with the last value returned by the closure.
- [func setFailureType<E>(to: E.Type) -> Publishers.SetFailureType<Self, E>](scene/publisher/setfailuretype(to:).md)
  Changes the failure type declared by the upstream publisher.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/scene/publisher/map(_:)-6m6k7)*