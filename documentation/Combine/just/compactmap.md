# compactMap(_:)

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
func compactMap<T>(_ transform: (Output) -> T?) -> Optional<T>.Publisher
```

## See Also

- [func filter((Output) -> Bool) -> Optional<Output>.Publisher](just/filter(_:).md)
- [func tryFilter((Self.Output) throws -> Bool) -> Publishers.TryFilter<Self>](just/tryfilter(_:).md)
  Republishes all elements that match a provided error-throwing closure.
- [func tryCompactMap<T>((Self.Output) throws -> T?) -> Publishers.TryCompactMap<Self, T>](just/trycompactmap(_:).md)
  Calls an error-throwing closure with each received element and publishes any returned optional that has a value.
- [func removeDuplicates() -> Just<Output>](just/removeduplicates.md)
- [func removeDuplicates(by: (Output, Output) -> Bool) -> Just<Output>](just/removeduplicates(by:).md)
- [func tryRemoveDuplicates(by: (Output, Output) throws -> Bool) -> Result<Output, any Error>.Publisher](just/tryremoveduplicates(by:).md)
- [func replaceEmpty(with: Output) -> Just<Output>](just/replaceempty(with:).md)
- [func replaceError(with: Output) -> Just<Output>](just/replaceerror(with:).md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/combine/just/compactmap(_:))*