# CLMonitoringRecord

**Framework**: Core Location  
**Kind**: class  
**Role**: Class

An object that represents a condition and its associated information that a location monitor is monitoring.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+

## Declaration

```objc
@interface CLMonitoringRecord : NSObject
```

#### Overview

When handling a new [`CLMonitoringEvent`](./clmonitoringevent.md), the `CLMonitoringRecord` available for the indicated identifier from the [`CLMonitor`](./clmonitor-2r51v.md) contains the prior event. The `CLMonitoringRecord` updates with the new event when the handling is complete.

## Topics

### Event properties
- [condition](./clmonitoringrecord/condition.md)
  The condition that the framework is monitoring events for.
- [lastEvent](./clmonitoringrecord/lastevent.md)
  An object that contains the specifics of the most recent event.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/nsobject-swift.class.md)
### Conforms To
- [NSSecureCoding](../Foundation/nssecurecoding.md)

## See Also

### Location monitor events
- [CLMonitoringEvent](./clmonitoringevent.md)
  The object that the framework passes to the monitor’s callback handler upon receiving an event.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corelocation/clmonitoringrecord)*