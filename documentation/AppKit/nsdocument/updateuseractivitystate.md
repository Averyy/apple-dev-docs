# updateUserActivityState(_:)

**Framework**: AppKit  
**Kind**: method

Updates the state of the given user activity.

**Availability**:
- macOS 10.10+

## Declaration

```swift
@MainActor
func updateUserActivityState(_ activity: NSUserActivity)
```

#### Discussion

The default implementation of this method puts the document’s [`fileURL`](nsdocument/fileurl.md) into the [`NSUserActivity`](https://developer.apple.com/documentation/Foundation/NSUserActivity) object’s [`userInfo`](https://developer.apple.com/documentation/foundation/nsuseractivity/1411706-userinfo) dictionary with the [`NSUserActivityDocumentURLKey`](nsuseractivitydocumenturlkey.md). [`NSDocument`](nsdocument.md) automatically sets the [`needsSave`](https://developer.apple.com/documentation/foundation/nsuseractivity/1408791-needssave) property of the [`NSUserActivity`](https://developer.apple.com/documentation/Foundation/NSUserActivity) to [`true`](https://developer.apple.com/documentation/swift/true) when the [`fileURL`](nsdocument/fileurl.md) changes.

## Parameters

- `activity`: The user activity to be updated.

## See Also

- [class NSDocument](nsdocument.md)
  An abstract class that defines the interface for macOS documents.
- [var userActivity: NSUserActivity?](nsdocument/useractivity.md)
  An object that encapsulates a user activity the document supports.
- [let NSUserActivityDocumentURLKey: String](nsuseractivitydocumenturlkey.md)
  The key that identifies the document associated with a user activity.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsdocument/updateuseractivitystate(_:))*