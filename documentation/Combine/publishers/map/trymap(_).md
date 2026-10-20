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

- [func map<T>((Output) -> T) -> Publishers.Map<Upstream, T>](publishers/map/map(_:).md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/combine/publishers/map/trymap(_:))*