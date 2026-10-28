# TipUICollectionReusableView

**Framework**: TipKit  
**Kind**: class  
**Role**: Class

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

## Overview

You create a tip view by providing a tip and an optional arrow edge. The tip is a type that conforms to the [`Tip`](./tip.md) protocol. The arrow edge is a directional arrow pointing away from the tip.

## Topics

### Initializers
- [init?(coder: NSCoder)](./tipuicollectionreusableview/init%28coder%29.md)
- [init(frame: CGRect)](./tipuicollectionreusableview/init%28frame%29.md)
### Instance Properties
- [var backgroundStyle: any ShapeStyle](./tipuicollectionreusableview/backgroundstyle.md)
  The background style to use for the tip view.
- [var cornerRadius: CGFloat](./tipuicollectionreusableview/cornerradius.md)
  Corner radius for the tip view.
- [var imageSize: CGSize](./tipuicollectionreusableview/imagesize.md)
  Size of the image displayed in the tip view.
- [var imageStyle: (any ShapeStyle)?](./tipuicollectionreusableview/imagestyle.md)
  Foreground style for the tip’s image.
- [var viewStyle: any TipViewStyle](./tipuicollectionreusableview/viewstyle.md)
  The given style for TipView within the view hierarchy
### Instance Methods
- [func configureTip(any Tip, arrowEdge: Edge?, actionHandler: (Tips.Action) -> Void) -> Self](./tipuicollectionreusableview/configuretip%28_,arrowedge,actionhandler%29.md)
  Configures a reusable view with a tip view embedded.

## Relationships

### Inherits From
- [UICollectionReusableView](../UIKit/uicollectionreusableview.md)
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
- [UIAccessibilityIdentification](../UIKit/uiaccessibilityidentification.md)
- [UIActivityItemsConfigurationProviding](../UIKit/uiactivityitemsconfigurationproviding.md)
- [UIAppearance](../UIKit/uiappearance.md)
- [UIAppearanceContainer](../UIKit/uiappearancecontainer.md)
- [UICoordinateSpace](../UIKit/uicoordinatespace.md)
- [UIDynamicItem](../UIKit/uidynamicitem.md)
- [UIFocusEnvironment](../UIKit/uifocusenvironment.md)
- [UIFocusItem](../UIKit/uifocusitem.md)
- [UIFocusItemContainer](../UIKit/uifocusitemcontainer.md)
- [UILargeContentViewerItem](../UIKit/uilargecontentvieweritem.md)
- [UIPasteConfigurationSupporting](../UIKit/uipasteconfigurationsupporting.md)
- [UIPopoverPresentationControllerSourceItem](../UIKit/uipopoverpresentationcontrollersourceitem.md)
- [UIResponderStandardEditActions](../UIKit/uiresponderstandardeditactions.md)
- [UITraitChangeObservable](../UIKit/uitraitchangeobservable-67e94.md)
- [UITraitEnvironment](../UIKit/uitraitenvironment.md)
- [UIUserActivityRestoring](../UIKit/uiuseractivityrestoring.md)

## See Also

### UIKit Views
- [class TipUIView](./tipuiview.md)
  A user interface element that represents a tip in UIKit applications.
- [class TipUIPopoverViewController](./tipuipopoverviewcontroller.md)
  A view controller that displays a popover tip in UIKit applications.
- [class TipUICollectionViewCell](./tipuicollectionviewcell.md)
  A collection view cell that embeds a tip.


---

*[View on Apple Developer](https://developer.apple.com/documentation/tipkit/tipuicollectionreusableview)*