# Publishers.Collect

**Framework**: Combine  
**Kind**: struct  
**Role**: Structure

A publisher that buffers items.

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
struct Collect<Upstream> where Upstream : Publisher
```

## Topics

### Creating a collect publisher
- [init(upstream: Upstream)](./collect/init%28upstream%29.md)
  Creates a publisher that buffers items.
### Declaring supporting types
- [Publishers.Collect.Output](./collect/output.md)
  The kind of values published by this publisher.
- [Publishers.Collect.Failure](./collect/failure.md)
  The kind of errors this publisher might publish.
### Inspecting publisher properties
- [let upstream: Upstream](./collect/upstream.md)
  The publisher that this publisher receives elements from.
### Comparing publishers
- [static func == (Publishers.Collect<Upstream>, Publishers.Collect<Upstream>) -> Bool](./collect/eqeq%28_,_%29.md)
  Returns a Boolean value that indicates whether two publishers are equivalent.
### Default Implementations
- [Equatable Implementations](./collect/equatable-implementations.md)

## Relationships

### Conforms To
- [Equatable](../../Swift/equatable.md)
- [Publisher](../publisher.md)

## See Also

### Reducing elements
- [Publishers.CollectByCount](./collectbycount.md)
  A publisher that buffers a maximum number of items.
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

*[View on Apple Developer](https://developer.apple.com/documentation/combine/publishers/collect)*