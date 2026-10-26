# lastEvent

**Framework**: Core Location  
**Kind**: property  
**Role**: Instance Property

An object that contains the specifics of the most recent event.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+

## Declaration

```objc
@property (strong, readonly) CLMonitoringEvent * lastEvent;
```

#### Discussion

This includes the state, the date, and the specifics of the condition, if applicable.

## See Also

### Event properties
- [condition](./condition.md)
  The condition that the framework is monitoring events for.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corelocation/clmonitoringrecord/lastevent)*