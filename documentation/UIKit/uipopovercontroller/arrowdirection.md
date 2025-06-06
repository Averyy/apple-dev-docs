# arrowDirection

**Framework**: UIKit  
**Kind**: property

The direction of the popover’s arrow.

**Availability**:
- iOS 3.2+
- iPadOS 3.2+
- Mac Catalyst 13.1+
- tvOS ?+

## Declaration

```swift
@MainActor
var arrowDirection: UIPopoverArrowDirection { get }
```

#### Discussion

The default value of this property is [`unknown`](uipopoverarrowdirection/unknown.md). When you present the popover, the value changes to reflect the actual direction of the arrow being used by the popover. When the popover is subsequently dismissed, the value of this property returns to [`unknown`](uipopoverarrowdirection/unknown.md).

## See Also

- [var isPopoverVisible: Bool](uipopovercontroller/ispopovervisible.md)
  A Boolean value indicating whether the popover is currently visible.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uipopovercontroller/arrowdirection)*