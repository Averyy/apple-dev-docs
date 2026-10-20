# arrowDirection

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

The direction of the popover’s arrow.

**Availability**:
- iOS 3.2+ - Deprecated in 9.0
- iPadOS 3.2+ - Deprecated in 9.0
- Mac Catalyst 13.1+ - Deprecated in 13.1
- tvOS - Deprecated in 9.0

> **Deprecated**: For more information, see [`UIPopoverController`](../uipopovercontroller.md).

## Declaration

```swift
var arrowDirection: UIPopoverArrowDirection { get }
```

```objc
@property (nonatomic, readonly) UIPopoverArrowDirection popoverArrowDirection;
```

#### Discussion

The default value of this property is [`unknown`](../uipopoverarrowdirection/unknown.md). When you present the popover, the value changes to reflect the actual direction of the arrow being used by the popover. When the popover is subsequently dismissed, the value of this property returns to [`unknown`](../uipopoverarrowdirection/unknown.md).

## See Also

### Getting the popover attributes
- [var isPopoverVisible: Bool](./ispopovervisible.md)
  A Boolean value indicating whether the popover is currently visible.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uipopovercontroller/arrowdirection)*