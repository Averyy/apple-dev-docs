# Publishers.Reduce

**Framework**: Combine  
**Kind**: struct  
**Role**: Structure

A publisher that applies a closure to all received elements and produces an accumulated value when the upstream publisher finishes.

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
struct Reduce<Upstream, Output> where Upstream : Publisher
```

## Topics

### Creating a reduce publisher
- [init(upstream: Upstream, initial: Output, nextPartialResult: (Output, Upstream.Output) -> Output)](./reduce/init%28upstream,initial,nextpartialresult%29.md)
  Creates a publisher that applies a closure to all received elements and produces an accumulated value when the upstream publisher finishes.
### Declaring supporting types
- [Publishers.Output](./output.md)
  A publisher that publishes elements specified by a range in the sequence of published elements.
- [Publishers.Reduce.Failure](./reduce/failure.md)
  The kind of errors this publisher might publish.
### Inspecting publisher properties
- [let upstream: Upstream](./reduce/upstream.md)
  The publisher from which this publisher receives elements.
- [let initial: Output](./reduce/initial.md)
  The initial value provided on the first invocation of the closure.
- [let nextPartialResult: (Output, Upstream.Output) -> Output](./reduce/nextpartialresult.md)
  A closure that takes the previously-accumulated value and the next element from the upstream publisher to produce a new value.

## Relationships

### Conforms To
- [Publisher](../publisher.md)

## See Also

### Reducing elements
- [Publishers.Collect](./collect.md)
  A publisher that buffers items.
- [Publishers.CollectByCount](./collectbycount.md)
  A publisher that buffers a maximum number of items.
- [Publishers.CollectByTime](./collectbytime.md)
  A publisher that buffers and periodically publishes its items.
- [Publishers.TimeGroupingStrategy](./timegroupingstrategy.md)
  A strategy for collecting received elements.
- [Publishers.IgnoreOutput](./ignoreoutput.md)
  A publisher that ignores all upstream elements, but passes along the upstream publisher’s completion state (finished or failed).
- [Publishers.TryReduce](./tryreduce.md)
  A publisher that applies an error-throwing closure to all received elements and produces an accumulated value when the upstream publisher finishes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/combine/publishers/reduce)*