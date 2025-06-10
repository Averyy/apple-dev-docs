# switchToLatest()

**Framework**: Combine  
**Kind**: method

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

#### Discussion

This operator works with an upstream publisher of publishers, flattening the stream of elements to appear as if they were coming from a single stream of elements. It switches the inner publisher as new ones arrive but keeps the outer publisher constant for downstream subscribers.

When this operator receives a new publisher from the upstream publisher, it cancels its previous subscription. Use this feature to prevent earlier publishers from performing unnecessary work, such as creating network request publishers from frequently updating user interface publishers.

## See Also

- [func flatMap<T, P>(maxPublishers: Subscribers.Demand, (Self.Output) -> P) -> Publishers.FlatMap<P, Self>](publishers/share/flatmap(maxpublishers:_:)-5kr03.md)
  Transforms all elements from an upstream publisher into a new publisher up to a maximum number of publishers you specify.
- [func flatMap<P>(maxPublishers: Subscribers.Demand, (Self.Output) -> P) -> Publishers.FlatMap<P, Publishers.SetFailureType<Self, P.Failure>>](publishers/share/flatmap(maxpublishers:_:)-2xzxz.md)
  Transforms all elements from an upstream publisher into a new publisher up to a maximum number of publishers you specify.
- [func flatMap<P>(maxPublishers: Subscribers.Demand, (Self.Output) -> P) -> Publishers.FlatMap<P, Self>](publishers/share/flatmap(maxpublishers:_:)-7s78j.md)
  Transforms all elements from an upstream publisher into a new publisher up to a maximum number of publishers you specify.
- [func flatMap<P>(maxPublishers: Subscribers.Demand, (Self.Output) -> P) -> Publishers.FlatMap<Publishers.SetFailureType<P, Self.Failure>, Self>](publishers/share/flatmap(maxpublishers:_:)-1fpf1.md)
  Transforms all elements from an upstream publisher into a new publisher up to a maximum number of publishers you specify.


---

*[View on Apple Developer](https://developer.apple.com/documentation/combine/publishers/share/switchtolatest())*