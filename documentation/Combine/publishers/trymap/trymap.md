# tryMap(_:)

**Framework**: Combine  
**Kind**: method

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
func tryMap<T>(_ transform: @escaping (Output) throws -> T) -> Publishers.TryMap<Upstream, T>
```

## See Also

- [func map<T>((Self.Output) -> T) -> Publishers.Map<Self, T>](publishers/trymap/map(_:)-13zij.md)
  Transforms all elements from the upstream publisher with a provided closure.
- [func map<T>((Output) -> T) -> Publishers.TryMap<Upstream, T>](publishers/trymap/map(_:).md)
- [func tryMap<T>((Self.Output) throws -> T) -> Publishers.TryMap<Self, T>](publishers/trymap/trymap(_:)-6b3tc.md)
  Transforms all elements from the upstream publisher with a provided error-throwing closure.
- [func mapError<E>((Self.Failure) -> E) -> Publishers.MapError<Self, E>](publishers/trymap/maperror(_:).md)
  Converts any failure from the upstream publisher into a new error.
- [func replaceNil<T>(with: T) -> Publishers.Map<Self, T>](publishers/trymap/replacenil(with:).md)
  Replaces nil elements in the stream with the provided element.
- [func scan<T>(T, (T, Self.Output) -> T) -> Publishers.Scan<Self, T>](publishers/trymap/scan(_:_:).md)
  Transforms elements from the upstream publisher by providing the current element to a closure along with the last value returned by the closure.
- [func tryScan<T>(T, (T, Self.Output) throws -> T) -> Publishers.TryScan<Self, T>](publishers/trymap/tryscan(_:_:).md)
  Transforms elements from the upstream publisher by providing the current element to an error-throwing closure along with the last value returned by the closure.


---

*[View on Apple Developer](https://developer.apple.com/documentation/combine/publishers/trymap/trymap(_:))*