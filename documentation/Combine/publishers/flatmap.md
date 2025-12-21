# Publishers.FlatMap

**Framework**: Combine  
**Kind**: struct

A publisher that transforms elements from an upstream publisher into a new publisher.

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
struct FlatMap<NewPublisher, Upstream> where NewPublisher : Publisher, Upstream : Publisher, NewPublisher.Failure == Upstream.Failure
```

## Topics

### Creating a flat map Publisher
- [init(upstream: Upstream, maxPublishers: Subscribers.Demand, transform: (Upstream.Output) -> NewPublisher)](publishers/flatmap/init(upstream:maxpublishers:transform:).md)
  Creates a publisher that transforms elements from an upstream publisher into a new publisher.
### Declaring supporting types
- [Publishers.FlatMap.Output](publishers/flatmap/output.md)
  The kind of values published by this publisher.
- [Publishers.FlatMap.Failure](publishers/flatmap/failure.md)
  The kind of errors this publisher might publish.
### Inspecting publisher properties
- [let upstream: Upstream](publishers/flatmap/upstream.md)
  The publisher from which this publisher receives elements.
- [let maxPublishers: Subscribers.Demand](publishers/flatmap/maxpublishers.md)
  The maximum number of concurrent publisher subscriptions
- [let transform: (Upstream.Output) -> NewPublisher](publishers/flatmap/transform.md)
  A closure that takes an element as a parameter and returns a publisher that produces elements of that type.

## Relationships

### Conforms To
- [Publisher](publisher.md)

## See Also

- [Publishers.SwitchToLatest](publishers/switchtolatest.md)
  A publisher that flattens nested publishers.


---

*[View on Apple Developer](https://developer.apple.com/documentation/combine/publishers/flatmap)*