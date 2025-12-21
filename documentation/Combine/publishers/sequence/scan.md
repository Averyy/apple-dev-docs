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
func scan<T>(_ initialResult: T, _ nextPartialResult: @escaping (T, Publishers.Sequence<Elements, Failure>.Output) -> T) -> Publishers.Sequence<[T], Failure>
```

## See Also

- [func map<T>((Elements.Element) -> T) -> Publishers.Sequence<[T], Failure>](publishers/sequence/map(_:).md)
- [func setFailureType<E>(to: E.Type) -> Publishers.Sequence<Elements, E>](publishers/sequence/setfailuretype(to:).md)
- [func replaceNil<T>(with: T) -> Publishers.Sequence<[Publishers.Sequence<Elements, Failure>.Output], Failure>](publishers/sequence/replacenil(with:).md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/combine/publishers/sequence/scan(_:_:))*