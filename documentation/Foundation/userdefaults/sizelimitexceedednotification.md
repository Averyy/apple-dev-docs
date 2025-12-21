# sizeLimitExceededNotification

**Framework**: Foundation  
**Kind**: property

Posted when the amount of data in the defaults database exceeds the allowed maximum.

**Availability**:
- iOS 9.3+
- iPadOS 9.3+
- Mac Catalyst 13.1+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
class let sizeLimitExceededNotification: NSNotification.Name
```

#### Discussion

In tvOS, the system posts this notification as a warning when the size of your app’s defaults database reaches 512 kilobytes. If your app continues to write to the defaults database, the system terminates your app when the database reaches or exceeds 1 megabyte in size. The system doesn’t post size exceeded notifications for other platforms.

The system posts this notification on your app’s main thread.

## See Also

- [UserDefaults.DidChangeMessage](userdefaults/didchangemessage.md)
- [class let didChangeNotification: NSNotification.Name](userdefaults/didchangenotification.md)
  Posted when the current process changes the value of a setting.
- [UserDefaults.SizeLimitExceededMessage](userdefaults/sizelimitexceededmessage.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/userdefaults/sizelimitexceedednotification)*