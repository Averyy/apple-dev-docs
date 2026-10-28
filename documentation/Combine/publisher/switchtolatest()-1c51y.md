# switchToLatest()

**Framework**: Combine  
**Kind**: method  
**Role**: Instance Method

Republishes elements sent by the most recently received publisher.

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
func switchToLatest() -> Publishers.SwitchToLatest<Self.Output, Publishers.SetFailureType<Self, Self.Output.Failure>>
```

Available when `Failure` is `Never` and `Output` conforms to `Publisher`.

## Discussion

This operator works with an upstream publisher of publishers, flattening the stream of elements to appear as if they were coming from a single stream of elements. It switches the inner publisher as new ones arrive but keeps the outer publisher constant for downstream subscribers.

When this operator receives a new publisher from the upstream publisher, it cancels its previous subscription. Use this feature to prevent earlier publishers from performing unnecessary work, such as creating network request publishers from frequently updating user interface publishers.

## See Also

### Republishing elements by subscribing to new publishers
- [func flatMap<T, P>(maxPublishers: Subscribers.Demand, (Self.Output) -> P) -> Publishers.FlatMap<P, Self>](./flatmap%28maxpublishers,_%29-3k7z5.md)
  Transforms all elements from an upstream publisher into a new publisher up to a maximum number of publishers you specify.
- [func flatMap<P>(maxPublishers: Subscribers.Demand, (Self.Output) -> P) -> Publishers.FlatMap<P, Publishers.SetFailureType<Self, P.Failure>>](./flatmap%28maxpublishers,_%29-qxf.md)
  Transforms all elements from an upstream publisher into a new publisher up to a maximum number of publishers you specify.
- [func flatMap<P>(maxPublishers: Subscribers.Demand, (Self.Output) -> P) -> Publishers.FlatMap<P, Self>](./flatmap%28maxpublishers,_%29-hyb0.md)
  Transforms all elements from an upstream publisher into a new publisher up to a maximum number of publishers you specify.
- [func flatMap<P>(maxPublishers: Subscribers.Demand, (Self.Output) -> P) -> Publishers.FlatMap<Publishers.SetFailureType<P, Self.Failure>, Self>](./flatmap%28maxpublishers,_%29-4of8w.md)
  Transforms all elements from an upstream publisher into a new publisher up to a maximum number of publishers you specify.
- [func switchToLatest() -> Publishers.SwitchToLatest<Self.Output, Self>](./switchtolatest%28%29-453ht.md)
  Republishes elements sent by the most recently received publisher.
- [func switchToLatest() -> Publishers.SwitchToLatest<Publishers.SetFailureType<Self.Output, Self.Failure>, Publishers.Map<Self, Publishers.SetFailureType<Self.Output, Self.Failure>>>](./switchtolatest%28%29-20v3t.md)
  Republishes elements sent by the most recently received publisher.
- [func switchToLatest() -> Publishers.SwitchToLatest<Self.Output, Self>](./switchtolatest%28%29-9eb3r.md)
  Republishes elements sent by the most recently received publisher.


---

*[View on Apple Developer](https://developer.apple.com/documentation/combine/publisher/switchtolatest()-1c51y)*