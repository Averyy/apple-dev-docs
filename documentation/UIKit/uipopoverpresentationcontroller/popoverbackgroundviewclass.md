# popoverBackgroundViewClass

**Framework**: UIKit  
**Kind**: property

The class to use for displaying the popover background content.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
@MainActor
var popoverBackgroundViewClass: (any UIPopoverBackgroundViewMethods.Type)? { get set }
```

#### Discussion

The default value of this property is `nil`, which causes the presentation controller to use the default popover appearance. Setting this property to a value other than `nil` causes the presentation controller to use the specified class to draw the popover’s background content. The class you specify must be a subclass of [`UIPopoverBackgroundView`](uipopoverbackgroundview.md).

## See Also

- [var popoverLayoutMargins: UIEdgeInsets](uipopoverpresentationcontroller/popoverlayoutmargins.md)
  The margins that define the portion of the screen in which it is permissible to display the popover.
- [var backgroundColor: UIColor?](uipopoverpresentationcontroller/backgroundcolor.md)
  The color of the popover’s backdrop view.
- [var passthroughViews: [UIView]?](uipopoverpresentationcontroller/passthroughviews.md)
  An array of views that the user can interact with while the popover is visible.
- [var canOverlapSourceViewRect: Bool](uipopoverpresentationcontroller/canoverlapsourceviewrect.md)
  A Boolean value indicating whether the popover can overlap its view rectangle.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uipopoverpresentationcontroller/popoverbackgroundviewclass)*