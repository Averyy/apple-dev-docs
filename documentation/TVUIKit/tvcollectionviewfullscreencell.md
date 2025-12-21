# TVCollectionViewFullScreenCell

**Framework**: TVUIKit  
**Kind**: class

A full-screen cell to use in full-screen display format.

**Availability**:
- tvOS 13.0+

## Declaration

```swift
@MainActor
class TVCollectionViewFullScreenCell
```

#### Overview

Use `TVCollectionViewFullScreenCell` to populate the full-screen collection view with content.

## Topics

### Modifying Cell Appearance
- [var contentBleed: UIEdgeInsets](tvcollectionviewfullscreencell/contentbleed.md)
  The amount of content that overlaps into the masked portions of the cell.
- [var cornerRadius: CGFloat](tvcollectionviewfullscreencell/cornerradius.md)
  The radius to use when drawing rounded corners for the cell.
- [var maskAmount: CGFloat](tvcollectionviewfullscreencell/maskamount.md)
  The factor that determines the amount of masking applied on the cell.
### Accessing Cell Views
- [var maskedContentView: UIView](tvcollectionviewfullscreencell/maskedcontentview.md)
  The content view in focus.
- [var maskedBackgroundView: UIView](tvcollectionviewfullscreencell/maskedbackgroundview.md)
  The background view that performs the parallax effect.
### Accessing Cell Position
- [var normalizedPosition: CGFloat](tvcollectionviewfullscreencell/normalizedposition.md)
  The value that determines the current cell’s relative position on the screen.
### Managing Cell Position
- [func normalizedPositionDidChange()](tvcollectionviewfullscreencell/normalizedpositiondidchange.md)
  Notifies the cell when its normalized position changes.
- [func normalizedPositionWillChange(CGFloat)](tvcollectionviewfullscreencell/normalizedpositionwillchange(_:).md)
  Notifies the cell when its normalized position is about to change.
### Managing Cell Mask
- [func maskAmountDidChange()](tvcollectionviewfullscreencell/maskamountdidchange.md)
  Notifies the cell when its mask amount changes.
- [func maskAmountWillChange(CGFloat)](tvcollectionviewfullscreencell/maskamountwillchange(_:).md)
  Notifies the cell when its mask amount is about to change.
### Managing the Parallax Effect
- [var parallaxOffset: CGFloat](tvcollectionviewfullscreencell/parallaxoffset.md)
  The number of pixels by which to shift the background from the center when moving focus.

## Relationships

### Inherits From
- [UICollectionViewCell](../UIKit/UICollectionViewCell.md)
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

- [Creating immersive experiences using a full-screen layout](creating-immersive-experiences-using-a-full-screen-layout.md)
  Display content with a collection view that maximizes the tvOS experience.
- [class TVCollectionViewFullScreenLayout](tvcollectionviewfullscreenlayout.md)
  A collection view layout that organizes items into a browsable, full-screen display format.
- [protocol TVCollectionViewDelegateFullScreenLayout](tvcollectionviewdelegatefullscreenlayout.md)
  Methods that send notifications of events during cell transitions.
- [class TVCollectionViewFullScreenLayoutAttributes](tvcollectionviewfullscreenlayoutattributes.md)
  Attributes to manage the appearance of the collection view’s layout.


---

*[View on Apple Developer](https://developer.apple.com/documentation/tvuikit/tvcollectionviewfullscreencell)*