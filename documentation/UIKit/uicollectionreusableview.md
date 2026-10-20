# UICollectionReusableView

**Framework**: UIKit  
**Kind**: class  
**Role**: Class

A view that defines the behavior for all cells and supplementary views presented by a collection view.

**Availability**:
- iOS 6.0+
- iPadOS 6.0+
- Mac Catalyst 13.1+
- tvOS
- visionOS 1.0+

## Declaration

```swift
@MainActor
class UICollectionReusableView
```

```objc
@interface UICollectionReusableView : UIView
```

#### Overview

Reusable views are so named because the collection view places them on a reuse queue rather than deleting them when they’re scrolled out of the visible bounds. Such a view can then be retrieved and repurposed for a different set of content.

##### Subclassing notes

This class is intended to be subclassed. Most methods defined by this class have minimal or no implementations. You aren’t required to override any of the methods but can do so in cases where you want to respond to changes in the view’s usage or layout.

## Topics

### Reusing cells
- [var reuseIdentifier: String?](./uicollectionreusableview/reuseidentifier.md)
  A string that identifies the purpose of the view.
- [func prepareForReuse()](./uicollectionreusableview/prepareforreuse%28%29.md)
  Performs any clean up necessary to prepare the view for use again.
### Managing layout changes
- [func preferredLayoutAttributesFitting(UICollectionViewLayoutAttributes) -> UICollectionViewLayoutAttributes](./uicollectionreusableview/preferredlayoutattributesfitting%28_%29.md)
  Gives the cell a chance to modify the attributes provided by the layout object.
- [func apply(UICollectionViewLayoutAttributes)](./uicollectionreusableview/apply%28_%29.md)
  Applies the specified layout attributes to the view.
- [func willTransition(from: UICollectionViewLayout, to: UICollectionViewLayout)](./uicollectionreusableview/willtransition%28from,to%29.md)
  Tells your view that the layout object of the collection view is about to change.
- [func didTransition(from: UICollectionViewLayout, to: UICollectionViewLayout)](./uicollectionreusableview/didtransition%28from,to%29.md)
  Tells your view that the layout object of the collection view changed.

## Relationships

### Inherits From
- [UIView](./uiview.md)
### Inherited By
- [UICollectionViewCell](./uicollectionviewcell.md)
### Conforms To
- [CALayerDelegate](../QuartzCore/calayerdelegate.md)
- [CLBodyIdentifiable](../CoreLocation/clbodyidentifiable.md)
- [CMBodyIdentifiable](../CoreMotion/cmbodyidentifiable.md)
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSCoding](../Foundation/nscoding.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)
- [NSTouchBarProvider](../AppKit/nstouchbarprovider.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)
- [UIAccessibilityIdentification](./uiaccessibilityidentification.md)
- [UIActivityItemsConfigurationProviding](./uiactivityitemsconfigurationproviding.md)
- [UIAppearance](./uiappearance.md)
- [UIAppearanceContainer](./uiappearancecontainer.md)
- [UICoordinateSpace](./uicoordinatespace.md)
- [UIDynamicItem](./uidynamicitem.md)
- [UIFocusEnvironment](./uifocusenvironment.md)
- [UIFocusItem](./uifocusitem.md)
- [UIFocusItemContainer](./uifocusitemcontainer.md)
- [UILargeContentViewerItem](./uilargecontentvieweritem.md)
- [UIPasteConfigurationSupporting](./uipasteconfigurationsupporting.md)
- [UIPopoverPresentationControllerSourceItem](./uipopoverpresentationcontrollersourceitem.md)
- [UIResponderStandardEditActions](./uiresponderstandardeditactions.md)
- [UITraitChangeObservable](./uitraitchangeobservable-67e94.md)
- [UITraitEnvironment](./uitraitenvironment.md)
- [UIUserActivityRestoring](./uiuseractivityrestoring.md)

## See Also

### Cells
- [class UICollectionViewCell](./uicollectionviewcell.md)
  A single data item when that item is within the collection view’s visible bounds.
- [class UICollectionViewListCell](./uicollectionviewlistcell.md)
  A collection view cell that provides list features and default styling.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uicollectionreusableview)*