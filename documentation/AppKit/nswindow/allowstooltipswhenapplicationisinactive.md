# allowsToolTipsWhenApplicationIsInactive

**Framework**: AppKit  
**Kind**: property

A Boolean value that indicates whether the window can display tooltips even when the application is in the background.

**Availability**:
- macOS ?+

## Declaration

```swift
@MainActor
var allowsToolTipsWhenApplicationIsInactive: Bool { get set }
```

#### Discussion

The value of this property is [`true`](https://developer.apple.com/documentation/swift/true) if the window can display tooltips even when the application is in the background; otherwise, [`false`](https://developer.apple.com/documentation/swift/false). The default is [`false`](https://developer.apple.com/documentation/swift/false). Changing the value of this property does not take effect until the window changes to an active state.

> **Note**:  Enabling tooltips in an inactive application will cause the application to do work any time the pointer passes over the window, thus degrading system performance.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nswindow/allowstooltipswhenapplicationisinactive)*