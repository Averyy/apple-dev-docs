# TVPosterView

**Framework**: TVUIKit  
**Kind**: class  
**Role**: Class

An optimized view for displaying an image, a header, and a footer.

**Availability**:
- tvOS 12.0+

## Declaration

```swift
class TVPosterView
```

```objc
@interface TVPosterView : TVLockupView
```

#### Overview

The `TVPosterView` object is a specialized [`TVLockupView`](./tvlockupview.md) used to display media items. The size of the poster view expands when it comes into focus.

![A darkened image with a highlighted box in the bottom-left corner that shows a media item image and title.](https://developer.apple.com/tutorials/images/com.apple.tvuikit/media-3016829@2x.png)

## Topics

### Creating a Poster View
- [init(image: UIImage?)](./tvposterview/init%28image%29.md)
  Creates a new poster view using the supplied image.
### Configuring a Poster View
- [var image: UIImage?](./tvposterview/image.md)
  The image for the poster view.
- [var imageView: UIImageView](./tvposterview/imageview.md)
  The image view associated with the poster view.
- [var title: String?](./tvposterview/title.md)
  The title for the poster view.
- [var subtitle: String?](./tvposterview/subtitle.md)
  The subtitle for the poster view.

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
- [class TVCaptionButtonView](./tvcaptionbuttonview.md)
  A button-like view that responds to user interactions.
- [class TVMonogramView](./tvmonogramview.md)
  A specialized lockup view that contains a circular image of a person or the person’s initials, along with a footer view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/tvuikit/tvposterview)*