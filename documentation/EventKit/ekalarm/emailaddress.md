# emailAddress

**Framework**: EventKit  
**Kind**: property

The recipient of an email to send when the alarm triggers.

**Availability**:
- macOS 10.8+

## Declaration

```swift
var emailAddress: String? { get set }
```

## Mentions

- [Setting an alarm](setting-an-alarm.md)

#### Discussion

Assigning this property a value will set the [`soundName`](ekalarm/soundname.md) and [`url`](ekalarm/url.md) properties to `nil`.

## See Also

- [enum EKAlarmType](ekalarmtype.md)
  A value that specifies what type of action occurs when the alarm triggers.
- [var type: EKAlarmType](ekalarm/type.md)
  The type of action to trigger when the alarm fires.
- [var soundName: String?](ekalarm/soundname.md)
  The name of the sound to play when the alarm triggers.


---

*[View on Apple Developer](https://developer.apple.com/documentation/eventkit/ekalarm/emailaddress)*