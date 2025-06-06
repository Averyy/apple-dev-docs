# backgroundViewClass

**Framework**: UIKit  
**Kind**: property

The class to use for displaying the popover background content.

**Availability**:
- iOS 5.0+
- iPadOS 5.0+
- Mac Catalyst 13.1+
- tvOS ?+

## Declaration

```swift
@MainActor
var backgroundViewClass: AnyClass? { get set }
```

#### Discussion

The default value of this property is `nil`, which indicates that the popover controller should use the default popover appearance. Setting this property to a value other than `nil` causes the popover controller to use the specified class to draw the popover’s background content. The class you specify must be a subclass of [`UIPopoverBackgroundView`](uipopoverbackgroundview.md).

## See Also

- [var layoutMargins: UIEdgeInsets](uipopovercontroller/layoutmargins.md)
  The margins that define the portion of the screen in which it is permissible to display the popover.
- [var backgroundColor: UIColor?](uipopovercontroller/backgroundcolor.md)
  The color of the popover’s backdrop view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uipopovercontroller/backgroundviewclass)*