# updateUserActivityState(_:)

**Framework**: UIKit  
**Kind**: method

Updates the state of the given user activity.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
@MainActor
func updateUserActivityState(_ userActivity: NSUserActivity)
```

#### Discussion

The default implementation of this method puts the document’s [`fileURL`](https://developer.apple.com/documentation/AppKit/NSDocument/fileURL) into the [`NSUserActivity`](https://developer.apple.com/documentation/Foundation/NSUserActivity) object’s [`userInfo`](https://developer.apple.com/documentation/Foundation/NSUserActivity/userInfo) dictionary with the [`userActivityURLKey`](uidocument/useractivityurlkey.md). [`UIDocument`](uidocument.md) automatically sets the [`needsSave`](https://developer.apple.com/documentation/Foundation/NSUserActivity/needsSave) property of the [`NSUserActivity`](https://developer.apple.com/documentation/Foundation/NSUserActivity) object to [`true`](https://developer.apple.com/documentation/swift/true) when the [`fileURL`](https://developer.apple.com/documentation/AppKit/NSDocument/fileURL) changes.

## Parameters

- `userActivity`: The user activity to be updated.

## See Also

- [var userActivity: NSUserActivity?](uidocument/useractivity.md)
  An object encapsulating a user activity supported by this document.
- [func restoreUserActivityState(NSUserActivity)](uidocument/restoreuseractivitystate(_:).md)
  Restores the state needed to continue the given user activity.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uidocument/updateuseractivitystate(_:))*