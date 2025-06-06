# restoreUserActivityState(_:)

**Framework**: UIKit  
**Kind**: method

Restores the state needed to continue the given user activity.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
@MainActor
func restoreUserActivityState(_ userActivity: NSUserActivity)
```

#### Discussion

Subclasses override this method to restore the responder’s state with the given user activity. The override should use the state data contained in the `userInfo` dictionary of the given user activity to restore the object.

User activities managed by [`NSDocument`](https://developer.apple.com/documentation/AppKit/NSDocument) can be restored automatically, if [`false`](https://developer.apple.com/documentation/swift/false) is returned from `application:continueActivity:restorationHandler:` or if it’s unimplemented. In this situation, the document is opened by the [`NSDocumentController`](https://developer.apple.com/documentation/AppKit/NSDocumentController) method [`openDocument(withContentsOf:display:completionHandler:)`](https://developer.apple.com/documentation/AppKit/NSDocumentController/openDocument(withContentsOf:display:completionHandler:)) and receives a [`restoreUserActivityState(_:)`](uidocument/restoreuseractivitystate(_:).md) message.

## Parameters

- `userActivity`: The user activity to be continued.

## See Also

- [var userActivity: NSUserActivity?](uidocument/useractivity.md)
  An object encapsulating a user activity supported by this document.
- [func updateUserActivityState(NSUserActivity)](uidocument/updateuseractivitystate(_:).md)
  Updates the state of the given user activity.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uidocument/restoreuseractivitystate(_:))*