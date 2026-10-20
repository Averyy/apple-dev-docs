# TVLockupView

**Framework**: TVUIKit  
**Kind**: class  
**Role**: Class

A focusable view that presents main content, like a movie poster, and an optional header and footer.

**Availability**:
- tvOS 12.0+

## Declaration

```swift
class TVLockupView
```

```objc
@interface TVLockupView : UIControl
```

#### Overview

A `TVLockupView` object consists of three views that operate as a single view. The content view typically contains a media item image, like a movie poster, with additional information in the header and footer views. The `TVLockupView` object expands when it comes into focus, using [`focusSizeIncrease`](./tvlockupview/focussizeincrease.md) and [`contentSize`](./tvlockupview/contentsize.md) to calculate the size increase. Provide sufficient `focusSizeIncrease` values so that your custom content doesn’t overlap other objects when the content comes into focus.

The following figure shows a `TVLockupView` object that’s in focus. The yellow, vertical bars indicate the space between views. The center view is in focus and has increased in size, expanding into the space between views. Views don’t move as other views come into focus.

![A diagram depicting five TV lockup views in a row, separated by yellow, vertical bars that indicate the space between views. The center view is larger than the other views and covers part of the yellow areas on either side of it.](https://developer.apple.com/tutorials/images/com.apple.tvuikit/media-3016664@2x.png)

> **Note**:  Don’t create a [`TVLockupView`](./tvlockupview.md) directly. Instead, create an instance of the subclass that best suits your use case, such as [`TVPosterView`](./tvposterview.md) or [`TVCardView`](./tvcardview.md).

## Topics

### Setting view size
- [var contentSize: CGSize](./tvlockupview/contentsize.md)
  The size of the content view.
- [var contentViewInsets: NSDirectionalEdgeInsets](./tvlockupview/contentviewinsets.md)
  The spacing between the content view and its peer and containing views.
- [var focusSizeIncrease: NSDirectionalEdgeInsets](./tvlockupview/focussizeincrease.md)
  The inset or outset values specifying your content’s size increase when in focus.
### Adding subviews
- [var contentView: UIView](./tvlockupview/contentview.md)
  The main view for the lockup.
- [var headerView: TVLockupHeaderFooterView?](./tvlockupview/headerview.md)
  A view containing header information.
- [var footerView: TVLockupHeaderFooterView?](./tvlockupview/footerview.md)
  A view containing footer information.

## Relationships

### Inherits From
- [UIControl](../UIKit/uicontrol.md)
### Inherited By
- [TVCaptionButtonView](./tvcaptionbuttonview.md)
- [TVCardView](./tvcardview.md)
- [TVMonogramView](./tvmonogramview.md)
- [TVPosterView](./tvposterview.md)
### Conforms To
- [CALayerDelegate](../QuartzCore/calayerdelegate.md)
- [CLBodyIdentifiable](../CoreLocation/clbodyidentifiable.md)
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSCoding](../Foundation/nscoding.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)
- [UIAccessibilityIdentification](../UIKit/uiaccessibilityidentification.md)
- [UIActivityItemsConfigurationProviding](../UIKit/uiactivityitemsconfigurationproviding.md)
- [UIAppearance](../UIKit/uiappearance.md)
- [UIAppearanceContainer](../UIKit/uiappearancecontainer.md)
- [UIContextMenuInteractionDelegate](../UIKit/uicontextmenuinteractiondelegate.md)
- [UICoordinateSpace](../UIKit/uicoordinatespace.md)
- [UIDynamicItem](../UIKit/uidynamicitem.md)
- [UIFocusEnvironment](../UIKit/uifocusenvironment.md)
- [UIFocusItem](../UIKit/uifocusitem.md)
- [UIFocusItemContainer](../UIKit/uifocusitemcontainer.md)
- [UIPopoverPresentationControllerSourceItem](../UIKit/uipopoverpresentationcontrollersourceitem.md)
- [UIResponderStandardEditActions](../UIKit/uiresponderstandardeditactions.md)
- [UITraitChangeObservable](../UIKit/uitraitchangeobservable-67e94.md)
- [UITraitEnvironment](../UIKit/uitraitenvironment.md)
- [UIUserActivityRestoring](../UIKit/uiuseractivityrestoring.md)

## See Also

### Lockup views
- [protocol TVLockupViewComponent](./tvlockupviewcomponent.md)
  The protocol for responding to lockup view state changes.
- [class TVLockupHeaderFooterView](./tvlockupheaderfooterview.md)
  A view that contains header and footer information.
- [class TVCardView](./tvcardview.md)
  A view that responds to focus interaction with a motion effect it applies to all of its subviews.
- [class TVPosterView](./tvposterview.md)
  An optimized view for displaying an image, a header, and a footer.
- [class TVCaptionButtonView](./tvcaptionbuttonview.md)
  A button-like view that responds to user interactions.
- [class TVMonogramView](./tvmonogramview.md)
  A specialized lockup view that contains a circular image of a person or the person’s initials, along with a footer view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/tvuikit/tvlockupview)*