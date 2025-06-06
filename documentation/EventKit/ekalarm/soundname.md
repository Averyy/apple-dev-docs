# soundName

**Framework**: EventKit  
**Kind**: property

The name of the sound to play when the alarm triggers.

**Availability**:
- macOS 10.8+

## Declaration

```swift
var soundName: String? { get set }
```

## Mentions

- [Setting an alarm](setting-an-alarm.md)

#### Discussion

The value of this property is the name of a system sound that can be used with the [`init(named:)`](https://developer.apple.com/documentation/AppKit/NSSound/init(named:)) class method to create an `NSSound` object. Assigning this property a value will set the [`emailAddress`](ekalarm/emailaddress.md) and [`url`](ekalarm/url.md) properties to `nil`.

## See Also

- [enum EKAlarmType](ekalarmtype.md)
  A value that specifies what type of action occurs when the alarm triggers.
- [var type: EKAlarmType](ekalarm/type.md)
  The type of action to trigger when the alarm fires.
- [var emailAddress: String?](ekalarm/emailaddress.md)
  The recipient of an email to send when the alarm triggers.


---

*[View on Apple Developer](https://developer.apple.com/documentation/eventkit/ekalarm/soundname)*