# isProtectedDataAvailable

**Framework**: UIKit  
**Kind**: property

A Boolean value that indicates whether content protection is active.

**Availability**:
- iOS 4.0+
- iPadOS 4.0+
- Mac Catalyst 13.1+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
nonisolated
var isProtectedDataAvailable: Bool { get }
```

#### Discussion

The value of this property is [`false`](https://developer.apple.com/documentation/swift/false) if data protection is enabled and the device is currently locked. The value of this property is set to [`true`](https://developer.apple.com/documentation/swift/true) if the device is unlocked or if content protection is not enabled.

When the value of this property is [`false`](https://developer.apple.com/documentation/swift/false), files that were assigned the [`complete`](https://developer.apple.com/documentation/Foundation/FileProtectionType/complete) or [`completeUnlessOpen`](https://developer.apple.com/documentation/Foundation/FileProtectionType/completeUnlessOpen) protection key cannot be read or written by your app. The user must unlock the device before your app can access them.

## See Also

- [class let protectedDataDidBecomeAvailableNotification: NSNotification.Name](uiapplication/protecteddatadidbecomeavailablenotification.md)
  A notification that posts when the protected files become available for your code to access.
- [class let protectedDataWillBecomeUnavailableNotification: NSNotification.Name](uiapplication/protecteddatawillbecomeunavailablenotification.md)
  A notification that posts shortly before protected files are locked down and become inaccessible.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiapplication/isprotecteddataavailable)*