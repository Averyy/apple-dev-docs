# CMPedometerHandler

**Framework**: Core Motion  
**Kind**: typealias

A block for processing pedometer-related data.

**Availability**:
- iOS 4.0+
- iPadOS 4.0+
- Mac Catalyst 13.0+
- macOS 10.15+
- watchOS 2.0+

## Declaration

```swift
typealias CMPedometerHandler = (CMPedometerData?, (any Error)?) -> Void
```

#### Discussion

You provide a block of this type when requesting data from the `CMPedometer` object. When the data becomes available, the pedometer object delivers that data to your block for processing. If there was an error retrieving the data, the pedometer object provides an error object instead.

This block has no return value and takes the following parameters:

## See Also

- [func startUpdates(from: Date, withHandler: CMPedometerHandler)](cmpedometer/startupdates(from:withhandler:).md)
  Starts the delivery of recent pedestrian-related data to your app.
- [func stopUpdates()](cmpedometer/stopupdates.md)
  Stops the delivery of recent pedestrian data updates to your app.
- [func startEventUpdates(handler: CMPedometerEventHandler)](cmpedometer/starteventupdates(handler:).md)
  Starts the delivery of pedometer events to your app.
- [func stopEventUpdates()](cmpedometer/stopeventupdates.md)
  Stops the delivery of pedometer events to your app.
- [typealias CMPedometerEventHandler](cmpedometereventhandler.md)
  A block for processing pedometer events.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremotion/cmpedometerhandler)*