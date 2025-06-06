# Publishers.TryCompactMap

**Framework**: Combine  
**Kind**: struct

A publisher that republishes all non-nil results of calling an error-throwing closure with each received element.

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
struct TryCompactMap<Upstream, Output> where Upstream : Publisher
```

## Topics

### Creating a Try Compact Map Publisher
- [init(upstream: Upstream, transform: (Upstream.Output) throws -> Output?)](publishers/trycompactmap/init(upstream:transform:).md)
### Declaring Publisher Topography
- [Publishers.Output](publishers/output.md)
  A publisher that publishes elements specified by a range in the sequence of published elements.
- [Publishers.TryCompactMap.Failure](publishers/trycompactmap/failure.md)
  The kind of errors this publisher might publish.
### Inspecting Publisher Properties
- [let upstream: Upstream](publishers/trycompactmap/upstream.md)
  The publisher from which this publisher receives elements.
- [let transform: (Upstream.Output) throws -> Output?](publishers/trycompactmap/transform.md)
  An error-throwing closure that receives values from the upstream publisher and returns optional values.
### Applying Operators
- [Publisher Operators](publishers-trycompactmap-publisher-operators.md)
  Methods that create downstream publishers or subscribers to act on the elements they receive.
### Default Implementations
- [Publisher Implementations](publishers/trycompactmap/publisher-implementations.md)

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
- [Publishers.RemoveDuplicates](publishers/removeduplicates.md)
  A publisher that publishes only elements that don’t match the previous element.
- [Publishers.TryRemoveDuplicates](publishers/tryremoveduplicates.md)
  A publisher that publishes only elements that don’t match the previous element, as evaluated by a provided error-throwing closure.
- [Publishers.ReplaceEmpty](publishers/replaceempty.md)
  A publisher that replaces an empty stream with a provided element.
- [Publishers.ReplaceError](publishers/replaceerror.md)
  A publisher that replaces any errors in the stream with a provided element.


---

*[View on Apple Developer](https://developer.apple.com/documentation/combine/publishers/trycompactmap)*