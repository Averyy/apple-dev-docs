# Publishers.ReplaceError

**Framework**: Combine  
**Kind**: struct

A publisher that replaces any errors in the stream with a provided element.

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
struct ReplaceError<Upstream> where Upstream : Publisher
```

## Topics

### Creating a replace error Publisher
- [init(upstream: Upstream, output: Publishers.ReplaceError<Upstream>.Output)](publishers/replaceerror/init(upstream:output:).md)
  Creates a publisher that replaces any errors in the stream with a provided element.
### Declaring supporting types
- [Publishers.ReplaceError.Output](publishers/replaceerror/output-swift.typealias.md)
  The kind of values published by this publisher.
- [Publishers.ReplaceError.Output](publishers/replaceerror/output-swift.typealias.md)
  The kind of values published by this publisher.
- [Publishers.ReplaceError.Failure](publishers/replaceerror/failure.md)
  The kind of errors this publisher might publish.
### Inspecting publisher properties
- [let upstream: Upstream](publishers/replaceerror/upstream.md)
  The publisher from which this publisher receives elements.
- [let output: Publishers.ReplaceError<Upstream>.Output](publishers/replaceerror/output-swift.property.md)
  The element with which to replace errors from the upstream publisher.
- [let output: Publishers.ReplaceError<Upstream>.Output](publishers/replaceerror/output-swift.property.md)
  The element with which to replace errors from the upstream publisher.
### Comparing publishers
- [static func == (Publishers.ReplaceError<Upstream>, Publishers.ReplaceError<Upstream>) -> Bool](publishers/replaceerror/==(_:_:).md)
  Returns a Boolean value that indicates whether two publishers are equivalent.
### Default Implementations
- [Equatable Implementations](publishers/replaceerror/equatable-implementations.md)

## Relationships

### Conforms To
- [Copyable](../Swift/Copyable.md)
- [Equatable](../Swift/Equatable.md)
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
- [Publishers.TryRemoveDuplicates](publishers/tryremoveduplicates.md)
  A publisher that publishes only elements that don’t match the previous element, as evaluated by a provided error-throwing closure.
- [Publishers.ReplaceEmpty](publishers/replaceempty.md)
  A publisher that replaces an empty stream with a provided element.


---

*[View on Apple Developer](https://developer.apple.com/documentation/combine/publishers/replaceerror)*