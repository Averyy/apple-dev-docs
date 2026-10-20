# updateUserActivityState(_:)

**Framework**: UIKit  
**Kind**: method  
**Role**: Instance Method

Updates the state of the given user activity.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
func updateUserActivityState(_ userActivity: NSUserActivity)
```

```objc
- (void) updateUserActivityState:(NSUserActivity *) userActivity;
```

#### Discussion

The default implementation of this method puts the document’s [`fileURL`](./fileurl.md) into the [`NSUserActivity`](../../Foundation/nsuseractivity.md) object’s [`userInfo`](../../Foundation/nsuseractivity/userinfo.md) dictionary with the [`userActivityURLKey`](./useractivityurlkey.md). [`UIDocument`](../uidocument.md) automatically sets the [`needsSave`](../../Foundation/nsuseractivity/needssave.md) property of the [`NSUserActivity`](../../Foundation/nsuseractivity.md) object to [`true`](../../Swift/true.md) when the [`fileURL`](./fileurl.md) changes.

## Parameters

- `userActivity`: The user activity to be updated.

## See Also

### Supporting user activities
- [var userActivity: NSUserActivity?](./useractivity.md)
  An object encapsulating a user activity supported by this document.
- [func restoreUserActivityState(NSUserActivity)](./restoreuseractivitystate%28_%29.md)
  Restores the state needed to continue the given user activity.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uidocument/updateuseractivitystate(_:))*