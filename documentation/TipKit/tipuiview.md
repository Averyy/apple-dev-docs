# TipUIView

**Framework**: TipKit  
**Kind**: class

A user interface element that represents a tip in UIKit applications.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- visionOS 1.0+

## Declaration

```swift
@MainActor
@objc @preconcurrency final class TipUIView
```

#### Overview

Use this view to create a tip you want to display and lay out as a [`UIView`](https://developer.apple.com/documentation/uikit/uiview). To configure the content and appearance of your view, use the [`init(_:arrowEdge:actionHandler:)`](tipuiview/init(_:arrowedge:actionhandler:).md) function and provide a tip along with an optional arrow edge and optional action. Set the background color of your tip view using [`backgroundColor`](tipuiview/backgroundcolor.md).

Adding and removing TipUIView from your app is done by listening to a tip’s [`shouldDisplayUpdates`](tip/shoulddisplayupdates.md) or [`statusUpdates`](tip/statusupdates.md).

```swift
import TipKit
import UIKit

struct CatTracksFeatureTip: Tip {
    var title: Text {
        Text("Sample tip title")
    }

    var message: Text? {
        Text("Sample tip message")
    }

    var image: Image? {
        Image(systemName: "globe")
    }
}

class CatTracksViewController: UIViewController {
    private var catTracksFeatureTip = CatTracksFeatureTip()
    private var tipObservationTask: Task<Void, Never>?
    private weak var tipView: TipUIView?    

    override func viewDidAppear(_ animated: Bool) {
        super.viewDidAppear(animated)

        tipObservationTask = tipObservationTask ?? Task { @MainActor in
            for await shouldDisplay in catTracksFeatureTip.shouldDisplayUpdates {
                if shouldDisplay {
                    let tipHostingView = TipUIView(catTracksFeatureTip)
                    tipHostingView.translatesAutoresizingMaskIntoConstraints = false
                                        
                    view.addSubview(tipHostingView)

                    view.addConstraints([
                        tipHostingView.centerYAnchor.constraint(equalTo: view.centerYAnchor),
                        tipHostingView.leadingAnchor.constraint(equalTo: view.leadingAnchor, constant: 20.0),
                        tipHostingView.trailingAnchor.constraint(equalTo: view.trailingAnchor, constant: -20.0)
                    ])

                    tipView = tipHostingView
                }
                else {
                    tipView?.removeFromSuperview()
                    tipView = nil
                }
            }
        }
    }

    override func viewWillDisappear(_ animated: Bool) {
        super.viewWillDisappear(animated)

        tipObservationTask?.cancel()
        tipObservationTask = nil
    }
}
```

## Topics

### Initializers
- [init(any Tip, arrowEdge: Edge?, actionHandler: (Tips.Action) -> Void)](tipuiview/init(_:arrowedge:actionhandler:).md)
  Creates a tip view with an optional arrow edge and action handler.
### Instance Properties
- [var backgroundColor: UIColor?](tipuiview/backgroundcolor.md)
  The background color to use for the tip view.
- [var backgroundStyle: any ShapeStyle](tipuiview/backgroundstyle.md)
  The background style to use for the tip view.
- [var cornerRadius: CGFloat](tipuiview/cornerradius.md)
  Corner radius for the tip view.
- [var imageSize: CGSize](tipuiview/imagesize.md)
  Size of the image displayed in the tip view.
- [var imageStyle: (any ShapeStyle)?](tipuiview/imagestyle.md)
  Foreground style for the tip’s image.
- [var viewStyle: any TipViewStyle](tipuiview/viewstyle.md)
  The given style for TipView within the view hierarchy.

## Relationships

### Inherits From
- [UIView](../uikit/uiview.md)
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

- [class TipUIPopoverViewController](tipuipopoverviewcontroller.md)
  A view controller that displays a popover tip in UIKit applications.
- [class TipUICollectionViewCell](tipuicollectionviewcell.md)
  A collection view cell that embeds a tip.
- [class TipUICollectionReusableView](tipuicollectionreusableview.md)
  A UICollectionReusableView subclass that represents a tip.


---

*[View on Apple Developer](https://developer.apple.com/documentation/tipkit/tipuiview)*