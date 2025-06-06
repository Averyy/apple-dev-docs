# flatMap(maxPublishers:_:)

**Framework**: RealityKit  
**Kind**: method

Transforms all elements from an upstream publisher into a new publisher up to a maximum number of publishers you specify.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst ?+
- macOS 10.15+
- tvOS 13.0+
- visionOS ?+
- watchOS 6.0+

## Declaration

```swift
func flatMap<T, P>(maxPublishers: Subscribers.Demand = .unlimited, _ transform: @escaping (Self.Output) -> P) -> Publishers.FlatMap<P, Self> where T == P.Output, P : Publisher, Self.Failure == P.Failure
```

#### Return Value

A publisher that transforms elements from an upstream  publisher into a publisher of that element’s type.

#### Discussion

Combine‘s `flatMap(maxPublishers:_:)` operator performs a similar function to the [`flatMap(_:)`](https://developer.apple.com/documentation/Swift/Sequence/flatMap(_:)-jo2y) operator in the Swift standard library, but turns the elements from one kind of publisher into a new publisher that is sent to subscribers. Use `flatMap(maxPublishers:_:)` when you want to create a new series of events for downstream subscribers based on the received value. The closure creates the new [`Scene.Publisher`](scene/publisher.md) based on the received value. The new [`Scene.Publisher`](scene/publisher.md) can emit more than one event, and successful completion of the new [`Scene.Publisher`](scene/publisher.md) does not complete the overall stream. Failure of the new [`Scene.Publisher`](scene/publisher.md) causes the overall stream to fail.

In the example below, a `PassthroughSubject` publishes `WeatherStation` elements. The `flatMap(maxPublishers:_:)` receives each element, creates a [`URL`](https://developer.apple.com/documentation/Foundation/URL) from it, and produces a new [`URLSession.DataTaskPublisher`](https://developer.apple.com/documentation/Foundation/URLSession/DataTaskPublisher), which will publish the data loaded from that [`URL`](https://developer.apple.com/documentation/Foundation/URL).

```None
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

- [func map<T>((Self.Output) -> T) -> Publishers.Map<Self, T>](scene/publisher/map(_:)-6m6k7.md)
  Transforms all elements from the upstream publisher with a provided closure.
- [func tryMap<T>((Self.Output) throws -> T) -> Publishers.TryMap<Self, T>](scene/publisher/trymap(_:).md)
  Transforms all elements from the upstream publisher with a provided error-throwing closure.
- [func mapError<E>((Self.Failure) -> E) -> Publishers.MapError<Self, E>](scene/publisher/maperror(_:).md)
  Converts any failure from the upstream publisher into a new error.
- [func replaceNil<T>(with: T) -> Publishers.Map<Self, T>](scene/publisher/replacenil(with:).md)
  Replaces nil elements in the stream with the provided element.
- [func scan<T>(T, (T, Self.Output) -> T) -> Publishers.Scan<Self, T>](scene/publisher/scan(_:_:).md)
  Transforms elements from the upstream publisher by providing the current element to a closure along with the last value returned by the closure.
- [func tryScan<T>(T, (T, Self.Output) throws -> T) -> Publishers.TryScan<Self, T>](scene/publisher/tryscan(_:_:).md)
  Transforms elements from the upstream publisher by providing the current element to an error-throwing closure along with the last value returned by the closure.
- [func setFailureType<E>(to: E.Type) -> Publishers.SetFailureType<Self, E>](scene/publisher/setfailuretype(to:).md)
  Changes the failure type declared by the upstream publisher.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/scene/publisher/flatmap(maxpublishers:_:)-9f9ie)*