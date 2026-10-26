# emailAddress

**Framework**: EventKit  
**Kind**: property  
**Role**: Instance Property

The recipient of an email to send when the alarm triggers.

**Availability**:
- macOS 10.8+

## Declaration

```swift
var emailAddress: String? { get set }
```

```objc
@property (nonatomic, copy, nullable) NSString * emailAddress;
```

## Mentions

- [Setting an alarm](../setting-an-alarm.md)

#### Discussion

Assigning this property a value will set the [`soundName`](./soundname.md) and [`url`](./url.md) properties to `nil`.

## See Also

### Triggering Alarm Actions
- [enum EKAlarmType](../ekalarmtype.md)
  A value that specifies what type of action occurs when the alarm triggers.
- [var type: EKAlarmType](./type.md)
  The type of action to trigger when the alarm fires.
- [var soundName: String?](./soundname.md)
  The name of the sound to play when the alarm triggers.
- [url](./url.md)
  The URL to open when the alarm triggers.


---

*[View on Apple Developer](https://developer.apple.com/documentation/eventkit/ekalarm/emailaddress)*