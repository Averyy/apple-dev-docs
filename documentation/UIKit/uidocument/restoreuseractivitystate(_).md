# restoreUserActivityState(_:)

**Framework**: UIKit  
**Kind**: method  
**Role**: Instance Method

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

```objc
- (void) restoreUserActivityState:(NSUserActivity *) userActivity;
```

## Discussion

Subclasses override this method to restore the responder’s state with the given user activity. The override should use the state data contained in the `userInfo` dictionary of the given user activity to restore the object.

The system can restore user activities that [`UIDocument`](../uidocument.md) manages automatically, if you return [`false`](../../Swift/false.md) from [`application(_:continue:restorationHandler:)`](../uiapplicationdelegate/application%28_,continue,restorationhandler%29.md) or if you don’t implement the method. In this situation, the [`UIDocumentViewController`](../uidocumentviewcontroller.md) method [`openDocument(completionHandler:)`](../uidocumentviewcontroller/opendocument%28completionhandler%29.md) opens the document, and calls [`restoreUserActivityState(_:)`](./restoreuseractivitystate%28_%29.md).

## Parameters

- `userActivity`: The user activity to be continued.

## See Also

### Supporting user activities
- [var userActivity: NSUserActivity?](./useractivity.md)
  An object encapsulating a user activity supported by this document.
- [func updateUserActivityState(NSUserActivity)](./updateuseractivitystate%28_%29.md)
  Updates the state of the given user activity.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uidocument/restoreuseractivitystate(_:))*