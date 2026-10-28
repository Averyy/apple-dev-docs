# url

**Framework**: EventKit  
**Kind**: property  
**Role**: Instance Property

The URL to open when the alarm triggers.

**Availability**:
- macOS 10.8+ - Deprecated in 10.9

## Declaration

```objc
@property (nonatomic, copy, nullable) NSURL * url;
```

## Mentions

- [Setting an alarm](../setting-an-alarm.md)

## Discussion

Assigning this property a value will set the [`emailAddress`](./emailaddress.md) and [`soundName`](./soundname.md) properties to `nil`.

## See Also

### Triggering Alarm Actions
- [enum EKAlarmType](../ekalarmtype.md)
  A value that specifies what type of action occurs when the alarm triggers.
- [var type: EKAlarmType](./type.md)
  The type of action to trigger when the alarm fires.
- [var emailAddress: String?](./emailaddress.md)
  The recipient of an email to send when the alarm triggers.
- [var soundName: String?](./soundname.md)
  The name of the sound to play when the alarm triggers.


---

*[View on Apple Developer](https://developer.apple.com/documentation/eventkit/ekalarm/url)*