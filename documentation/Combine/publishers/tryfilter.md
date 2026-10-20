# Publishers.TryFilter

**Framework**: Combine  
**Kind**: struct  
**Role**: Structure

A publisher that republishes all elements that match a provided error-throwing closure.

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
struct TryFilter<Upstream> where Upstream : Publisher
```

## Topics

### Creating a try-filter publisher
- [init(upstream: Upstream, isIncluded: (Upstream.Output) throws -> Bool)](./tryfilter/init%28upstream,isincluded%29.md)
  Creates a publisher that republishes all elements that match a provided error-throwing closure.
### Filtering elements
- [func filter((Publishers.TryFilter<Upstream>.Output) -> Bool) -> Publishers.TryFilter<Upstream>](./tryfilter/filter%28_%29.md)
- [func tryFilter((Publishers.TryFilter<Upstream>.Output) throws -> Bool) -> Publishers.TryFilter<Upstream>](./tryfilter/tryfilter%28_%29.md)
### Declaring supporting types
- [Publishers.TryFilter.Output](./tryfilter/output.md)
  The kind of values published by this publisher.
- [Publishers.TryFilter.Failure](./tryfilter/failure.md)
  The kind of errors this publisher might publish.
### Inspecting publisher properties
- [let upstream: Upstream](./tryfilter/upstream.md)
  The publisher from which this publisher receives elements.
- [let isIncluded: (Upstream.Output) throws -> Bool](./tryfilter/isincluded.md)
  An error-throwing closure that indicates whether this filter should republish an element.

## Relationships

### Conforms To
- [Publisher](../publisher.md)

## See Also

### Filtering elements
- [Publishers.Filter](./filter.md)
  A publisher that republishes all elements that match a provided closure.
- [Publishers.CompactMap](./compactmap.md)
  A publisher that republishes all non-nil results of calling a closure with each received element.
- [Publishers.TryCompactMap](./trycompactmap.md)
  A publisher that republishes all non-nil results of calling an error-throwing closure with each received element.
- [Publishers.RemoveDuplicates](./removeduplicates.md)
  A publisher that publishes only elements that don’t match the previous element.
- [Publishers.TryRemoveDuplicates](./tryremoveduplicates.md)
  A publisher that publishes only elements that don’t match the previous element, as evaluated by a provided error-throwing closure.
- [Publishers.ReplaceEmpty](./replaceempty.md)
  A publisher that replaces an empty stream with a provided element.
- [Publishers.ReplaceError](./replaceerror.md)
  A publisher that replaces any errors in the stream with a provided element.


---

*[View on Apple Developer](https://developer.apple.com/documentation/combine/publishers/tryfilter)*