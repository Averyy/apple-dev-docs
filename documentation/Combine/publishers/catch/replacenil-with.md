# replaceNil(with:)

**Framework**: Combine  
**Kind**: method

Replaces nil elements in the stream with the provided element.

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
func replaceNil<T>(with output: T) -> Publishers.Map<Self, T> where Self.Output == T?
```

#### Return Value

A publisher that replaces `nil` elements from the upstream publisher with the provided element.

#### Discussion

The [`replaceNil(with:)`](publisher/replacenil(with:).md) operator enables replacement of `nil` values in a stream with a substitute value. In the example below, a collection publisher contains a nil value. The [`replaceNil(with:)`](publisher/replacenil(with:).md) operator replaces this with `0.0`.

```swift
let numbers: [Double?] = [1.0, 2.0, nil, 3.0]
numbers.publisher
    .replaceNil(with: 0.0)
    .sink { print("\($0)", terminator: " ") }

// Prints: "Optional(1.0) Optional(2.0) Optional(0.0) Optional(3.0)"
```

## Parameters

- `output`: The element to use when replacing  .

## See Also

- [func map<T>((Self.Output) -> T) -> Publishers.Map<Self, T>](publishers/catch/map(_:)-6vw93.md)
  Transforms all elements from the upstream publisher with a provided closure.
- [func tryMap<T>((Self.Output) throws -> T) -> Publishers.TryMap<Self, T>](publishers/catch/trymap(_:).md)
  Transforms all elements from the upstream publisher with a provided error-throwing closure.
- [func mapError<E>((Self.Failure) -> E) -> Publishers.MapError<Self, E>](publishers/catch/maperror(_:).md)
  Converts any failure from the upstream publisher into a new error.
- [func scan<T>(T, (T, Self.Output) -> T) -> Publishers.Scan<Self, T>](publishers/catch/scan(_:_:).md)
  Transforms elements from the upstream publisher by providing the current element to a closure along with the last value returned by the closure.
- [func tryScan<T>(T, (T, Self.Output) throws -> T) -> Publishers.TryScan<Self, T>](publishers/catch/tryscan(_:_:).md)
  Transforms elements from the upstream publisher by providing the current element to an error-throwing closure along with the last value returned by the closure.
- [func setFailureType<E>(to: E.Type) -> Publishers.SetFailureType<Self, E>](publishers/catch/setfailuretype(to:).md)
  Changes the failure type declared by the upstream publisher.


---

*[View on Apple Developer](https://developer.apple.com/documentation/combine/publishers/catch/replacenil(with:))*