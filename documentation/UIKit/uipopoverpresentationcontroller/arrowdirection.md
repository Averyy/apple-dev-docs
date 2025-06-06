# arrowDirection

**Framework**: UIKit  
**Kind**: property

The arrow direction in use by the popover.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
@MainActor
var arrowDirection: UIPopoverArrowDirection { get }
```

#### Discussion

When the popover is onscreen, this property reflects the actual arrow direction. Before and after presentation, the value of this property is [`unknown`](uipopoverarrowdirection/unknown.md).

## See Also

- [var permittedArrowDirections: UIPopoverArrowDirection](uipopoverpresentationcontroller/permittedarrowdirections.md)
  The arrow directions that you allow for the popover.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uipopoverpresentationcontroller/arrowdirection)*