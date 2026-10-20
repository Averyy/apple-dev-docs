# accessibilityFrame

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

The frame of the accessibility element, in screen coordinates.

**Availability**:
- iOS 3.0+
- iPadOS 3.0+
- Mac Catalyst 13.1+
- tvOS
- visionOS 1.0+

## Declaration

```swift
var accessibilityFrame: CGRect { get set }
```

```objc
@property (nonatomic, assign) CGRect accessibilityFrame;
```

#### Discussion

When you create an accessibility element to represent an element in your application, you must set this property to the `CGRect` structure that specifies the object’s screen location and size. (Objects that inherit from `UIView` include this information by default.)

Assigning a new value to this property changes the value of the [`accessibilityFrameInContainerSpace`](./accessibilityframeincontainerspace.md) property to [`CGRectNull`](../../CoreGraphics/cgrectnull.md).

## See Also

### Related Documentation
- [static func convertToScreenCoordinates(CGRect, in: UIView) -> CGRect](../uiaccessibility/converttoscreencoordinates%28_,in%29-9ziiu.md)
  Converts the specified rectangle from view coordinates to screen coordinates.
### Accessing the attributes of an accessibility element
- [var accessibilityLabel: String?](./accessibilitylabel.md)
  A string that succinctly identifies the accessibility element.
- [var accessibilityHint: String?](./accessibilityhint.md)
  A string that briefly describes the result of performing an action on the accessibility element.
- [var accessibilityValue: String?](./accessibilityvalue.md)
  A string that represents the current value of the accessibility element.
- [var accessibilityFrameInContainerSpace: CGRect](./accessibilityframeincontainerspace.md)
  The frame of the accessibility element, in the coordinate space of its container view.
- [var accessibilityTraits: UIAccessibilityTraits](./accessibilitytraits.md)
  The combination of traits that best characterize the accessibility element.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uiaccessibilityelement/accessibilityframe)*