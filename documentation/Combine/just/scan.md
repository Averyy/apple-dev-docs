# scan(_:_:)

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
func scan<T>(_ initialResult: T, _ nextPartialResult: (T, Output) -> T) -> Result<T, Just<Output>.Failure>.Publisher
```

## See Also

- [func map<T>((Output) -> T) -> Just<T>](just/map(_:).md)
- [func tryMap<T>((Output) throws -> T) -> Result<T, any Error>.Publisher](just/trymap(_:).md)
- [func mapError<E>((Just<Output>.Failure) -> E) -> Result<Output, E>.Publisher](just/maperror(_:).md)
- [func replaceNil<T>(with: T) -> Publishers.Map<Self, T>](just/replacenil(with:).md)
  Replaces nil elements in the stream with the provided element.
- [func tryScan<T>(T, (T, Output) throws -> T) -> Result<T, any Error>.Publisher](just/tryscan(_:_:).md)
- [func setFailureType<E>(to: E.Type) -> Result<Output, E>.Publisher](just/setfailuretype(to:).md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/combine/just/scan(_:_:))*