# stopUpdates()

**Framework**: Core Motion  
**Kind**: method

Stops the delivery of recent pedestrian data updates to your app.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.15+
- watchOS 2.0+

## Declaration

```swift
func stopUpdates()
```

#### Discussion

Use this method to stop the delivery of continuous updates that were initiated by a call to the [`startUpdates(from:withHandler:)`](cmpedometer/startupdates(from:withhandler:).md) method.

## See Also

- [func startUpdates(from: Date, withHandler: CMPedometerHandler)](cmpedometer/startupdates(from:withhandler:).md)
  Starts the delivery of recent pedestrian-related data to your app.
- [func startEventUpdates(handler: CMPedometerEventHandler)](cmpedometer/starteventupdates(handler:).md)
  Starts the delivery of pedometer events to your app.
- [func stopEventUpdates()](cmpedometer/stopeventupdates.md)
  Stops the delivery of pedometer events to your app.
- [typealias CMPedometerHandler](cmpedometerhandler.md)
  A block for processing pedometer-related data.
- [typealias CMPedometerEventHandler](cmpedometereventhandler.md)
  A block for processing pedometer events.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremotion/cmpedometer/stopupdates())*