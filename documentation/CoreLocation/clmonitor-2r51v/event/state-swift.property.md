# state

**Framework**: Core Location  
**Kind**: property  
**Role**: Instance Property

The event’s state.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+

## Declaration

```swift
var state: CLMonitor.Event.State { get }
```

## See Also

### Event characteristics
- [var date: Date](./date.md)
  A date indicating the time of the event.
- [var identifier: String](./identifier.md)
  A string that identifies the event.
- [let refinement: (any CLCondition)?](./refinement.md)
  An optional instance of a condition that represents the most specific condition that this event can apply to.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corelocation/clmonitor-2r51v/event/state-swift.property)*