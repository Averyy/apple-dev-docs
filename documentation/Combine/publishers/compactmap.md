# Publishers.CompactMap

**Framework**: Combine  
**Kind**: struct

A publisher that republishes all non-nil results of calling a closure with each received element.

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
struct CompactMap<Upstream, Output> where Upstream : Publisher
```

## Topics

### Creating a compact map publisher
- [init(upstream: Upstream, transform: (Upstream.Output) -> Output?)](publishers/compactmap/init(upstream:transform:).md)
  Creates a publisher that republishes all non-`nil` results of calling a closure with each received element.
### Declaring supporting types
- [Publishers.Output](publishers/output.md)
  A publisher that publishes elements specified by a range in the sequence of published elements.
- [Publishers.CompactMap.Failure](publishers/compactmap/failure.md)
  The kind of errors this publisher might publish.
### Mapping elements
- [func map<T>((Output) -> T) -> Publishers.CompactMap<Upstream, T>](publishers/compactmap/map(_:).md)
- [func compactMap<T>((Output) -> T?) -> Publishers.CompactMap<Upstream, T>](publishers/compactmap/compactmap(_:).md)
### Inspecting publisher properties
- [let upstream: Upstream](publishers/compactmap/upstream.md)
  The publisher from which this publisher receives elements.
- [let transform: (Upstream.Output) -> Output?](publishers/compactmap/transform.md)
  A closure that receives values from the upstream publisher and returns optional values.

## Relationships

### Conforms To
- [Publisher](publisher.md)

## See Also

- [Publishers.Filter](publishers/filter.md)
  A publisher that republishes all elements that match a provided closure.
- [Publishers.TryFilter](publishers/tryfilter.md)
  A publisher that republishes all elements that match a provided error-throwing closure.
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

*[View on Apple Developer](https://developer.apple.com/documentation/combine/publishers/compactmap)*