# didChangeNotification

**Framework**: Foundation  
**Kind**: property

Posted when the current process changes the value of a setting.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.0+
- macOS 10.0+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
class let didChangeNotification: NSNotification.Name
```

## Mentions

- [Accessing settings from your code](accessing-settings-from-your-code.md)

#### Discussion

When you write a new value to a setting, or remove an existing value, the system generates this notification to alert you that your app’s settings changed. Use this notification in other parts of your app to incorporate updated settings. The system posts this notification on the same thread you used to make the change.

If a different process changes your app’s settings, the system doesn’t generate this notification. To detect changes made by another process, register a key-value observer on the [`UserDefaults`](userdefaults.md) object. Key-value observing reports all updates to setting values, regardless of which process made the change.

## See Also

- [UserDefaults.DidChangeMessage](userdefaults/didchangemessage.md)
- [UserDefaults.SizeLimitExceededMessage](userdefaults/sizelimitexceededmessage.md)
- [class let sizeLimitExceededNotification: NSNotification.Name](userdefaults/sizelimitexceedednotification.md)
  Posted when the amount of data in the defaults database exceeds the allowed maximum.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/userdefaults/didchangenotification)*