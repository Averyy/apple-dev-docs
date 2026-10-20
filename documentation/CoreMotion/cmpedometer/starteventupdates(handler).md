# startEventUpdates(handler:)

**Framework**: Core Motion  
**Kind**: method  
**Role**: Instance Method

Starts the delivery of pedometer events to your app.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- watchOS 3.0+

## Declaration

```swift
func startEventUpdates(handler: @escaping CMPedometerEventHandler)
```

```objc
- (void) startPedometerEventUpdatesWithHandler:(CMPedometerEventHandler) handler;
```

#### Discussion

Pedometer events report changes in the user’s pedestrian activity.

## Parameters

- `handler`: The block to execute when a pedometer event is available. This parameter must not be `nil`.

## See Also

### Gathering Live Pedometer Data
- [func startUpdates(from: Date, withHandler: CMPedometerHandler)](./startupdates%28from,withhandler%29.md)
  Starts the delivery of recent pedestrian-related data to your app.
- [func stopUpdates()](./stopupdates%28%29.md)
  Stops the delivery of recent pedestrian data updates to your app.
- [func stopEventUpdates()](./stopeventupdates%28%29.md)
  Stops the delivery of pedometer events to your app.
- [typealias CMPedometerHandler](../cmpedometerhandler.md)
  A block for processing pedometer-related data.
- [typealias CMPedometerEventHandler](../cmpedometereventhandler.md)
  A block for processing pedometer events.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremotion/cmpedometer/starteventupdates(handler:))*