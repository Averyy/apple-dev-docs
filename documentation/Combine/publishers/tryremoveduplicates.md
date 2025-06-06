# Publishers.TryRemoveDuplicates

**Framework**: Combine  
**Kind**: struct

A publisher that publishes only elements that don’t match the previous element, as evaluated by a provided error-throwing closure.

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
struct TryRemoveDuplicates<Upstream> where Upstream : Publisher
```

## Topics

### Creating a Try Remove Duplicates Publisher
- [init(upstream: Upstream, predicate: (Publishers.TryRemoveDuplicates<Upstream>.Output, Publishers.TryRemoveDuplicates<Upstream>.Output) throws -> Bool)](publishers/tryremoveduplicates/init(upstream:predicate:).md)
  Creates a publisher that publishes only elements that don’t match the previous element, as evaluated by a provided error-throwing closure.
### Declaring Publisher Topography
- [Publishers.TryRemoveDuplicates.Output](publishers/tryremoveduplicates/output.md)
  The kind of values published by this publisher.
- [Publishers.TryRemoveDuplicates.Failure](publishers/tryremoveduplicates/failure.md)
  The kind of errors this publisher might publish.
### Inspecting Publisher Properties
- [let upstream: Upstream](publishers/tryremoveduplicates/upstream.md)
  The publisher from which this publisher receives elements.
- [let predicate: (Publishers.TryRemoveDuplicates<Upstream>.Output, Publishers.TryRemoveDuplicates<Upstream>.Output) throws -> Bool](publishers/tryremoveduplicates/predicate.md)
  An error-throwing closure to evaluate whether two elements are equivalent, for purposes of filtering.
### Applying Operators
- [Publisher Operators](publishers-tryremoveduplicates-publisher-operators.md)
  Methods that create downstream publishers or subscribers to act on the elements they receive.
### Default Implementations
- [Publisher Implementations](publishers/tryremoveduplicates/publisher-implementations.md)

## Relationships

### Conforms To
- [Publisher](publisher.md)

## See Also

- [Publishers.Filter](publishers/filter.md)
  A publisher that republishes all elements that match a provided closure.
- [Publishers.TryFilter](publishers/tryfilter.md)
  A publisher that republishes all elements that match a provided error-throwing closure.
- [Publishers.CompactMap](publishers/compactmap.md)
  A publisher that republishes all non-nil results of calling a closure with each received element.
- [Publishers.TryCompactMap](publishers/trycompactmap.md)
  A publisher that republishes all non-nil results of calling an error-throwing closure with each received element.
- [Publishers.RemoveDuplicates](publishers/removeduplicates.md)
  A publisher that publishes only elements that don’t match the previous element.
- [Publishers.ReplaceEmpty](publishers/replaceempty.md)
  A publisher that replaces an empty stream with a provided element.
- [Publishers.ReplaceError](publishers/replaceerror.md)
  A publisher that replaces any errors in the stream with a provided element.


---

*[View on Apple Developer](https://developer.apple.com/documentation/combine/publishers/tryremoveduplicates)*