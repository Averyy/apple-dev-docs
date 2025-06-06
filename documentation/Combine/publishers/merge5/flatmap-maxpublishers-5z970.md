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
func flatMap<P>(maxPublishers: Subscribers.Demand = .unlimited, _ transform: @escaping (Self.Output) -> P) -> Publishers.FlatMap<P, Publishers.SetFailureType<Self, P.Failure>> where P : Publisher
```

#### Return Value

A publisher that transforms elements from an upstream  publisher into a publisher of that element’s type.

## Parameters

- `maxPublishers`: Specifies the maximum number of concurrent publisher subscriptions, or   if unspecified.
- `transform`: A closure that takes an element as a parameter and returns a publisher that produces elements of that type.

## See Also

- [func flatMap<T, P>(maxPublishers: Subscribers.Demand, (Self.Output) -> P) -> Publishers.FlatMap<P, Self>](publishers/merge5/flatmap(maxpublishers:_:)-90vph.md)
  Transforms all elements from an upstream publisher into a new publisher up to a maximum number of publishers you specify.
- [func flatMap<P>(maxPublishers: Subscribers.Demand, (Self.Output) -> P) -> Publishers.FlatMap<P, Self>](publishers/merge5/flatmap(maxpublishers:_:)-2iern.md)
  Transforms all elements from an upstream publisher into a new publisher up to a maximum number of publishers you specify.
- [func flatMap<P>(maxPublishers: Subscribers.Demand, (Self.Output) -> P) -> Publishers.FlatMap<Publishers.SetFailureType<P, Self.Failure>, Self>](publishers/merge5/flatmap(maxpublishers:_:)-9u04v.md)
  Transforms all elements from an upstream publisher into a new publisher up to a maximum number of publishers you specify.
- [func switchToLatest() -> Publishers.SwitchToLatest<Self.Output, Publishers.SetFailureType<Self, Self.Output.Failure>>](publishers/merge5/switchtolatest.md)
  Republishes elements sent by the most recently received publisher.


---

*[View on Apple Developer](https://developer.apple.com/documentation/combine/publishers/merge5/flatmap(maxpublishers:_:)-5z970)*