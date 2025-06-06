# accessibilityFrameInContainerSpace

**Framework**: UIKit  
**Kind**: property

The frame of the accessibility element, in the coordinate space of its container view.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- tvOS 10.0+
- visionOS 1.0+

## Declaration

```swift
@MainActor
var accessibilityFrameInContainerSpace: CGRect { get set }
```

#### Discussion

The default value of this property is [`CGRectNull`](https://developer.apple.com/documentation/CoreGraphics/CGRectNull). Use this property to set the frame rectangle of an element whose frame rectangle could be affected by its container view. For example, use this property to set the frame rectangle for an element in a scroll view’s content view. Changing the value of this property automatically adjusts the rectangle in the [`accessibilityFrame`](uiaccessibilityelement/accessibilityframe.md) property.

## See Also

- [var accessibilityLabel: String?](uiaccessibilityelement/accessibilitylabel.md)
  A string that succinctly identifies the accessibility element.
- [var accessibilityHint: String?](uiaccessibilityelement/accessibilityhint.md)
  A string that briefly describes the result of performing an action on the accessibility element.
- [var accessibilityValue: String?](uiaccessibilityelement/accessibilityvalue.md)
  A string that represents the current value of the accessibility element.
- [var accessibilityFrame: CGRect](uiaccessibilityelement/accessibilityframe.md)
  The frame of the accessibility element, in screen coordinates.
- [var accessibilityTraits: UIAccessibilityTraits](uiaccessibilityelement/accessibilitytraits.md)
  The combination of traits that best characterize the accessibility element.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiaccessibilityelement/accessibilityframeincontainerspace)*