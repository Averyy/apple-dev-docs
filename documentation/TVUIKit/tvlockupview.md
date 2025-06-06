# TVLockupView

**Framework**: Tvuikit  
**Kind**: class

A focusable view that presents main content, like a movie poster, and an optional header and footer.

**Availability**:
- tvOS 12.0+

## Declaration

```swift
@MainActor
class TVLockupView
```

#### Overview

A `TVLockupView` object consists of three views that operate as a single view. The content view typically contains a media item image, like a movie poster, with additional information in the header and footer views. The `TVLockupView` object expands when it comes into focus, using [`focusSizeIncrease`](tvlockupview/focussizeincrease.md) and [`contentSize`](tvlockupview/contentsize.md) to calculate the size increase. Provide sufficient `focusSizeIncrease` values so that your custom content doesn’t overlap other objects when the content comes into focus.

The following figure shows a `TVLockupView` object that’s in focus. The yellow, vertical bars indicate the space between views. The center view is in focus and has increased in size, expanding into the space between views. Views don’t move as other views come into focus.

![A diagram depicting five TV lockup views in a row, separated by yellow, vertical bars that indicate the space between views. The center view is larger than the other views and covers part of the yellow areas on either side of it.](https://docs-assets.developer.apple.com/published/2ed04a2c3cfadc7465289bdfbee40037/media-3016664%402x.png)

> **Note**:  Don’t create a [`TVLockupView`](tvlockupview.md) directly. Instead, create an instance of the subclass that best suits your use case, such as [`TVPosterView`](tvposterview.md) or [`TVCardView`](tvcardview.md).

## Topics

### Setting view size
- [var contentSize: CGSize](tvlockupview/contentsize.md)
  The size of the content view.
- [var contentViewInsets: NSDirectionalEdgeInsets](tvlockupview/contentviewinsets.md)
  The spacing between the content view and its peer and containing views.
- [var focusSizeIncrease: NSDirectionalEdgeInsets](tvlockupview/focussizeincrease.md)
  The inset or outset values specifying your content’s size increase when in focus.
### Adding subviews
- [var contentView: UIView](tvlockupview/contentview.md)
  The main view for the lockup.
- [var headerView: TVLockupHeaderFooterView?](tvlockupview/headerview.md)
  A view containing header information.
- [var footerView: TVLockupHeaderFooterView?](tvlockupview/footerview.md)
  A view containing footer information.

## Relationships

### Inherits From
- [UIControl](../UIKit/UIControl.md)
### Inherited By
- [TVCaptionButtonView](tvcaptionbuttonview.md)
- [TVCardView](tvcardview.md)
- [TVMonogramView](tvmonogramview.md)
- [TVPosterView](tvposterview.md)
### Conforms To
- [CALayerDelegate](../QuartzCore/CALayerDelegate.md)
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSCoding](../Foundation/NSCoding.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [UIAccessibilityIdentification](../UIKit/UIAccessibilityIdentification.md)
- [UIAppearance](../UIKit/UIAppearance.md)
- [UIAppearanceContainer](../UIKit/UIAppearanceContainer.md)
- [UIContextMenuInteractionDelegate](../UIKit/UIContextMenuInteractionDelegate.md)
- [UICoordinateSpace](../UIKit/UICoordinateSpace.md)
- [UIDynamicItem](../UIKit/UIDynamicItem.md)
- [UIFocusEnvironment](../UIKit/UIFocusEnvironment.md)
- [UIFocusItem](../UIKit/UIFocusItem.md)
- [UIFocusItemContainer](../UIKit/UIFocusItemContainer.md)
- [UIResponderStandardEditActions](../UIKit/UIResponderStandardEditActions.md)
- [UITraitChangeObservable](../UIKit/UITraitChangeObservable-67e94.md)
- [UITraitEnvironment](../UIKit/UITraitEnvironment.md)
- [UIUserActivityRestoring](../UIKit/UIUserActivityRestoring.md)

## See Also

- [protocol TVLockupViewComponent](tvlockupviewcomponent.md)
  The protocol for responding to lockup view state changes.
- [class TVLockupHeaderFooterView](tvlockupheaderfooterview.md)
  A view that contains header and footer information.
- [class TVCardView](tvcardview.md)
  A view that responds to focus interaction with a motion effect it applies to all of its subviews.
- [class TVPosterView](tvposterview.md)
  An optimized view for displaying an image, a header, and a footer.
- [class TVCaptionButtonView](tvcaptionbuttonview.md)
  A button-like view that responds to user interactions.
- [class TVMonogramView](tvmonogramview.md)
  A specialized lockup view that contains a circular image of a person or the person’s initials, along with a footer view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/TVUIKit/tvlockupview)*