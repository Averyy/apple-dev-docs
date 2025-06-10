# userActivity

**Framework**: AppKit  
**Kind**: property

An object that encapsulates a user activity the document supports.

**Availability**:
- macOS 10.10+

## Declaration

```swift
@MainActor
var userActivity: NSUserActivity? { get set }
```

#### Discussion

[`NSDocument`](nsdocument.md) automatically creates [`NSUserActivity`](https://developer.apple.com/documentation/Foundation/NSUserActivity) objects. The system makes user activities eligible for Handoff if the document is iCloud-based and the app’s `Info.plist` property list file includes a `CFBundleDocumentTypes` key of `NSUbiquitousDocumentUserActivityType`. The value of `NSUbiquitousDocumentUserActivityType` is a string that represents the [`NSUserActivity`](https://developer.apple.com/documentation/Foundation/NSUserActivity) object’s activity type. The document’s URL is in the [`NSUserActivity`](https://developer.apple.com/documentation/Foundation/NSUserActivity) object’s [`userInfo`](https://developer.apple.com/documentation/Foundation/NSUserActivity/userInfo) dictionary with the [`NSUserActivityDocumentURLKey`](nsuseractivitydocumenturlkey.md).

In macOS, [`NSUserActivity`](https://developer.apple.com/documentation/Foundation/NSUserActivity) objects that [`NSDocument`](nsdocument.md) manage automatically become current when any of the document window controller’s windows become main. Otherwise, you need to invoke [`becomeCurrent()`](https://developer.apple.com/documentation/Foundation/NSUserActivity/becomeCurrent()) at appropriate times.

AppKit automatically invalidates any [`NSUserActivity`](https://developer.apple.com/documentation/Foundation/NSUserActivity) objects that have no associated documents or responders.

You can use this property from any thread. It’s KVO-observable in case you share the [`NSDocument`](nsdocument.md) object with other objects that need to be in sync as the document moves into and out of iCloud.

## See Also

- [class NSDocument](nsdocument.md)
  An abstract class that defines the interface for macOS documents.
- [func updateUserActivityState(NSUserActivity)](nsdocument/updateuseractivitystate(_:).md)
  Updates the state of the given user activity.
- [let NSUserActivityDocumentURLKey: String](nsuseractivitydocumenturlkey.md)
  The key that identifies the document associated with a user activity.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsdocument/useractivity)*