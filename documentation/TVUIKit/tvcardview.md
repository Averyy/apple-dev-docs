# TVCardView

**Framework**: TVUIKit  
**Kind**: class  
**Role**: Class

A view that responds to focus interaction with a motion effect it applies to all of its subviews.

**Availability**:
- tvOS 12.0+

## Declaration

```swift
class TVCardView
```

```objc
@interface TVCardView : TVLockupView
```

## Overview

A `TVCardView` object is a specialized version of [`TVLockupView`](./tvlockupview.md) that presents an arbitrarily composed view hierarchy in a floating content view. You add custom subviews to the [`contentView`](./tvlockupview/contentview.md) property, and the subviews act as a single unit in regard to selection and motion effects. You typically use a TVCardView to display ratings and reviews for a media item. The following figure shows a rating card that consists of two label views (the rating and related information) and an image view (the stars).

![A darkened screen with a highlighted box in the upper left corner containing the rating for a media item.](https://developer.apple.com/tutorials/images/com.apple.tvuikit/media-3016830@2x.png)

## Topics

### Setting the Background Color
- [var cardBackgroundColor: UIColor?](./tvcardview/cardbackgroundcolor.md)
  The background color of the content view.

## Relationships

### Inherits From
- [TVLockupView](./tvlockupview.md)
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
- [class TVLockupView](./tvlockupview.md)
  A focusable view that presents main content, like a movie poster, and an optional header and footer.
- [protocol TVLockupViewComponent](./tvlockupviewcomponent.md)
  The protocol for responding to lockup view state changes.
- [class TVLockupHeaderFooterView](./tvlockupheaderfooterview.md)
  A view that contains header and footer information.
- [class TVPosterView](./tvposterview.md)
  An optimized view for displaying an image, a header, and a footer.
- [class TVCaptionButtonView](./tvcaptionbuttonview.md)
  A button-like view that responds to user interactions.
- [class TVMonogramView](./tvmonogramview.md)
  A specialized lockup view that contains a circular image of a person or the person’s initials, along with a footer view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/tvuikit/tvcardview)*