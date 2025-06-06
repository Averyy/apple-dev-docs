# Publishers.TryReduce

**Framework**: Combine  
**Kind**: struct

A publisher that applies an error-throwing closure to all received elements and produces an accumulated value when the upstream publisher finishes.

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
struct TryReduce<Upstream, Output> where Upstream : Publisher
```

## Topics

### Creating a Try Reduce Publisher
- [init(upstream: Upstream, initial: Output, nextPartialResult: (Output, Upstream.Output) throws -> Output)](publishers/tryreduce/init(upstream:initial:nextpartialresult:).md)
  Creates a publisher that applies an error-throwing closure to all received elements and produces an accumulated value when the upstream publisher finishes.
### Declaring Publisher Topography
- [Publishers.Output](publishers/output.md)
  A publisher that publishes elements specified by a range in the sequence of published elements.
- [Publishers.TryReduce.Failure](publishers/tryreduce/failure.md)
  The kind of errors this publisher might publish.
### Inspecting Publisher Properties
- [let upstream: Upstream](publishers/tryreduce/upstream.md)
  The publisher from which this publisher receives elements.
- [let initial: Output](publishers/tryreduce/initial.md)
  The initial value provided on the first-use of the closure.
- [let nextPartialResult: (Output, Upstream.Output) throws -> Output](publishers/tryreduce/nextpartialresult.md)
  An error-throwing closure that takes the previously-accumulated value and the next element from the upstream to produce a new value.
### Applying Operators
- [Publisher Operators](publishers-tryreduce-publisher-operators.md)
  Methods that create downstream publishers or subscribers to act on the elements they receive.
### Default Implementations
- [Publisher Implementations](publishers/tryreduce/publisher-implementations.md)

## Relationships

### Conforms To
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
- [Publishers.IgnoreOutput](publishers/ignoreoutput.md)
  A publisher that ignores all upstream elements, but passes along the upstream publisher’s completion state (finished or failed).
- [Publishers.Reduce](publishers/reduce.md)
  A publisher that applies a closure to all received elements and produces an accumulated value when the upstream publisher finishes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/combine/publishers/tryreduce)*