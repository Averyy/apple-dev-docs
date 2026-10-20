# Publishers.TryRemoveDuplicates

**Framework**: Combine  
**Kind**: struct  
**Role**: Structure

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

### Creating a try-remove-duplicates publisher
- [init(upstream: Upstream, predicate: (Publishers.TryRemoveDuplicates<Upstream>.Output, Publishers.TryRemoveDuplicates<Upstream>.Output) throws -> Bool)](./tryremoveduplicates/init%28upstream,predicate%29.md)
  Creates a publisher that publishes only elements that don’t match the previous element, as evaluated by a provided error-throwing closure.
### Declaring supporting types
- [Publishers.Output](./output.md)
  A publisher that publishes elements specified by a range in the sequence of published elements.
### Inspecting publisher properties
- [let upstream: Upstream](./tryremoveduplicates/upstream.md)
  The publisher from which this publisher receives elements.
- [let predicate: (Publishers.TryRemoveDuplicates<Upstream>.Output, Publishers.TryRemoveDuplicates<Upstream>.Output) throws -> Bool](./tryremoveduplicates/predicate.md)
  An error-throwing closure to evaluate whether two elements are equivalent, for purposes of filtering.

## Relationships

### Conforms To
- [Publisher](../publisher.md)

## See Also

### Filtering elements
- [Publishers.Filter](./filter.md)
  A publisher that republishes all elements that match a provided closure.
- [Publishers.TryFilter](./tryfilter.md)
  A publisher that republishes all elements that match a provided error-throwing closure.
- [Publishers.CompactMap](./compactmap.md)
  A publisher that republishes all non-nil results of calling a closure with each received element.
- [Publishers.TryCompactMap](./trycompactmap.md)
  A publisher that republishes all non-nil results of calling an error-throwing closure with each received element.
- [Publishers.RemoveDuplicates](./removeduplicates.md)
  A publisher that publishes only elements that don’t match the previous element.
- [Publishers.ReplaceEmpty](./replaceempty.md)
  A publisher that replaces an empty stream with a provided element.
- [Publishers.ReplaceError](./replaceerror.md)
  A publisher that replaces any errors in the stream with a provided element.


---

*[View on Apple Developer](https://developer.apple.com/documentation/combine/publishers/tryremoveduplicates)*