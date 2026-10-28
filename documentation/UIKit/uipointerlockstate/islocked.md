# isLocked

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

A Boolean value that indicates whether the pointer is locked.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- visionOS 1.0+

## Declaration

```swift
var isLocked: Bool { get }
```

```objc
@property (nonatomic, readonly, getter=isLocked) BOOL locked;
```

## Discussion

This value reflects the status of the pointer lock for the scene, as determined by the system. A view controller specifies its preferred pointer lock value, but the system may not honor the request.

This property is key-value observable. The [`didChangeNotification`](./didchangenotification.md) is posted when it changes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uipointerlockstate/islocked)*