# type

**Framework**: EventKit  
**Kind**: property  
**Role**: Instance Property

The type of action to trigger when the alarm fires.

**Availability**:
- macOS 10.8+

## Declaration

```swift
var type: EKAlarmType { get }
```

```objc
@property (nonatomic, readonly) EKAlarmType type;
```

#### Discussion

To set the type of alarm, define one of [`emailAddress`](./emailaddress.md), [`soundName`](./soundname.md), or [`url`](./url.md).

## See Also

### Triggering Alarm Actions
- [enum EKAlarmType](../ekalarmtype.md)
  A value that specifies what type of action occurs when the alarm triggers.
- [var emailAddress: String?](./emailaddress.md)
  The recipient of an email to send when the alarm triggers.
- [var soundName: String?](./soundname.md)
  The name of the sound to play when the alarm triggers.


---

*[View on Apple Developer](https://developer.apple.com/documentation/eventkit/ekalarm/type)*