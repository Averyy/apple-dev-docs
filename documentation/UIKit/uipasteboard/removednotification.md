# removedNotification

**Framework**: UIKit  
**Kind**: property  
**Role**: Type Property

A notification that a pasteboard object posts just before an app removes it.

**Availability**:
- iOS
- iPadOS
- Mac Catalyst
- visionOS

## Declaration

```swift
nonisolated
class let removedNotification: NSNotification.Name
```

```c
extern NSNotificationName const UIPasteboardRemovedNotification;
```

#### Discussion

The removal class method is [`remove(withName:)`](./remove%28withname%29.md). There is no `userInfo` dictionary.

## See Also

### Notifications
- [class let changedNotification: NSNotification.Name](./changednotification.md)
  A notification that a pasteboard object posts when its contents change.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uipasteboard/removednotification)*