# willProcessEditingNotification

**Framework**: AppKit  
**Kind**: property  
**Role**: Type Property

A notification that posts before a text storage begins processing edits.

**Availability**:
- macOS 10.0+

## Declaration

```swift
class let willProcessEditingNotification: NSNotification.Name
```

```c
extern NSNotificationName NSTextStorageWillProcessEditingNotification;
```

#### Discussion

The framework posts this notification before a text storage begins processing edits in [`processEditing()`](./processediting%28%29.md). Observers other than the delegate shouldn’t make further changes to the text storage. The notification object is the text storage object that’s about to process the edits. This notification doesn’t contain a `userInfo` dictionary.

## See Also

### Notifications
- [class let didProcessEditingNotification: NSNotification.Name](./didprocesseditingnotification.md)
  A notification that posts after a text storage finishes processing edits.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstextstorage/willprocesseditingnotification)*