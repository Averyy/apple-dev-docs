# updateUserActivityState(_:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Updates the state of the given user activity.

**Availability**:
- macOS 10.10+

## Declaration

```swift
func updateUserActivityState(_ activity: NSUserActivity)
```

```objc
- (void) updateUserActivityState:(NSUserActivity *) activity;
```

#### Discussion

The default implementation of this method puts the document’s [`fileURL`](./fileurl.md) into the [`NSUserActivity`](../../Foundation/nsuseractivity.md) object’s [`userInfo`](../../Foundation/nsuseractivity/userinfo.md) dictionary with the [`NSUserActivityDocumentURLKey`](../nsuseractivitydocumenturlkey.md). [`NSDocument`](../nsdocument.md) automatically sets the [`needsSave`](../../Foundation/nsuseractivity/needssave.md) property of the [`NSUserActivity`](../../Foundation/nsuseractivity.md) to [`true`](../../Swift/true.md) when the [`fileURL`](./fileurl.md) changes.

## Parameters

- `activity`: The user activity to be updated.

## See Also

### Related Documentation
- [class NSDocument](../nsdocument.md)
  An abstract class that defines the interface for macOS documents.
### Supporting User Activities
- [var userActivity: NSUserActivity?](./useractivity.md)
  An object that encapsulates a user activity the document supports.
- [let NSUserActivityDocumentURLKey: String](../nsuseractivitydocumenturlkey.md)
  The key that identifies the document associated with a user activity.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsdocument/updateuseractivitystate(_:))*