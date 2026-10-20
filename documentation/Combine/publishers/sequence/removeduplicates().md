# removeDuplicates()

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
func removeDuplicates() -> Publishers.Sequence<[Publishers.Sequence<Elements, Failure>.Output], Failure>
```

Available when `Elements` conforms to `Sequence`, `Failure` conforms to `Error`, and `Elements.Element` conforms to `Equatable`.

## See Also

### Filtering elements
- [func filter((Publishers.Sequence<Elements, Failure>.Output) -> Bool) -> Publishers.Sequence<[Publishers.Sequence<Elements, Failure>.Output], Failure>](./filter%28_%29.md)
- [func compactMap<T>((Publishers.Sequence<Elements, Failure>.Output) -> T?) -> Publishers.Sequence<[T], Failure>](./compactmap%28_%29.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/combine/publishers/sequence/removeduplicates())*