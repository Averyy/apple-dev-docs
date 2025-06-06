# flatMap(maxPublishers:_:)

**Framework**: Combine  
**Kind**: method

Transforms all elements from an upstream publisher into a new publisher up to a maximum number of publishers you specify.

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
func flatMap<T, P>(maxPublishers: Subscribers.Demand = .unlimited, _ transform: @escaping (Self.Output) -> P) -> Publishers.FlatMap<P, Self> where T == P.Output, P : Publisher, Self.Failure == P.Failure
```

#### Return Value

A publisher that transforms elements from an upstream  publisher into a publisher of that element’s type.

#### Discussion

Combine‘s `flatMap(maxPublishers:_:)` operator performs a similar function to the [`flatMap(_:)`](https://developer.apple.com/documentation/Swift/Sequence/flatMap(_:)-jo2y) operator in the Swift standard library, but turns the elements from one kind of publisher into a new publisher that is sent to subscribers. Use `flatMap(maxPublishers:_:)` when you want to create a new series of events for downstream subscribers based on the received value. The closure creates the new [`Published.Publisher`](published/publisher.md) based on the received value. The new [`Published.Publisher`](published/publisher.md) can emit more than one event, and successful completion of the new [`Published.Publisher`](published/publisher.md) does not complete the overall stream. Failure of the new [`Published.Publisher`](published/publisher.md) causes the overall stream to fail.

In the example below, a [`PassthroughSubject`](passthroughsubject.md) publishes `WeatherStation` elements. The `flatMap(maxPublishers:_:)` receives each element, creates a [`URL`](https://developer.apple.com/documentation/Foundation/URL) from it, and produces a new [`URLSession.DataTaskPublisher`](https://developer.apple.com/documentation/Foundation/URLSession/DataTaskPublisher), which will publish the data loaded from that [`URL`](https://developer.apple.com/documentation/Foundation/URL).

```swift
public struct WeatherStation {
    public let stationID: String
}

var weatherPublisher = PassthroughSubject<WeatherStation, URLError>()

cancellable = weatherPublisher.flatMap { station -> URLSession.DataTaskPublisher in
    let url = URL(string:"https://weatherapi.example.com/stations/\(station.stationID)/observations/latest")!
    return URLSession.shared.dataTaskPublisher(for: url)
}
.sink(
    receiveCompletion: { completion in
        // Handle publisher completion (normal or error).
    },
    receiveValue: {
        // Process the received data.
    }
 )

weatherPublisher.send(WeatherStation(stationID: "KSFO")) // San Francisco, CA
weatherPublisher.send(WeatherStation(stationID: "EGLC")) // London, UK
weatherPublisher.send(WeatherStation(stationID: "ZBBB")) // Beijing, CN
```

## Parameters

- `maxPublishers`: Specifies the maximum number of concurrent publisher subscriptions, or   if unspecified.
- `transform`: A closure that takes an element as a parameter and returns a publisher that produces elements of that type.

## See Also

- [func flatMap<P>(maxPublishers: Subscribers.Demand, (Self.Output) -> P) -> Publishers.FlatMap<P, Publishers.SetFailureType<Self, P.Failure>>](published/publisher/flatmap(maxpublishers:_:)-4z3ke.md)
  Transforms all elements from an upstream publisher into a new publisher up to a maximum number of publishers you specify.
- [func flatMap<P>(maxPublishers: Subscribers.Demand, (Self.Output) -> P) -> Publishers.FlatMap<P, Self>](published/publisher/flatmap(maxpublishers:_:)-85rt8.md)
  Transforms all elements from an upstream publisher into a new publisher up to a maximum number of publishers you specify.
- [func flatMap<P>(maxPublishers: Subscribers.Demand, (Self.Output) -> P) -> Publishers.FlatMap<Publishers.SetFailureType<P, Self.Failure>, Self>](published/publisher/flatmap(maxpublishers:_:)-1zz14.md)
  Transforms all elements from an upstream publisher into a new publisher up to a maximum number of publishers you specify.
- [func switchToLatest() -> Publishers.SwitchToLatest<Self.Output, Publishers.SetFailureType<Self, Self.Output.Failure>>](published/publisher/switchtolatest.md)
  Republishes elements sent by the most recently received publisher.


---

*[View on Apple Developer](https://developer.apple.com/documentation/combine/published/publisher/flatmap(maxpublishers:_:)-5miz8)*