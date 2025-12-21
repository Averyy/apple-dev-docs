# Publishers.Filter

**Framework**: Combine  
**Kind**: struct

A publisher that republishes all elements that match a provided closure.

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
struct Filter<Upstream> where Upstream : Publisher
```

## Topics

### Creating a filter publisher
- [init(upstream: Upstream, isIncluded: (Upstream.Output) -> Bool)](publishers/filter/init(upstream:isincluded:).md)
  Creates a publisher that republishes all elements that match a provided closure.
### Filtering elements
- [func filter((Publishers.Filter<Upstream>.Output) -> Bool) -> Publishers.Filter<Upstream>](publishers/filter/filter(_:).md)
- [func tryFilter((Publishers.Filter<Upstream>.Output) throws -> Bool) -> Publishers.TryFilter<Upstream>](publishers/filter/tryfilter(_:).md)
### Declaring supporting types
- [Publishers.Filter.Output](publishers/filter/output.md)
  The kind of values published by this publisher.
- [Publishers.Filter.Failure](publishers/filter/failure.md)
  The kind of errors this publisher might publish.
### Inspecting publisher properties
- [let upstream: Upstream](publishers/filter/upstream.md)
  The publisher from which this publisher receives elements.
- [let isIncluded: (Upstream.Output) -> Bool](publishers/filter/isincluded.md)
  A closure that indicates whether to republish an element.

## Relationships

### Conforms To
- [Publisher](publisher.md)

## See Also

- [Publishers.TryFilter](publishers/tryfilter.md)
  A publisher that republishes all elements that match a provided error-throwing closure.
- [Publishers.CompactMap](publishers/compactmap.md)
  A publisher that republishes all non-nil results of calling a closure with each received element.
- [Publishers.TryCompactMap](publishers/trycompactmap.md)
  A publisher that republishes all non-nil results of calling an error-throwing closure with each received element.
- [Publishers.RemoveDuplicates](publishers/removeduplicates.md)
  A publisher that publishes only elements that don’t match the previous element.
- [Publishers.TryRemoveDuplicates](publishers/tryremoveduplicates.md)
  A publisher that publishes only elements that don’t match the previous element, as evaluated by a provided error-throwing closure.
- [Publishers.ReplaceEmpty](publishers/replaceempty.md)
  A publisher that replaces an empty stream with a provided element.
- [Publishers.ReplaceError](publishers/replaceerror.md)
  A publisher that replaces any errors in the stream with a provided element.


---

*[View on Apple Developer](https://developer.apple.com/documentation/combine/publishers/filter)*