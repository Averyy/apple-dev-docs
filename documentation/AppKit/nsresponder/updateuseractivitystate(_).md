# updateUserActivityState(_:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Updates the state of the given user activity.

**Availability**:
- macOS 10.10+

## Declaration

```swift
func updateUserActivityState(_ userActivity: NSUserActivity)
```

```objc
- (void) updateUserActivityState:(NSUserActivity *) userActivity;
```

#### Discussion

Subclasses override this method to update the state of the supplied `userActivity`. Add state representing the user’s activity into `userActivity` using its [`addUserInfoEntries(from:)`](../../Foundation/nsuseractivity/adduserinfoentries%28from%29.md) method. When the state is dirty, set the [`needsSave`](../../Foundation/nsuseractivity/needssave.md) property to [`true`](../../Swift/true.md).

When an [`NSUserActivity`](../../Foundation/nsuseractivity.md) object managed by AppKit is updated, an empty `userInfo` dictionary is given to the user activity, and all of the objects associated with the user activity are sent an [`NSResponder`](../nsresponder.md) message.

## Parameters

- `userActivity`: The user activity to be updated.

## See Also

### Related Documentation
- [class NSResponder](../nsresponder.md)
  An abstract class that forms the basis of event and command processing in AppKit.
### Supporting User Activities
- [var userActivity: NSUserActivity?](./useractivity.md)
  An object encapsulating a user activity supported by this responder.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsresponder/updateuseractivitystate(_:))*