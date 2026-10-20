# CMPedometerEventHandler

**Framework**: Core Motion  
**Kind**: typealias  
**Role**: Type Alias

A block for processing pedometer events.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- macOS 10.15+
- watchOS 3.0+

## Declaration

```swift
typealias CMPedometerEventHandler = (CMPedometerEvent?, (any Error)?) -> Void
```

```c
typedef void (^)(CMPedometerEvent *, NSError *) CMPedometerEventHandler;
```

#### Discussion

You provide a block of this type when requesting pedometer events from a [`CMPedometer`](./cmpedometer.md) object. When a new event becomes available, the pedometer object delivers that data to your block for processing. If there was an error retrieving the data, the pedometer object provides an error object instead.

This block has no return value and takes the following parameters.

- **`pedometerEvent`**: A [`CMPedometerEvent`](./cmpedometerevent.md) object containing the event information. If there was an error retrieving the data, this parameter is nil.
- **`error`**: An [`NSError`](../Foundation/nserror.md) object if there was a problem or `nil` if the pedometer event was retrieved successfully.

## See Also

### Gathering Live Pedometer Data
- [func startUpdates(from: Date, withHandler: CMPedometerHandler)](./cmpedometer/startupdates%28from,withhandler%29.md)
  Starts the delivery of recent pedestrian-related data to your app.
- [func stopUpdates()](./cmpedometer/stopupdates%28%29.md)
  Stops the delivery of recent pedestrian data updates to your app.
- [func startEventUpdates(handler: CMPedometerEventHandler)](./cmpedometer/starteventupdates%28handler%29.md)
  Starts the delivery of pedometer events to your app.
- [func stopEventUpdates()](./cmpedometer/stopeventupdates%28%29.md)
  Stops the delivery of pedometer events to your app.
- [typealias CMPedometerHandler](./cmpedometerhandler.md)
  A block for processing pedometer-related data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremotion/cmpedometereventhandler)*