# tryFilter(_:)

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
func tryFilter(_ isIncluded: @escaping (Publishers.Filter<Upstream>.Output) throws -> Bool) -> Publishers.TryFilter<Upstream>
```

Available when `Upstream` conforms to `Publisher`.

## See Also

### Filtering elements
- [func filter((Publishers.Filter<Upstream>.Output) -> Bool) -> Publishers.Filter<Upstream>](./filter%28_%29.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/combine/publishers/filter/tryfilter(_:))*