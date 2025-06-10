# TVMonogramView

**Framework**: TVUIKit  
**Kind**: class

A specialized lockup view that contains a circular image of a person or the person’s initials, along with a footer view.

**Availability**:
- tvOS 12.0+

## Declaration

```swift
@MainActor
class TVMonogramView
```

#### Overview

If you don’t provide an image, the system provides a generic placeholder image. If [`personNameComponents`](tvmonogramview/personnamecomponents.md) is not `nil`, the system creates a localized monogram image using the first initials from the name components.

![A darkened image with a highlighted box along the left side. The box contains a round image with an actor’s initials inside of it.](https://docs-assets.developer.apple.com/published/fe64712a44bd1278401b48bb657bc167/media-3016835%402x.png)

## Topics

### Configuring a Monogram
- [var personNameComponents: PersonNameComponents?](tvmonogramview/personnamecomponents.md)
  The names used to create a monogram image.
- [var image: UIImage?](tvmonogramview/image.md)
  The custom image for the monogram.
- [var title: String?](tvmonogramview/title.md)
  The title for the monogram.
- [var subtitle: String?](tvmonogramview/subtitle.md)
  The subtitle for the monogram.

## Relationships

### Inherits From
- [TVLockupView](tvlockupview.md)
### Conforms To
- [CALayerDelegate](../QuartzCore/CALayerDelegate.md)
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSCoding](../Foundation/NSCoding.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)
- [UIAccessibilityIdentification](../UIKit/UIAccessibilityIdentification.md)
- [UIActivityItemsConfigurationProviding](../UIKit/UIActivityItemsConfigurationProviding.md)
- [UIAppearance](../UIKit/UIAppearance.md)
- [UIAppearanceContainer](../UIKit/UIAppearanceContainer.md)
- [UIContextMenuInteractionDelegate](../UIKit/UIContextMenuInteractionDelegate.md)
- [UICoordinateSpace](../UIKit/UICoordinateSpace.md)
- [UIDynamicItem](../UIKit/UIDynamicItem.md)
- [UIFocusEnvironment](../UIKit/UIFocusEnvironment.md)
- [UIFocusItem](../UIKit/UIFocusItem.md)
- [UIFocusItemContainer](../UIKit/UIFocusItemContainer.md)
- [UIPopoverPresentationControllerSourceItem](../UIKit/UIPopoverPresentationControllerSourceItem.md)
- [UIResponderStandardEditActions](../UIKit/UIResponderStandardEditActions.md)
- [UITraitChangeObservable](../UIKit/UITraitChangeObservable-67e94.md)
- [UITraitEnvironment](../UIKit/UITraitEnvironment.md)
- [UIUserActivityRestoring](../UIKit/UIUserActivityRestoring.md)

## See Also

- [class TVLockupView](tvlockupview.md)
  A focusable view that presents main content, like a movie poster, and an optional header and footer.
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


---

*[View on Apple Developer](https://developer.apple.com/documentation/tvuikit/tvmonogramview)*