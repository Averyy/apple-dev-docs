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
func filter(_ isIncluded: (Output) -> Bool) -> Optional<Output>.Publisher
```

## See Also

### Filtering elements
- [func compactMap<T>((Output) -> T?) -> Optional<T>.Publisher](./compactmap%28_%29.md)
- [func removeDuplicates() -> Just<Output>](./removeduplicates%28%29.md)
- [func removeDuplicates(by: (Output, Output) -> Bool) -> Just<Output>](./removeduplicates%28by%29.md)
- [func tryRemoveDuplicates(by: (Output, Output) throws -> Bool) -> Result<Output, any Error>.Publisher](./tryremoveduplicates%28by%29.md)
- [func replaceEmpty(with: Output) -> Just<Output>](./replaceempty%28with%29.md)
- [func replaceError(with: Output) -> Just<Output>](./replaceerror%28with%29.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/combine/just/filter(_:))*