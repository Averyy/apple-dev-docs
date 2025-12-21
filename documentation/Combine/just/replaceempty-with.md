# replaceEmpty(with:)

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
func replaceEmpty(with output: Output) -> Just<Output>
```

## See Also

- [func filter((Output) -> Bool) -> Optional<Output>.Publisher](just/filter(_:).md)
- [func compactMap<T>((Output) -> T?) -> Optional<T>.Publisher](just/compactmap(_:).md)
- [func removeDuplicates() -> Just<Output>](just/removeduplicates.md)
- [func removeDuplicates(by: (Output, Output) -> Bool) -> Just<Output>](just/removeduplicates(by:).md)
- [func tryRemoveDuplicates(by: (Output, Output) throws -> Bool) -> Result<Output, any Error>.Publisher](just/tryremoveduplicates(by:).md)
- [func replaceError(with: Output) -> Just<Output>](just/replaceerror(with:).md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/combine/just/replaceempty(with:))*