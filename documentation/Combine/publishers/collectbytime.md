# Publishers.CollectByTime

**Framework**: Combine  
**Kind**: struct

A publisher that buffers and periodically publishes its items.

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
struct CollectByTime<Upstream, Context> where Upstream : Publisher, Context : Scheduler
```

## Topics

### Creating a Collect by Time Publisher
- [init(upstream: Upstream, strategy: Publishers.TimeGroupingStrategy<Context>, options: Context.SchedulerOptions?)](publishers/collectbytime/init(upstream:strategy:options:).md)
  Creates a publisher that buffers and periodically publishes its items.
### Declaring Publisher Topography
- [Publishers.CollectByTime.Output](publishers/collectbytime/output.md)
  The kind of values published by this publisher.
- [Publishers.CollectByTime.Failure](publishers/collectbytime/failure.md)
  The kind of errors this publisher might publish.
### Inspecting Publisher Properties
- [let upstream: Upstream](publishers/collectbytime/upstream.md)
  The publisher that this publisher receives elements from.
- [let strategy: Publishers.TimeGroupingStrategy<Context>](publishers/collectbytime/strategy.md)
  The strategy with which to collect and publish elements.
- [let options: Context.SchedulerOptions?](publishers/collectbytime/options.md)
  Scheduler options to use for the strategy.
### Applying Operators
- [Publisher Operators](publishers-collectbytime-publisher-operators.md)
  Methods that create downstream publishers or subscribers to act on the elements they receive.
### Default Implementations
- [Publisher Implementations](publishers/collectbytime/publisher-implementations.md)

## Relationships

### Conforms To
- [Publisher](publisher.md)

## See Also

- [Publishers.Collect](publishers/collect.md)
  A publisher that buffers items.
- [Publishers.CollectByCount](publishers/collectbycount.md)
  A publisher that buffers a maximum number of items.
- [Publishers.TimeGroupingStrategy](publishers/timegroupingstrategy.md)
  A strategy for collecting received elements.
- [Publishers.IgnoreOutput](publishers/ignoreoutput.md)
  A publisher that ignores all upstream elements, but passes along the upstream publisher’s completion state (finished or failed).
- [Publishers.Reduce](publishers/reduce.md)
  A publisher that applies a closure to all received elements and produces an accumulated value when the upstream publisher finishes.
- [Publishers.TryReduce](publishers/tryreduce.md)
  A publisher that applies an error-throwing closure to all received elements and produces an accumulated value when the upstream publisher finishes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/combine/publishers/collectbytime)*