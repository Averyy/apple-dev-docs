# backgroundColor

**Framework**: UIKit  
**Kind**: property

The color of the popover’s backdrop view.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+

## Declaration

```swift
@NSCopying
@MainActor var backgroundColor: UIColor? { get set }
```

#### Discussion

Use this property to customize the background color of your popover. Changing the value of this property while the popover is visible triggers an animated change to the new color. The default value of this property is `nil`, which corresponds to the default background color.

## See Also

- [var popoverLayoutMargins: UIEdgeInsets](uipopoverpresentationcontroller/popoverlayoutmargins.md)
  The margins that define the portion of the screen in which it is permissible to display the popover.
- [var passthroughViews: [UIView]?](uipopoverpresentationcontroller/passthroughviews.md)
  An array of views that the user can interact with while the popover is visible.
- [var popoverBackgroundViewClass: (any UIPopoverBackgroundViewMethods.Type)?](uipopoverpresentationcontroller/popoverbackgroundviewclass.md)
  The class to use for displaying the popover background content.
- [var canOverlapSourceViewRect: Bool](uipopoverpresentationcontroller/canoverlapsourceviewrect.md)
  A Boolean value indicating whether the popover can overlap its view rectangle.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uipopoverpresentationcontroller/backgroundcolor)*