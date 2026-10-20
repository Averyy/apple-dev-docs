# Publishers.CollectByCount

**Framework**: Combine  
**Kind**: struct  
**Role**: Structure

A publisher that buffers a maximum number of items.

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
struct CollectByCount<Upstream> where Upstream : Publisher
```

## Topics

### Creating a collect by count publisher
- [init(upstream: Upstream, count: Int)](./collectbycount/init%28upstream,count%29.md)
  Creates a publisher that buffers a maximum number of items.
### Declaring supporting types
- [Publishers.CollectByCount.Output](./collectbycount/output.md)
  The kind of values published by this publisher.
- [Publishers.CollectByCount.Failure](./collectbycount/failure.md)
  The kind of errors this publisher might publish.
### Inspecting publisher properties
- [let upstream: Upstream](./collectbycount/upstream.md)
  The publisher that this publisher receives elements from.
- [let count: Int](./collectbycount/count.md)
  The maximum number of received elements to buffer before publishing.
### Comparing publishers
- [static func == (Publishers.CollectByCount<Upstream>, Publishers.CollectByCount<Upstream>) -> Bool](./collectbycount/eqeq%28_,_%29.md)
  Returns a Boolean value that indicates whether two publishers are equivalent.
### Default Implementations
- [Equatable Implementations](./collectbycount/equatable-implementations.md)

## Relationships

### Conforms To
- [Equatable](../../Swift/equatable.md)
- [Publisher](../publisher.md)

## See Also

### Reducing elements
- [Publishers.Collect](./collect.md)
  A publisher that buffers items.
- [Publishers.CollectByTime](./collectbytime.md)
  A publisher that buffers and periodically publishes its items.
- [Publishers.TimeGroupingStrategy](./timegroupingstrategy.md)
  A strategy for collecting received elements.
- [Publishers.IgnoreOutput](./ignoreoutput.md)
  A publisher that ignores all upstream elements, but passes along the upstream publisher’s completion state (finished or failed).
- [Publishers.Reduce](./reduce.md)
  A publisher that applies a closure to all received elements and produces an accumulated value when the upstream publisher finishes.
- [Publishers.TryReduce](./tryreduce.md)
  A publisher that applies an error-throwing closure to all received elements and produces an accumulated value when the upstream publisher finishes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/combine/publishers/collectbycount)*