# type

**Framework**: EventKit  
**Kind**: property

The type of action to trigger when the alarm fires.

**Availability**:
- macOS 10.8+

## Declaration

```swift
var type: EKAlarmType { get }
```

#### Discussion

To set the type of alarm, define one of [`emailAddress`](ekalarm/emailaddress.md), [`soundName`](ekalarm/soundname.md), or [`url`](ekalarm/url.md).

## See Also

- [enum EKAlarmType](ekalarmtype.md)
  A value that specifies what type of action occurs when the alarm triggers.
- [var emailAddress: String?](ekalarm/emailaddress.md)
  The recipient of an email to send when the alarm triggers.
- [var soundName: String?](ekalarm/soundname.md)
  The name of the sound to play when the alarm triggers.


---

*[View on Apple Developer](https://developer.apple.com/documentation/eventkit/ekalarm/type)*