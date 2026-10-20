# scan(_:_:)

**Framework**: Combine  
**Kind**: method  
**Role**: Instance Method

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

Available when `Elements` conforms to `Sequence` and `Failure` conforms to `Error`.

## See Also

### Mapping elements
- [func map<T>((Elements.Element) -> T) -> Publishers.Sequence<[T], Failure>](./map%28_%29.md)
- [func setFailureType<E>(to: E.Type) -> Publishers.Sequence<Elements, E>](./setfailuretype%28to%29.md)
- [func replaceNil<T>(with: T) -> Publishers.Sequence<[Publishers.Sequence<Elements, Failure>.Output], Failure>](./replacenil%28with%29.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/combine/publishers/sequence/scan(_:_:))*