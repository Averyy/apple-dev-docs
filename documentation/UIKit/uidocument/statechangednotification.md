# stateChangedNotification

**Framework**: UIKit  
**Kind**: property

A notification the document object posts when there’s a change in the state of the document.

**Availability**:
- iOS 5.0+
- iPadOS 5.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
nonisolated
class let stateChangedNotification: NSNotification.Name
```

#### Discussion

When handling this notification, check the value of the [`documentState`](uidocument/documentstate.md) property to see what the new state is, and then proceed accordingly. There’s no `userInfo` dictionary.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uidocument/statechangednotification)*