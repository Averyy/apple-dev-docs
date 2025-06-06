# TipUICollectionReusableView

**Framework**: TipKit  
**Kind**: class

A UICollectionReusableView subclass that represents a tip.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- visionOS 1.0+

## Declaration

```swift
@MainActor
@objc @preconcurrency final class TipUICollectionReusableView
```

#### Overview

You create a tip view by providing a tip and an optional arrow edge. The tip is a type that conforms to the [`Tip`](tip.md) protocol. The arrow edge is a directional arrow pointing away from the tip.

## Topics

### Initializers
- [init?(coder: NSCoder)](tipuicollectionreusableview/init(coder:).md)
- [init(frame: CGRect)](tipuicollectionreusableview/init(frame:).md)
### Instance Properties
- [var cornerRadius: CGFloat](tipuicollectionreusableview/cornerradius.md)
  Corner radius for the tip view.
- [var imageSize: CGSize](tipuicollectionreusableview/imagesize.md)
  Size of the image displayed in the tip view.
- [var imageStyle: (any ShapeStyle)?](tipuicollectionreusableview/imagestyle.md)
  Foreground style for the tip’s image.
- [var viewStyle: any TipViewStyle](tipuicollectionreusableview/viewstyle.md)
  The given style for TipView within the view hierarchy
### Instance Methods
- [func configureTip(any Tip, arrowEdge: Edge?, actionHandler: (Tips.Action) -> Void) -> Self](tipuicollectionreusableview/configuretip(_:arrowedge:actionhandler:).md)
  Configures a reusable view with a tip view embedded.

## Relationships

### Inherits From
- [UICollectionReusableView](../UIKit/UICollectionReusableView.md)
### Conforms To
- [CALayerDelegate](../QuartzCore/CALayerDelegate.md)
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSCoding](../Foundation/NSCoding.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [NSTouchBarProvider](../AppKit/NSTouchBarProvider.md)
- [UIAccessibilityIdentification](../UIKit/UIAccessibilityIdentification.md)
- [UIActivityItemsConfigurationProviding](../UIKit/UIActivityItemsConfigurationProviding.md)
- [UIAppearance](../UIKit/UIAppearance.md)
- [UIAppearanceContainer](../UIKit/UIAppearanceContainer.md)
- [UICoordinateSpace](../UIKit/UICoordinateSpace.md)
- [UIDynamicItem](../UIKit/UIDynamicItem.md)
- [UIFocusEnvironment](../UIKit/UIFocusEnvironment.md)
- [UIFocusItem](../UIKit/UIFocusItem.md)
- [UIFocusItemContainer](../UIKit/UIFocusItemContainer.md)
- [UILargeContentViewerItem](../UIKit/UILargeContentViewerItem.md)
- [UIPasteConfigurationSupporting](../UIKit/UIPasteConfigurationSupporting.md)
- [UIPopoverPresentationControllerSourceItem](../UIKit/UIPopoverPresentationControllerSourceItem.md)
- [UIResponderStandardEditActions](../UIKit/UIResponderStandardEditActions.md)
- [UITraitChangeObservable](../UIKit/UITraitChangeObservable-67e94.md)
- [UITraitEnvironment](../UIKit/UITraitEnvironment.md)
- [UIUserActivityRestoring](../UIKit/UIUserActivityRestoring.md)

## See Also

- [class TipUIView](tipuiview.md)
  A user interface element that represents a tip in UIKit applications.
- [class TipUIPopoverViewController](tipuipopoverviewcontroller.md)
  A view controller that displays a popover tip in UIKit applications.
- [class TipUICollectionViewCell](tipuicollectionviewcell.md)
  A collection view cell that embeds a tip.


---

*[View on Apple Developer](https://developer.apple.com/documentation/tipkit/tipuicollectionreusableview)*