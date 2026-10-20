# Publishers.ReplaceError

**Framework**: Combine  
**Kind**: struct  
**Role**: Structure

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
- [init(upstream: Upstream, output: Publishers.ReplaceError<Upstream>.Output)](./replaceerror/init%28upstream,output%29.md)
  Creates a publisher that replaces any errors in the stream with a provided element.
### Declaring supporting types
- [Publishers.ReplaceError.Output](./replaceerror/output-swift.typealias.md)
  The kind of values published by this publisher.
- [Publishers.ReplaceError.Output](./replaceerror/output-swift.typealias.md)
  The kind of values published by this publisher.
- [Publishers.ReplaceError.Failure](./replaceerror/failure.md)
  The kind of errors this publisher might publish.
### Inspecting publisher properties
- [let upstream: Upstream](./replaceerror/upstream.md)
  The publisher from which this publisher receives elements.
- [let output: Publishers.ReplaceError<Upstream>.Output](./replaceerror/output-swift.property.md)
  The element with which to replace errors from the upstream publisher.
- [let output: Publishers.ReplaceError<Upstream>.Output](./replaceerror/output-swift.property.md)
  The element with which to replace errors from the upstream publisher.
### Comparing publishers
- [static func == (Publishers.ReplaceError<Upstream>, Publishers.ReplaceError<Upstream>) -> Bool](./replaceerror/eqeq%28_,_%29.md)
  Returns a Boolean value that indicates whether two publishers are equivalent.
### Default Implementations
- [Equatable Implementations](./replaceerror/equatable-implementations.md)

## Relationships

### Conforms To
- [Equatable](../../Swift/equatable.md)
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
- [Publishers.TryRemoveDuplicates](./tryremoveduplicates.md)
  A publisher that publishes only elements that don’t match the previous element, as evaluated by a provided error-throwing closure.
- [Publishers.ReplaceEmpty](./replaceempty.md)
  A publisher that replaces an empty stream with a provided element.


---

*[View on Apple Developer](https://developer.apple.com/documentation/combine/publishers/replaceerror)*