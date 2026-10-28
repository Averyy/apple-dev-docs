# name

**Framework**: Core Location  
**Kind**: property  
**Role**: Instance Property

The name of the monitor instance.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+

## Declaration

```objc
@property (readonly) NSString * name;
```

## Discussion

`name` can contain only alphanumeric characters and can’t start with an underscore (_).

## See Also

### Instance properties
- [eventHandler](./eventhandler.md)
  The block the framework calls as the event handler for the location monitor instance.
- [queue](./queue.md)
  The dispatch queue to bind the instance of a location monitor to.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corelocation/clmonitorconfiguration/name)*