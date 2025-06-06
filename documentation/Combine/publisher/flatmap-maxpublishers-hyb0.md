# flatMap(maxPublishers:_:)

**Framework**: Combine  
**Kind**: method

Transforms all elements from an upstream publisher into a new publisher up to a maximum number of publishers you specify.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 14.0+
- visionOS 1.0+
- watchOS 7.0+

## Declaration

```swift
func flatMap<P>(maxPublishers: Subscribers.Demand = .unlimited, _ transform: @escaping (Self.Output) -> P) -> Publishers.FlatMap<P, Self> where P : Publisher, P.Failure == Never
```

#### Return Value

A publisher that transforms elements from an upstream  publisher into a publisher of that element’s type.

## Parameters

- `maxPublishers`: Specifies the maximum number of concurrent publisher subscriptions, or   if unspecified.
- `transform`: A closure that takes an element as a parameter and returns a publisher that produces elements of that type.

## See Also

- [func flatMap<T, P>(maxPublishers: Subscribers.Demand, (Self.Output) -> P) -> Publishers.FlatMap<P, Self>](publisher/flatmap(maxpublishers:_:)-3k7z5.md)
  Transforms all elements from an upstream publisher into a new publisher up to a maximum number of publishers you specify.
- [func flatMap<P>(maxPublishers: Subscribers.Demand, (Self.Output) -> P) -> Publishers.FlatMap<P, Publishers.SetFailureType<Self, P.Failure>>](publisher/flatmap(maxpublishers:_:)-qxf.md)
  Transforms all elements from an upstream publisher into a new publisher up to a maximum number of publishers you specify.
- [func flatMap<P>(maxPublishers: Subscribers.Demand, (Self.Output) -> P) -> Publishers.FlatMap<Publishers.SetFailureType<P, Self.Failure>, Self>](publisher/flatmap(maxpublishers:_:)-4of8w.md)
  Transforms all elements from an upstream publisher into a new publisher up to a maximum number of publishers you specify.
- [func switchToLatest() -> Publishers.SwitchToLatest<Self.Output, Self>](publisher/switchtolatest-453ht.md)
  Republishes elements sent by the most recently received publisher.
- [func switchToLatest() -> Publishers.SwitchToLatest<Self.Output, Publishers.SetFailureType<Self, Self.Output.Failure>>](publisher/switchtolatest-1c51y.md)
  Republishes elements sent by the most recently received publisher.
- [func switchToLatest() -> Publishers.SwitchToLatest<Publishers.SetFailureType<Self.Output, Self.Failure>, Publishers.Map<Self, Publishers.SetFailureType<Self.Output, Self.Failure>>>](publisher/switchtolatest-20v3t.md)
  Republishes elements sent by the most recently received publisher.
- [func switchToLatest() -> Publishers.SwitchToLatest<Self.Output, Self>](publisher/switchtolatest-9eb3r.md)
  Republishes elements sent by the most recently received publisher.


---

*[View on Apple Developer](https://developer.apple.com/documentation/combine/publisher/flatmap(maxpublishers:_:)-hyb0)*