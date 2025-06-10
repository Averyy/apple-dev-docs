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
func compactMap<T>(_ transform: @escaping (Output) throws -> T?) -> Publishers.TryCompactMap<Upstream, T>
```

## See Also

- [func filter((Self.Output) -> Bool) -> Publishers.Filter<Self>](publishers/trycompactmap/filter(_:).md)
  Republishes all elements that match a provided closure.
- [func tryFilter((Self.Output) throws -> Bool) -> Publishers.TryFilter<Self>](publishers/trycompactmap/tryfilter(_:).md)
  Republishes all elements that match a provided error-throwing closure.
- [func compactMap<T>((Self.Output) -> T?) -> Publishers.CompactMap<Self, T>](publishers/trycompactmap/compactmap(_:)-9ip9g.md)
  Calls a closure with each received element and publishes any returned optional that has a value.
- [func tryCompactMap<T>((Self.Output) throws -> T?) -> Publishers.TryCompactMap<Self, T>](publishers/trycompactmap/trycompactmap(_:).md)
  Calls an error-throwing closure with each received element and publishes any returned optional that has a value.
- [func removeDuplicates() -> Publishers.RemoveDuplicates<Self>](publishers/trycompactmap/removeduplicates.md)
  Publishes only elements that don’t match the previous element.
- [func removeDuplicates(by: (Self.Output, Self.Output) -> Bool) -> Publishers.RemoveDuplicates<Self>](publishers/trycompactmap/removeduplicates(by:).md)
  Publishes only elements that don’t match the previous element, as evaluated by a provided closure.
- [func tryRemoveDuplicates(by: (Self.Output, Self.Output) throws -> Bool) -> Publishers.TryRemoveDuplicates<Self>](publishers/trycompactmap/tryremoveduplicates(by:).md)
  Publishes only elements that don’t match the previous element, as evaluated by a provided error-throwing closure.
- [func replaceEmpty(with: Self.Output) -> Publishers.ReplaceEmpty<Self>](publishers/trycompactmap/replaceempty(with:).md)
  Replaces an empty stream with the provided element.
- [func replaceError(with: Self.Output) -> Publishers.ReplaceError<Self>](publishers/trycompactmap/replaceerror(with:).md)
  Replaces any errors in the stream with the provided element.


---

*[View on Apple Developer](https://developer.apple.com/documentation/combine/publishers/trycompactmap/compactmap(_:))*