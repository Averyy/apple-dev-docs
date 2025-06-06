# Publishers.SwitchToLatest

**Framework**: Combine  
**Kind**: struct

A publisher that flattens nested publishers.

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
struct SwitchToLatest<P, Upstream> where P : Publisher, P == Upstream.Output, Upstream : Publisher, P.Failure == Upstream.Failure
```

#### Overview

Given a publisher that publishes [`Publisher`](publisher.md) instances, the [`Publishers.SwitchToLatest`](publishers/switchtolatest.md) publisher produces a sequence of events from only the most recent one. For example, given the type `AnyPublisher<URLSession.DataTaskPublisher, NSError>`, calling `Publisher/switchToLatest()` results in the type `SwitchToLatest<(Data, URLResponse), URLError>`. The downstream subscriber sees a continuous stream of `(Data, URLResponse)` elements from what looks like a single [`URLSession.DataTaskPublisher`](https://developer.apple.com/documentation/Foundation/URLSession/DataTaskPublisher) even though the elements are coming from different upstream publishers.

When [`Publishers.SwitchToLatest`](publishers/switchtolatest.md) receives a new publisher from the upstream publisher, it cancels its previous subscription. Use this feature to prevent earlier publishers from performing unnecessary work, such as creating network request publishers from frequently-updating user interface publishers.

## Topics

### Creating a Switch to Latest Publisher
- [init(upstream: Upstream)](publishers/switchtolatest/init(upstream:).md)
  Creates a publisher that “flattens” nested publishers.
### Declaring Publisher Topography
- [Publishers.SwitchToLatest.Output](publishers/switchtolatest/output.md)
  The kind of values published by this publisher.
- [Publishers.SwitchToLatest.Failure](publishers/switchtolatest/failure.md)
  The kind of errors this publisher might publish.
### Inspecting Publisher Properties
- [let upstream: Upstream](publishers/switchtolatest/upstream.md)
  The publisher from which this publisher receives elements.
### Applying Operators
- [Publisher Operators](publishers-switchtolatest-publisher-operators.md)
  Methods that create downstream publishers or subscribers to act on the elements they receive.
### Default Implementations
- [Publisher Implementations](publishers/switchtolatest/publisher-implementations.md)

## Relationships

### Conforms To
- [Publisher](publisher.md)

## See Also

- [Publishers.FlatMap](publishers/flatmap.md)
  A publisher that transforms elements from an upstream publisher into a new publisher.


---

*[View on Apple Developer](https://developer.apple.com/documentation/combine/publishers/switchtolatest)*