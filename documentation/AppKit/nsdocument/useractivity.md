# userActivity

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

An object that encapsulates a user activity the document supports.

**Availability**:
- macOS 10.10+

## Declaration

```swift
var userActivity: NSUserActivity? { get set }
```

```objc
@property (strong, nullable) NSUserActivity * userActivity;
```

#### Discussion

[`NSDocument`](../nsdocument.md) automatically creates [`NSUserActivity`](../../Foundation/nsuseractivity.md) objects. The system makes user activities eligible for Handoff if the document is iCloud-based and the app’s `Info.plist` property list file includes a `CFBundleDocumentTypes` key of `NSUbiquitousDocumentUserActivityType`. The value of `NSUbiquitousDocumentUserActivityType` is a string that represents the [`NSUserActivity`](../../Foundation/nsuseractivity.md) object’s activity type. The document’s URL is in the [`NSUserActivity`](../../Foundation/nsuseractivity.md) object’s [`userInfo`](../../Foundation/nsuseractivity/userinfo.md) dictionary with the [`NSUserActivityDocumentURLKey`](../nsuseractivitydocumenturlkey.md).

In macOS, [`NSUserActivity`](../../Foundation/nsuseractivity.md) objects that [`NSDocument`](../nsdocument.md) manage automatically become current when any of the document window controller’s windows become main. Otherwise, you need to invoke [`becomeCurrent()`](../../Foundation/nsuseractivity/becomecurrent%28%29.md) at appropriate times.

AppKit automatically invalidates any [`NSUserActivity`](../../Foundation/nsuseractivity.md) objects that have no associated documents or responders.

You can use this property from any thread. It’s KVO-observable in case you share the [`NSDocument`](../nsdocument.md) object with other objects that need to be in sync as the document moves into and out of iCloud.

## See Also

### Related Documentation
- [class NSDocument](../nsdocument.md)
  An abstract class that defines the interface for macOS documents.
### Supporting User Activities
- [func updateUserActivityState(NSUserActivity)](./updateuseractivitystate%28_%29.md)
  Updates the state of the given user activity.
- [let NSUserActivityDocumentURLKey: String](../nsuseractivitydocumenturlkey.md)
  The key that identifies the document associated with a user activity.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsdocument/useractivity)*