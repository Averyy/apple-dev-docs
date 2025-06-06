# popoverLayoutMargins

**Framework**: UIKit  
**Kind**: property

The margins that define the portion of the screen in which it is permissible to display the popover.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+

## Declaration

```swift
@MainActor
var popoverLayoutMargins: UIEdgeInsets { get set }
```

#### Discussion

The edge inset values are measured in points from the edges of the screen, relative to the current device orientation. Thus, the top-edge inset always reflects the top edge of the device from the user’s perspective, which changes depending on whether the user is holding the device in a portrait or landscape orientation. Remember that the device orientation is not always the same as the interface orientation—that is, the orientation of your window and views. Window orientations are typically fixed and view orientations are controlled by the owning view controller. In addition, if the rotation lock option is engaged, the interface does not change orientation at all, even when the device orientation changes.

The default edge insets are 10 points along each edge. The popover presentation controller automatically subtracts the status bar from the viable area when determining where to display the popover, so you do not need to factor the status bar height into your insets.

## See Also

- [var backgroundColor: UIColor?](uipopoverpresentationcontroller/backgroundcolor.md)
  The color of the popover’s backdrop view.
- [var passthroughViews: [UIView]?](uipopoverpresentationcontroller/passthroughviews.md)
  An array of views that the user can interact with while the popover is visible.
- [var popoverBackgroundViewClass: (any UIPopoverBackgroundViewMethods.Type)?](uipopoverpresentationcontroller/popoverbackgroundviewclass.md)
  The class to use for displaying the popover background content.
- [var canOverlapSourceViewRect: Bool](uipopoverpresentationcontroller/canoverlapsourceviewrect.md)
  A Boolean value indicating whether the popover can overlap its view rectangle.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uipopoverpresentationcontroller/popoverlayoutmargins)*