# isPopoverVisible

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

A Boolean value indicating whether the popover is currently visible.

**Availability**:
- iOS 3.2+ - Deprecated in 9.0
- iPadOS 3.2+ - Deprecated in 9.0
- Mac Catalyst 13.1+ - Deprecated in 13.1
- tvOS - Deprecated in 9.0

> **Deprecated**: For more information, see [`UIPopoverController`](../uipopovercontroller.md).

## Declaration

```swift
var isPopoverVisible: Bool { get }
```

```objc
@property (nonatomic, readonly, getter=isPopoverVisible) BOOL popoverVisible;
```

## Discussion

You must present the popover to make it visible.

## See Also

### Getting the popover attributes
- [var arrowDirection: UIPopoverArrowDirection](./arrowdirection.md)
  The direction of the popover’s arrow.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uipopovercontroller/ispopovervisible)*