# CLMonitorConfiguration

**Framework**: Core Location  
**Kind**: class  
**Role**: Class

An object for configuring a location monitor instance.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+

## Declaration

```objc
@interface CLMonitorConfiguration : NSObject
```

## Topics

### Creating a monitor configuration
- [+ configWithMonitorName:queue:eventHandler:](./clmonitorconfiguration/configwithmonitorname_queue_eventhandler_.md)
  Creates a location monitor instance with the name, dispatch queue, and event handler you specify.
### Instance properties
- [eventHandler](./clmonitorconfiguration/eventhandler.md)
  The block the framework calls as the event handler for the location monitor instance.
- [name](./clmonitorconfiguration/name.md)
  The name of the monitor instance.
- [queue](./clmonitorconfiguration/queue.md)
  The dispatch queue to bind the instance of a location monitor to.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/nsobject-swift.class.md)

## See Also

### Creating a monitor
- [+ requestMonitorWithConfiguration:completion:](./clmonitor-6ynwz/requestmonitorwithconfiguration_completion_.md)
  Creates a location monitor with the configuration and event handler you provide.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corelocation/clmonitorconfiguration)*