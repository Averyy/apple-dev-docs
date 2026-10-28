# userActivity

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

An object encapsulating a user activity supported by this document.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
var userActivity: NSUserActivity? { get set }
```

```objc
@property (nonatomic, strong, nullable) NSUserActivity * userActivity;
```

## Discussion

[`UIDocument`](../uidocument.md) automatically creates [`NSUserActivity`](../../Foundation/nsuseractivity.md) objects. The system makes user activities eligible for Handoff if the document is iCloud-based and the app’s `Info.plist` property list file includes a [`CFBundleDocumentTypes`](../../BundleResources/information-property-list/cfbundledocumenttypes.md) key of `NSUbiquitousDocumentUserActivityType`. The value of `NSUbiquitousDocumentUserActivityType` is a string that represents the [`NSUserActivity`](../../Foundation/nsuseractivity.md) object’s activity type. The document’s URL is in the [`NSUserActivity`](../../Foundation/nsuseractivity.md) object’s [`userInfo`](../../Foundation/nsuseractivity/userinfo.md) dictionary with the [`userActivityURLKey`](./useractivityurlkey.md).

In iOS, to make an  [`NSUserActivity`](../../Foundation/nsuseractivity.md) object that UIKit manages current, you must either call [`becomeCurrent()`](../../Foundation/nsuseractivity/becomecurrent%28%29.md) explicitly or have the document’s [`NSUserActivity`](../../Foundation/nsuseractivity.md) object also set on a [`UIViewController`](../uiviewcontroller.md) object that’s in the view hierarchy when the app comes to the foreground.

You can use this property from any thread. It’s KVO-observable in case you share the [`userActivity`](./useractivity.md) object with other objects that need to be kept in sync as the document moves into and out of iCloud.

## See Also

### Supporting user activities
- [func restoreUserActivityState(NSUserActivity)](./restoreuseractivitystate%28_%29.md)
  Restores the state needed to continue the given user activity.
- [func updateUserActivityState(NSUserActivity)](./updateuseractivitystate%28_%29.md)
  Updates the state of the given user activity.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uidocument/useractivity)*