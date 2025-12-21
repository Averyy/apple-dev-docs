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
func restoreUserActivityState(_ userActivity: NSUserActivity)
```

#### Discussion

Subclasses override this method to restore the responder’s state with the given user activity. The override should use the state data contained in the `userInfo` dictionary of the given user activity to restore the object.

The system can restore user activities that [`UIDocument`](uidocument.md) manages automatically, if you return [`false`](https://developer.apple.com/documentation/Swift/false) from [`application(_:continue:restorationHandler:)`](uiapplicationdelegate/application(_:continue:restorationhandler:).md) or if you don’t implement the method. In this situation, the [`UIDocumentViewController`](uidocumentviewcontroller.md) method [`openDocument(completionHandler:)`](uidocumentviewcontroller/opendocument(completionhandler:).md) opens the document, and calls [`restoreUserActivityState(_:)`](uidocument/restoreuseractivitystate(_:).md).

## Parameters

- `userActivity`: The user activity to be continued.

## See Also

- [var userActivity: NSUserActivity?](uidocument/useractivity.md)
  An object encapsulating a user activity supported by this document.
- [func updateUserActivityState(NSUserActivity)](uidocument/updateuseractivitystate(_:).md)
  Updates the state of the given user activity.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uidocument/restoreuseractivitystate(_:))*