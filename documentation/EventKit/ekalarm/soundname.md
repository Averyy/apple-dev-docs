# soundName

**Framework**: EventKit  
**Kind**: property  
**Role**: Instance Property

The name of the sound to play when the alarm triggers.

**Availability**:
- macOS 10.8+

## Declaration

```swift
var soundName: String? { get set }
```

```objc
@property (nonatomic, copy, nullable) NSString * soundName;
```

## Mentions

- [Setting an alarm](../setting-an-alarm.md)

#### Discussion

The value of this property is the name of a system sound that can be used with the [`init(named:)`](../../AppKit/nssound/init%28named%29.md) class method to create an `NSSound` object. Assigning this property a value will set the [`emailAddress`](./emailaddress.md) and [`url`](./url.md) properties to `nil`.

## See Also

### Triggering Alarm Actions
- [enum EKAlarmType](../ekalarmtype.md)
  A value that specifies what type of action occurs when the alarm triggers.
- [var type: EKAlarmType](./type.md)
  The type of action to trigger when the alarm fires.
- [var emailAddress: String?](./emailaddress.md)
  The recipient of an email to send when the alarm triggers.


---

*[View on Apple Developer](https://developer.apple.com/documentation/eventkit/ekalarm/soundname)*