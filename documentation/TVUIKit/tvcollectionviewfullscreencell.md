# TVCollectionViewFullScreenCell

**Framework**: TVUIKit  
**Kind**: class  
**Role**: Class

A full-screen cell to use in full-screen display format.

**Availability**:
- tvOS 13.0+

## Declaration

```swift
class TVCollectionViewFullScreenCell
```

```objc
@interface TVCollectionViewFullScreenCell : UICollectionViewCell
```

## Overview

Use `TVCollectionViewFullScreenCell` to populate the full-screen collection view with content.

## Topics

### Modifying Cell Appearance
- [var contentBleed: UIEdgeInsets](./tvcollectionviewfullscreencell/contentbleed.md)
  The amount of content that overlaps into the masked portions of the cell.
- [var cornerRadius: CGFloat](./tvcollectionviewfullscreencell/cornerradius.md)
  The radius to use when drawing rounded corners for the cell.
- [var maskAmount: CGFloat](./tvcollectionviewfullscreencell/maskamount.md)
  The factor that determines the amount of masking applied on the cell.
### Accessing Cell Views
- [var maskedContentView: UIView](./tvcollectionviewfullscreencell/maskedcontentview.md)
  The content view in focus.
- [var maskedBackgroundView: UIView](./tvcollectionviewfullscreencell/maskedbackgroundview.md)
  The background view that performs the parallax effect.
### Accessing Cell Position
- [var normalizedPosition: CGFloat](./tvcollectionviewfullscreencell/normalizedposition.md)
  The value that determines the current cell’s relative position on the screen.
### Managing Cell Position
- [func normalizedPositionDidChange()](./tvcollectionviewfullscreencell/normalizedpositiondidchange%28%29.md)
  Notifies the cell when its normalized position changes.
- [func normalizedPositionWillChange(CGFloat)](./tvcollectionviewfullscreencell/normalizedpositionwillchange%28_%29.md)
  Notifies the cell when its normalized position is about to change.
### Managing Cell Mask
- [func maskAmountDidChange()](./tvcollectionviewfullscreencell/maskamountdidchange%28%29.md)
  Notifies the cell when its mask amount changes.
- [func maskAmountWillChange(CGFloat)](./tvcollectionviewfullscreencell/maskamountwillchange%28_%29.md)
  Notifies the cell when its mask amount is about to change.
### Managing the Parallax Effect
- [var parallaxOffset: CGFloat](./tvcollectionviewfullscreencell/parallaxoffset.md)
  The number of pixels by which to shift the background from the center when moving focus.

## Relationships

### Inherits From
- [UICollectionViewCell](../UIKit/uicollectionviewcell.md)
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

### Collections of content
- [Creating immersive experiences using a full-screen layout](./creating-immersive-experiences-using-a-full-screen-layout.md)
  Display content with a collection view that maximizes the tvOS experience.
- [class TVCollectionViewFullScreenLayout](./tvcollectionviewfullscreenlayout.md)
  A collection view layout that organizes items into a browsable, full-screen display format.
- [protocol TVCollectionViewDelegateFullScreenLayout](./tvcollectionviewdelegatefullscreenlayout.md)
  Methods that send notifications of events during cell transitions.
- [class TVCollectionViewFullScreenLayoutAttributes](./tvcollectionviewfullscreenlayoutattributes.md)
  Attributes to manage the appearance of the collection view’s layout.


---

*[View on Apple Developer](https://developer.apple.com/documentation/tvuikit/tvcollectionviewfullscreencell)*