# updateUserActivityState(_:)

**Framework**: AppKit  
**Kind**: method

Updates the state of the given user activity.

**Availability**:
- macOS 10.10+

## Declaration

```swift
@MainActor
func updateUserActivityState(_ userActivity: NSUserActivity)
```

#### Discussion

Subclasses override this method to update the state of the supplied `userActivity`. Add state representing the user’s activity into `userActivity` using its [`addUserInfoEntries(from:)`](https://developer.apple.com/documentation/Foundation/NSUserActivity/addUserInfoEntries(from:)) method. When the state is dirty, set the [`needsSave`](https://developer.apple.com/documentation/Foundation/NSUserActivity/needsSave) property to [`true`](https://developer.apple.com/documentation/Swift/true).

When an [`NSUserActivity`](https://developer.apple.com/documentation/Foundation/NSUserActivity) object managed by AppKit is updated, an empty `userInfo` dictionary is given to the user activity, and all of the objects associated with the user activity are sent an [`NSResponder`](nsresponder.md) message.

## Parameters

- `userActivity`: The user activity to be updated.

## See Also

- [class NSResponder](nsresponder.md)
  An abstract class that forms the basis of event and command processing in AppKit.
- [var userActivity: NSUserActivity?](nsresponder/useractivity.md)
  An object encapsulating a user activity supported by this responder.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsresponder/updateuseractivitystate(_:))*