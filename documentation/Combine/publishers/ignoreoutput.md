# Publishers.IgnoreOutput

**Framework**: Combine  
**Kind**: struct

A publisher that ignores all upstream elements, but passes along the upstream publisher’s completion state (finished or failed).

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
struct IgnoreOutput<Upstream> where Upstream : Publisher
```

## Topics

### Creating an Ignore Output Publisher
- [init(upstream: Upstream)](publishers/ignoreoutput/init(upstream:).md)
  Creates a publisher that ignores all upstream elements, but passes along the upstream publisher’s completion state (finish or failed).
### Declaring Publisher Topography
- [Publishers.IgnoreOutput.Output](publishers/ignoreoutput/output.md)
  The kind of values published by this publisher.
- [Publishers.IgnoreOutput.Failure](publishers/ignoreoutput/failure.md)
  The kind of errors this publisher might publish.
### Inspecting Publisher Properties
- [let upstream: Upstream](publishers/ignoreoutput/upstream.md)
  The publisher from which this publisher receives elements.
### Comparing Publishers
- [static func == (Publishers.IgnoreOutput<Upstream>, Publishers.IgnoreOutput<Upstream>) -> Bool](publishers/ignoreoutput/==(_:_:).md)
  Returns a Boolean value that indicates whether two publishers are equivalent.
- [static func != (Self, Self) -> Bool](publishers/ignoreoutput/!=(_:_:).md)
  Returns a Boolean value indicating whether two values are not equal.
### Applying Operators
- [Publisher Operators](publishers-ignoreoutput-publisher-operators.md)
  Methods that create downstream publishers or subscribers to act on the elements they receive.
### Default Implementations
- [Equatable Implementations](publishers/ignoreoutput/equatable-implementations.md)
- [Publisher Implementations](publishers/ignoreoutput/publisher-implementations.md)

## Relationships

### Conforms To
- [Copyable](../Swift/Copyable.md)
- [Equatable](../Swift/Equatable.md)
- [Publisher](publisher.md)

## See Also

- [Publishers.Collect](publishers/collect.md)
  A publisher that buffers items.
- [Publishers.CollectByCount](publishers/collectbycount.md)
  A publisher that buffers a maximum number of items.
- [Publishers.CollectByTime](publishers/collectbytime.md)
  A publisher that buffers and periodically publishes its items.
- [Publishers.TimeGroupingStrategy](publishers/timegroupingstrategy.md)
  A strategy for collecting received elements.
- [Publishers.Reduce](publishers/reduce.md)
  A publisher that applies a closure to all received elements and produces an accumulated value when the upstream publisher finishes.
- [Publishers.TryReduce](publishers/tryreduce.md)
  A publisher that applies an error-throwing closure to all received elements and produces an accumulated value when the upstream publisher finishes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/combine/publishers/ignoreoutput)*