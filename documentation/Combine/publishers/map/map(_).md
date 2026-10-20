# map(_:)

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
func map<T>(_ transform: @escaping (Output) -> T) -> Publishers.Map<Upstream, T>
```

Available when `Upstream` conforms to `Publisher`.

## See Also

### Mapping elements
- [func tryMap<T>((Output) throws -> T) -> Publishers.TryMap<Upstream, T>](./trymap%28_%29.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/combine/publishers/map/map(_:))*