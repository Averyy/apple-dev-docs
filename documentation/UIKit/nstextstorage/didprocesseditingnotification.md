# didProcessEditingNotification

**Framework**: UIKit  
**Kind**: property

A notification that posts after a text storage finishes processing edits.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst 13.1+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
class let didProcessEditingNotification: NSNotification.Name
```

#### Discussion

The framework posts this notification after a text storage finishes processing edits in [`processEditing()`](nstextstorage/processediting().md). Observers other than the delegate shouldn’t make further changes to the text storage. The notification object is the text storage object that processed the edits. This notification doesn’t contain a `userInfo` dictionary.

## See Also

- [class let willProcessEditingNotification: NSNotification.Name](nstextstorage/willprocesseditingnotification.md)
  A notification that posts before a text storage begins processing edits.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/nstextstorage/didprocesseditingnotification)*