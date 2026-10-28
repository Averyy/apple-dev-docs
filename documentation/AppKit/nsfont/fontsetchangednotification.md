# fontSetChangedNotification

**Framework**: AppKit  
**Kind**: property  
**Role**: Type Property

Posted after the currently-set font changes.

**Availability**:
- macOS

## Declaration

```swift
class let fontSetChangedNotification: NSNotification.Name
```

```c
extern NSNotificationName NSFontSetChangedNotification;
```

## Discussion

To observe this notification using Swift concurrency, use [`NSFont.FontSetChangedMessage`](./fontsetchangedmessage.md).

## See Also

### Responding to Font-Related Notifications
- [class let antialiasThresholdChangedNotification: NSNotification.Name](./antialiasthresholdchangednotification.md)
  Posted after the threshold for antialiasing changes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsfont/fontsetchangednotification)*