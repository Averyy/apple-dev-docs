# Publishers.TryFilter

**Framework**: Combine  
**Kind**: struct

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

### Creating a Try Filter Publisher
- [init(upstream: Upstream, isIncluded: (Upstream.Output) throws -> Bool)](publishers/tryfilter/init(upstream:isincluded:).md)
  Creates a publisher that republishes all elements that match a provided error-throwing closure.
### Declaring Publisher Topography
- [Publishers.TryFilter.Output](publishers/tryfilter/output.md)
  The kind of values published by this publisher.
- [Publishers.TryFilter.Failure](publishers/tryfilter/failure.md)
  The kind of errors this publisher might publish.
### Inspecting Publisher Properties
- [let upstream: Upstream](publishers/tryfilter/upstream.md)
  The publisher from which this publisher receives elements.
- [let isIncluded: (Upstream.Output) throws -> Bool](publishers/tryfilter/isincluded.md)
  An error-throwing closure that indicates whether this filter should republish an element.
### Applying Operators
- [Publisher Operators](publishers-tryfilter-publisher-operators.md)
  Methods that create downstream publishers or subscribers to act on the elements they receive.
### Default Implementations
- [Publisher Implementations](publishers/tryfilter/publisher-implementations.md)

## Relationships

### Conforms To
- [Publisher](publisher.md)

## See Also

- [Publishers.Filter](publishers/filter.md)
  A publisher that republishes all elements that match a provided closure.
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

*[View on Apple Developer](https://developer.apple.com/documentation/combine/publishers/tryfilter)*