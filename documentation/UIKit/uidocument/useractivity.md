# userActivity

**Framework**: UIKit  
**Kind**: property

An object encapsulating a user activity supported by this document.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
@MainActor
var userActivity: NSUserActivity? { get set }
```

#### Discussion

[`UIDocument`](uidocument.md) automatically creates [`NSUserActivity`](https://developer.apple.com/documentation/Foundation/NSUserActivity) objects. The system makes user activities eligible for Handoff if the document is iCloud-based and the app’s `Info.plist` property list file includes a [`CFBundleDocumentTypes`](https://developer.apple.com/documentation/BundleResources/Information-Property-List/CFBundleDocumentTypes) key of `NSUbiquitousDocumentUserActivityType`. The value of `NSUbiquitousDocumentUserActivityType` is a string that represents the [`NSUserActivity`](https://developer.apple.com/documentation/Foundation/NSUserActivity) object’s activity type. The document’s URL is in the [`NSUserActivity`](https://developer.apple.com/documentation/Foundation/NSUserActivity) object’s [`userInfo`](https://developer.apple.com/documentation/Foundation/NSUserActivity/userInfo) dictionary with the [`userActivityURLKey`](uidocument/useractivityurlkey.md).

In iOS, to make an  [`NSUserActivity`](https://developer.apple.com/documentation/Foundation/NSUserActivity) object that UIKit manages current, you must either call [`becomeCurrent()`](https://developer.apple.com/documentation/Foundation/NSUserActivity/becomeCurrent()) explicitly or have the document’s [`NSUserActivity`](https://developer.apple.com/documentation/Foundation/NSUserActivity) object also set on a [`UIViewController`](uiviewcontroller.md) object that’s in the view hierarchy when the app comes to the foreground.

You can use this property from any thread. It’s KVO-observable in case you share the [`userActivity`](uidocument/useractivity.md) object with other objects that need to be kept in sync as the document moves into and out of iCloud.

## See Also

- [func restoreUserActivityState(NSUserActivity)](uidocument/restoreuseractivitystate(_:).md)
  Restores the state needed to continue the given user activity.
- [func updateUserActivityState(NSUserActivity)](uidocument/updateuseractivitystate(_:).md)
  Updates the state of the given user activity.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uidocument/useractivity)*