# TVMonogramView

**Framework**: TVUIKit  
**Kind**: class  
**Role**: Class

A specialized lockup view that contains a circular image of a person or the person’s initials, along with a footer view.

**Availability**:
- tvOS 12.0+ - Deprecated in 27.2 (renamed: __TVMonogramContentConfiguration)

> **Deprecated**: Use [`TVMonogramContentView`](./tvmonogramcontentview.md) instead.

## Declaration

```swift
class TVMonogramView
```

```objc
@interface TVMonogramView : TVLockupView
```

## Overview

If you don’t provide an image, the system provides a generic placeholder image. If [`personNameComponents`](./tvmonogramview/personnamecomponents.md) is not `nil`, the system creates a localized monogram image using the first initials from the name components.

![A darkened image with a highlighted box along the left side. The box contains a round image with an actor’s initials inside of it.](https://developer.apple.com/tutorials/images/com.apple.tvuikit/media-3016835@2x.png)

## Topics

### Configuring a Monogram
- [var personNameComponents: PersonNameComponents?](./tvmonogramview/personnamecomponents.md)
  The names used to create a monogram image.
- [var image: UIImage?](./tvmonogramview/image.md)
  The custom image for the monogram.
- [var title: String?](./tvmonogramview/title.md)
  The title for the monogram.
- [var subtitle: String?](./tvmonogramview/subtitle.md)
  The subtitle for the monogram.

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
- [class TVCaptionButtonView](./tvcaptionbuttonview.md)
  A button-like view that responds to user interactions.


---

*[View on Apple Developer](https://developer.apple.com/documentation/tvuikit/tvmonogramview)*