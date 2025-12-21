# map(_:)

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
func map<T>(_ transform: @escaping (Output) -> T) -> Publishers.CompactMap<Upstream, T>
```

## See Also

- [func compactMap<T>((Output) -> T?) -> Publishers.CompactMap<Upstream, T>](publishers/compactmap/compactmap(_:).md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/combine/publishers/compactmap/map(_:))*