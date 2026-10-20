# CMStepCounter

**Framework**: Core Motion  
**Kind**: class  
**Role**: Class

The number of steps the user has taken with the device.

**Availability**:
- iOS 7.0+ - Deprecated in 8.0
- iPadOS 7.0+ - Deprecated in 8.0
- Mac Catalyst 13.1+ - Deprecated in 13.1
- visionOS 1.0+ - Deprecated in 1.0

> **Deprecated**: Use the [`CMPedometer`](./cmpedometer.md) class instead.

## Declaration

```swift
class CMStepCounter
```

```objc
@interface CMStepCounter : NSObject
```

#### Overview

Step information is gathered on devices with the appropriate built-in hardware and stored so that you can run queries to determine the user’s recent physical activity. You use this class to gather both current step data and any historical data.

## Topics

### Determining Step Counting Availability
- [class func isStepCountingAvailable() -> Bool](./cmstepcounter/isstepcountingavailable%28%29.md)
  Returns a Boolean indicating whether step-counting support is available on the current device.
### Starting and Stopping Step Counting Updates
- [func startStepCountingUpdates(to: OperationQueue, updateOn: Int, withHandler: CMStepUpdateHandler)](./cmstepcounter/startstepcountingupdates%28to,updateon,withhandler%29.md)
  Starts the delivery of current step-counting data to your app.
- [func stopStepCountingUpdates()](./cmstepcounter/stopstepcountingupdates%28%29.md)
  Stops the delivery of step-counting updates to your app.
- [typealias CMStepUpdateHandler](./cmstepupdatehandler.md)
  A block that reports the number of steps recorded since updates began.
### Getting Historical Step Counting Data
- [func queryStepCountStarting(from: Date, to: Date, to: OperationQueue, withHandler: CMStepQueryHandler)](./cmstepcounter/querystepcountstarting%28from,to,to,withhandler%29.md)
  Gathers and returns historical step count data for the specified time period.
- [typealias CMStepQueryHandler](./cmstepqueryhandler.md)
  A block that reports the number of steps for a query operation.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/nsobject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)

## See Also

### Pedometer and fitness
- [class CMPedometer](./cmpedometer.md)
  An object for fetching the system-generated live walking data.
- [class CMPedometerData](./cmpedometerdata.md)
  Information about the distance traveled by a user on foot.
- [class CMPedometerEvent](./cmpedometerevent.md)
  A change in the user’s pedestrian activity.
- [class CMOdometerData](./cmodometerdata.md)
  A class that represents odometer data for workouts.
- [class CMHighFrequencyHeartRateData](./cmhighfrequencyheartratedata.md)
  A class that represents heart rate data collected at 1 Hz.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coremotion/cmstepcounter)*