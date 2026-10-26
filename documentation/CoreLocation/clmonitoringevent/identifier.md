# identifier

**Framework**: Core Location  
**Kind**: property  
**Role**: Instance Property

A string that represents the identifier of a monitored condition.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+

## Declaration

```objc
@property (strong, readonly) NSString * identifier;
```

## See Also

### Event properties
- [date](./date.md)
  The date the event occurs.
- [refinement](./refinement.md)
  An optional instance of a condition that represents the most specific condition to that this event can apply to.
- [state](./state.md)
  The state of the condition at the time of the event.
- [CLMonitoringState](../clmonitoringstate.md)
  Values that represent the current state of a monitoring condition.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corelocation/clmonitoringevent/identifier)*