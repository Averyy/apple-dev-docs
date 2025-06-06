# protectedDataDidBecomeAvailableNotification

**Framework**: UIKit  
**Kind**: property

A notification that posts when the protected files become available for your code to access.

**Availability**:
- iOS 4.0+
- iPadOS 4.0+
- Mac Catalyst 13.1+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
nonisolated
class let protectedDataDidBecomeAvailableNotification: NSNotification.Name
```

#### Discussion

This notification does not contain a `userInfo` dictionary.

## See Also

- [var isProtectedDataAvailable: Bool](uiapplication/isprotecteddataavailable.md)
  A Boolean value that indicates whether content protection is active.
- [class let protectedDataWillBecomeUnavailableNotification: NSNotification.Name](uiapplication/protecteddatawillbecomeunavailablenotification.md)
  A notification that posts shortly before protected files are locked down and become inaccessible.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiapplication/protecteddatadidbecomeavailablenotification)*