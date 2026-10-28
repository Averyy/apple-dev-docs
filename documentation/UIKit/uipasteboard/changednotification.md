# changedNotification

**Framework**: UIKit  
**Kind**: property  
**Role**: Type Property

A notification that a pasteboard object posts when its contents change.

**Availability**:
- iOS
- iPadOS
- Mac Catalyst
- visionOS

## Declaration

```swift
nonisolated
class let changedNotification: NSNotification.Name
```

```c
extern NSNotificationName const UIPasteboardChangedNotification;
```

## Discussion

This happens at the same time the pasteboard’s change count ([`changeCount`](./changecount.md) property) is incremented. Changes include the addition, removal, and modification of pasteboard items. The `userInfo` dictionary may contain the representation types of pasteboard items that have been added to or removed from the pasteboard. See [UserInfo Dictionary Keys](../userinfo-dictionary-keys.md) for the keys used to access these representation types. If pasteboard items have been modified but not added or removed, the `userInfo` dictionary is `nil`.

## See Also

### Notifications
- [class let removedNotification: NSNotification.Name](./removednotification.md)
  A notification that a pasteboard object posts just before an app removes it.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uipasteboard/changednotification)*