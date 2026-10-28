# TVCaptionButtonView

**Framework**: TVUIKit  
**Kind**: class  
**Role**: Class

A button-like view that responds to user interactions.

**Availability**:
- tvOS 12.0+

## Declaration

```swift
class TVCaptionButtonView
```

```objc
@interface TVCaptionButtonView : TVLockupView
```

## Overview

A caption button responds to user interactions and can contain an image or text. When the caption button comes into focus, the caption button expands in the [`leading`](../AppKit/nsdirectionaledgeinsets/leading.md), [`top`](../AppKit/nsdirectionaledgeinsets/top.md), and [`trailing`](../AppKit/nsdirectionaledgeinsets/trailing.md) directions. The user can click the caption button to select an option. As the user moves their finger on the Siri Remote up and down, or left and right, the caption button may limit the direction of the tilt based on the type set in [`motionDirection`](./tvcaptionbuttonview/motiondirection.md).

![A darkened figure with a highlighted button. The button contains a stylized TV icon with the word preview below the button.](https://developer.apple.com/tutorials/images/com.apple.tvuikit/media-3016836@2x.png)

## Topics

### Setting the Motion Direction
- [var motionDirection: TVCaptionButtonViewMotionDirection](./tvcaptionbuttonview/motiondirection.md)
  The direction that the caption button view tilts in response to user interaction on the remote.
- [enum TVCaptionButtonViewMotionDirection](./tvcaptionbuttonviewmotiondirection.md)
  The directions that the caption button view can tilt in response to user interactions on the remote.
### Configuring the Caption Button
- [var contentImage: UIImage?](./tvcaptionbuttonview/contentimage.md)
  The image displayed in the main content view.
- [var contentText: String?](./tvcaptionbuttonview/contenttext.md)
  The text displayed in the main content view.
- [var title: String?](./tvcaptionbuttonview/title.md)
  The title for the caption button.
- [var subtitle: String?](./tvcaptionbuttonview/subtitle.md)
  The subtitle of the caption button.

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
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)
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
- [class TVCardView](./tvcardview.md)
  A view that responds to focus interaction with a motion effect it applies to all of its subviews.
- [class TVPosterView](./tvposterview.md)
  An optimized view for displaying an image, a header, and a footer.
- [class TVMonogramView](./tvmonogramview.md)
  A specialized lockup view that contains a circular image of a person or the person’s initials, along with a footer view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/tvuikit/tvcaptionbuttonview)*