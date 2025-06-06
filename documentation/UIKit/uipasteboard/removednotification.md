# removedNotification

**Framework**: UIKit  
**Kind**: property

A notification that a pasteboard object posts just before an app removes it.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- visionOS ?+

## Declaration

```swift
nonisolated
class let removedNotification: NSNotification.Name
```

#### Discussion

The removal class method is [`remove(withName:)`](uipasteboard/remove(withname:).md). There is no `userInfo` dictionary.

## See Also

- [class let changedNotification: NSNotification.Name](uipasteboard/changednotification.md)
  A notification that a pasteboard object posts when its contents change.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uipasteboard/removednotification)*