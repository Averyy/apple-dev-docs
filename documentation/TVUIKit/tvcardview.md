# TVCardView

**Framework**: TVUIKit  
**Kind**: class

A view that responds to focus interaction with a motion effect it applies to all of its subviews.

**Availability**:
- tvOS 12.0+

## Declaration

```swift
@MainActor
class TVCardView
```

#### Overview

A `TVCardView` object is a specialized version of [`TVLockupView`](tvlockupview.md) that presents an arbitrarily composed view hierarchy in a floating content view. You add custom subviews to the [`contentView`](tvlockupview/contentview.md) property, and the subviews act as a single unit in regard to selection and motion effects. You typically use a TVCardView to display ratings and reviews for a media item. The following figure shows a rating card that consists of two label views (the rating and related information) and an image view (the stars).

![A darkened screen with a highlighted box in the upper left corner containing the rating for a media item.](https://docs-assets.developer.apple.com/published/9e3a591eedd92d1c844d51b7ed6b4f51/media-3016830%402x.png)

## Topics

### Setting the Background Color
- [var cardBackgroundColor: UIColor?](tvcardview/cardbackgroundcolor.md)
  The background color of the content view.

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

- [class TVLockupView](tvlockupview.md)
  A focusable view that presents main content, like a movie poster, and an optional header and footer.
- [protocol TVLockupViewComponent](tvlockupviewcomponent.md)
  The protocol for responding to lockup view state changes.
- [class TVLockupHeaderFooterView](tvlockupheaderfooterview.md)
  A view that contains header and footer information.
- [class TVPosterView](tvposterview.md)
  An optimized view for displaying an image, a header, and a footer.
- [class TVCaptionButtonView](tvcaptionbuttonview.md)
  A button-like view that responds to user interactions.
- [class TVMonogramView](tvmonogramview.md)
  A specialized lockup view that contains a circular image of a person or the person’s initials, along with a footer view.


---

*[View on Apple Developer](https://developer.apple.com/documentation/tvuikit/tvcardview)*