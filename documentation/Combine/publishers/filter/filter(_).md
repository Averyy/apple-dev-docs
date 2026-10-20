# filter(_:)

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
func filter(_ isIncluded: @escaping (Publishers.Filter<Upstream>.Output) -> Bool) -> Publishers.Filter<Upstream>
```

Available when `Upstream` conforms to `Publisher`.

## See Also

### Filtering elements
- [func tryFilter((Publishers.Filter<Upstream>.Output) throws -> Bool) -> Publishers.TryFilter<Upstream>](./tryfilter%28_%29.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/combine/publishers/filter/filter(_:))*