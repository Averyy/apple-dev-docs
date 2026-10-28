# allowsToolTipsWhenApplicationIsInactive

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

A Boolean value that indicates whether the window can display tooltips even when the application is in the background.

**Availability**:
- macOS

## Declaration

```swift
var allowsToolTipsWhenApplicationIsInactive: Bool { get set }
```

```objc
@property BOOL allowsToolTipsWhenApplicationIsInactive;
```

## Discussion

The value of this property is [`true`](../../Swift/true.md) if the window can display tooltips even when the application is in the background; otherwise, [`false`](../../Swift/false.md). The default is [`false`](../../Swift/false.md). Changing the value of this property does not take effect until the window changes to an active state.

> **Note**:  Enabling tooltips in an inactive application will cause the application to do work any time the pointer passes over the window, thus degrading system performance.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nswindow/allowstooltipswhenapplicationisinactive)*