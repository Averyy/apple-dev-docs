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
- [var backgroundStyle: any ShapeStyle](tipuicollectionreusableview/backgroundstyle.md)
  The background style to use for the tip view.
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
- [UICollectionReusableView](../uikit/uicollectionreusableview.md)
### Conforms To
- [CALayerDelegate](../quartzcore/calayerdelegate.md)
- [CLBodyIdentifiable](../corelocation/clbodyidentifiable.md)
- [CMBodyIdentifiable](../coremotion/cmbodyidentifiable.md)
- [CVarArg](../swift/cvararg.md)
- [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../swift/customstringconvertible.md)
- [Equatable](../swift/equatable.md)
- [Hashable](../swift/hashable.md)
- [NSCoding](../foundation/nscoding.md)
- [NSObjectProtocol](../objectivec/nsobjectprotocol.md)
- [NSTouchBarProvider](../appkit/nstouchbarprovider.md)
- [UIAccessibilityIdentification](../uikit/uiaccessibilityidentification.md)
- [UIActivityItemsConfigurationProviding](../uikit/uiactivityitemsconfigurationproviding.md)
- [UIAppearance](../uikit/uiappearance.md)
- [UIAppearanceContainer](../uikit/uiappearancecontainer.md)
- [UICoordinateSpace](../uikit/uicoordinatespace.md)
- [UIDynamicItem](../uikit/uidynamicitem.md)
- [UIFocusEnvironment](../uikit/uifocusenvironment.md)
- [UIFocusItem](../uikit/uifocusitem.md)
- [UIFocusItemContainer](../uikit/uifocusitemcontainer.md)
- [UILargeContentViewerItem](../uikit/uilargecontentvieweritem.md)
- [UIPasteConfigurationSupporting](../uikit/uipasteconfigurationsupporting.md)
- [UIPopoverPresentationControllerSourceItem](../uikit/uipopoverpresentationcontrollersourceitem.md)
- [UIResponderStandardEditActions](../uikit/uiresponderstandardeditactions.md)
- [UITraitChangeObservable](../uikit/uitraitchangeobservable-67e94.md)
- [UITraitEnvironment](../uikit/uitraitenvironment.md)
- [UIUserActivityRestoring](../uikit/uiuseractivityrestoring.md)

## See Also

- [class TipUIView](tipuiview.md)
  A user interface element that represents a tip in UIKit applications.
- [class TipUIPopoverViewController](tipuipopoverviewcontroller.md)
  A view controller that displays a popover tip in UIKit applications.
- [class TipUICollectionViewCell](tipuicollectionviewcell.md)
  A collection view cell that embeds a tip.


---

*[View on Apple Developer](https://developer.apple.com/documentation/tipkit/tipuicollectionreusableview)*