# TVPosterView

**Framework**: TVUIKit  
**Kind**: class

An optimized view for displaying an image, a header, and a footer.

**Availability**:
- tvOS 12.0+

## Declaration

```swift
@MainActor
class TVPosterView
```

#### Overview

The `TVPosterView` object is a specialized [`TVLockupView`](tvlockupview.md) used to display media items. The size of the poster view expands when it comes into focus.

![A darkened image with a highlighted box in the bottom-left corner that shows a media item image and title.](https://docs-assets.developer.apple.com/published/7d8ecd26b7c4508b923d2464f359313f/media-3016829%402x.png)

## Topics

### Creating a Poster View
- [init(image: UIImage?)](tvposterview/init(image:).md)
  Creates a new poster view using the supplied image.
### Configuring a Poster View
- [var image: UIImage?](tvposterview/image.md)
  The image for the poster view.
- [var imageView: UIImageView](tvposterview/imageview.md)
  The image view associated with the poster view.
- [var title: String?](tvposterview/title.md)
  The title for the poster view.
- [var subtitle: String?](tvposterview/subtitle.md)
  The subtitle for the poster view.

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
- [class TVCaptionButtonView](tvcaptionbuttonview.md)
  A button-like view that responds to user interactions.
- [class TVMonogramView](tvmonogramview.md)
  A specialized lockup view that contains a circular image of a person or the person’s initials, along with a footer view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/tvuikit/tvposterview)*