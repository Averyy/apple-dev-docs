# isLocked

**Framework**: UIKit  
**Kind**: property

A Boolean value that indicates whether the pointer is locked.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- visionOS 1.0+

## Declaration

```swift
@MainActor
var isLocked: Bool { get }
```

#### Discussion

This value reflects the status of the pointer lock for the scene, as determined by the system. A view controller specifies its preferred pointer lock value, but the system may not honor the request.

This property is key-value observable. The [`didChangeNotification`](uipointerlockstate/didchangenotification.md) is posted when it changes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uipointerlockstate/islocked)*