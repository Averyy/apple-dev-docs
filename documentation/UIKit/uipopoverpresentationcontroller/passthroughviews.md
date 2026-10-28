# passthroughViews

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

An array of views that the user can interact with while the popover is visible.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- visionOS 1.0+

## Declaration

```swift
var passthroughViews: [UIView]? { get set }
```

```objc
@property (nonatomic, copy, nullable) NSArray<UIView *> * passthroughViews;
```

## Discussion

When a popover is active, interactions with other views are normally disabled until the popover is dismissed. Assigning an array of [`UIView`](../uiview.md) objects to this property causes UIKit to continue dispatching touch event to the views you specified.

## See Also

### Configuring the popover appearance
- [var popoverLayoutMargins: UIEdgeInsets](./popoverlayoutmargins.md)
  The margins that define the portion of the screen in which it is permissible to display the popover.
- [var backgroundColor: UIColor?](./backgroundcolor.md)
  The color of the popover’s backdrop view.
- [var popoverBackgroundViewClass: (any UIPopoverBackgroundViewMethods.Type)?](./popoverbackgroundviewclass.md)
  The class to use for displaying the popover background content.
- [var canOverlapSourceViewRect: Bool](./canoverlapsourceviewrect.md)
  A Boolean value indicating whether the popover can overlap its view rectangle.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uipopoverpresentationcontroller/passthroughviews)*