# flatMap(maxPublishers:_:)

**Framework**: Swift  
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

Combine‘s `flatMap(maxPublishers:_:)` operator performs a similar function to the [`flatMap(_:)`](Sequence/flatMap(_:)-jo2y.md) operator in the Swift standard library, but turns the elements from one kind of publisher into a new publisher that is sent to subscribers. Use `flatMap(maxPublishers:_:)` when you want to create a new series of events for downstream subscribers based on the received value. The closure creates the new [`Optional.Publisher`](optional/publisher-swift.struct.md) based on the received value. The new [`Optional.Publisher`](optional/publisher-swift.struct.md) can emit more than one event, and successful completion of the new [`Optional.Publisher`](optional/publisher-swift.struct.md) does not complete the overall stream. Failure of the new [`Optional.Publisher`](optional/publisher-swift.struct.md) causes the overall stream to fail.

In the example below, a `PassthroughSubject` publishes `WeatherStation` elements. The `flatMap(maxPublishers:_:)` receives each element, creates a [`URL`](https://developer.apple.com/documentation/Foundation/URL) from it, and produces a new [`URLSession.DataTaskPublisher`](https://developer.apple.com/documentation/Foundation/URLSession/DataTaskPublisher), which will publish the data loaded from that [`URL`](https://developer.apple.com/documentation/Foundation/URL).

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


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/optional/publisher-swift.struct/flatmap(maxpublishers:_:)-6qqrd)*