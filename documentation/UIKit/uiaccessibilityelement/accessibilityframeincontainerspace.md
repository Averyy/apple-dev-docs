# accessibilityFrameInContainerSpace

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

The frame of the accessibility element, in the coordinate space of its container view.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- tvOS 10.0+
- visionOS 1.0+

## Declaration

```swift
var accessibilityFrameInContainerSpace: CGRect { get set }
```

```objc
@property (nonatomic, assign) CGRect accessibilityFrameInContainerSpace;
```

## Discussion

The default value of this property is [`CGRectNull`](../../CoreGraphics/cgrectnull.md). Use this property to set the frame rectangle of an element whose frame rectangle could be affected by its container view. For example, use this property to set the frame rectangle for an element in a scroll view’s content view. Changing the value of this property automatically adjusts the rectangle in the [`accessibilityFrame`](./accessibilityframe.md) property.

## See Also

### Accessing the attributes of an accessibility element
- [var accessibilityLabel: String?](./accessibilitylabel.md)
  A string that succinctly identifies the accessibility element.
- [var accessibilityHint: String?](./accessibilityhint.md)
  A string that briefly describes the result of performing an action on the accessibility element.
- [var accessibilityValue: String?](./accessibilityvalue.md)
  A string that represents the current value of the accessibility element.
- [var accessibilityFrame: CGRect](./accessibilityframe.md)
  The frame of the accessibility element, in screen coordinates.
- [var accessibilityTraits: UIAccessibilityTraits](./accessibilitytraits.md)
  The combination of traits that best characterize the accessibility element.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiaccessibilityelement/accessibilityframeincontainerspace)*