# Publishers.RemoveDuplicates

**Framework**: Combine  
**Kind**: struct  
**Role**: Structure

A publisher that publishes only elements that don’t match the previous element.

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
struct RemoveDuplicates<Upstream> where Upstream : Publisher
```

## Topics

### Creating a remove duplicates publisher
- [init(upstream: Upstream, predicate: (Publishers.RemoveDuplicates<Upstream>.Output, Publishers.RemoveDuplicates<Upstream>.Output) -> Bool)](./removeduplicates/init%28upstream,predicate%29.md)
  Creates a publisher that publishes only elements that don’t match the previous element, as evaluated by a provided closure.
### Declaring supporting types
- [Publishers.RemoveDuplicates.Output](./removeduplicates/output.md)
  The kind of values published by this publisher.
- [Publishers.RemoveDuplicates.Failure](./removeduplicates/failure.md)
  The kind of errors this publisher might publish.
### Inspecting publisher properties
- [let upstream: Upstream](./removeduplicates/upstream.md)
  The publisher from which this publisher receives elements.
- [let predicate: (Publishers.RemoveDuplicates<Upstream>.Output, Publishers.RemoveDuplicates<Upstream>.Output) -> Bool](./removeduplicates/predicate.md)
  The predicate closure used to evaluate whether two elements are duplicates.

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
- [Publishers.TryRemoveDuplicates](./tryremoveduplicates.md)
  A publisher that publishes only elements that don’t match the previous element, as evaluated by a provided error-throwing closure.
- [Publishers.ReplaceEmpty](./replaceempty.md)
  A publisher that replaces an empty stream with a provided element.
- [Publishers.ReplaceError](./replaceerror.md)
  A publisher that replaces any errors in the stream with a provided element.


---

*[View on Apple Developer](https://developer.apple.com/documentation/combine/publishers/removeduplicates)*