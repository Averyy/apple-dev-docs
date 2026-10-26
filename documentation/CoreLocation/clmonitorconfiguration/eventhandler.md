# eventHandler

**Framework**: Core Location  
**Kind**: property  
**Role**: Instance Property

The block the framework calls as the event handler for the location monitor instance.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+

## Declaration

```objc
@property (nonatomic, readonly) void (^eventHandler)(CLMonitor *monitor, CLMonitoringEvent *event);
```

## See Also

### Instance properties
- [name](./name.md)
  The name of the monitor instance.
- [queue](./queue.md)
  The dispatch queue to bind the instance of a location monitor to.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corelocation/clmonitorconfiguration/eventhandler)*