# tryFilter(_:)

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
func tryFilter(_ isIncluded: @escaping (Publishers.TryFilter<Upstream>.Output) throws -> Bool) -> Publishers.TryFilter<Upstream>
```

## See Also

- [func filter((Publishers.TryFilter<Upstream>.Output) -> Bool) -> Publishers.TryFilter<Upstream>](publishers/tryfilter/filter(_:).md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/combine/publishers/tryfilter/tryfilter(_:))*