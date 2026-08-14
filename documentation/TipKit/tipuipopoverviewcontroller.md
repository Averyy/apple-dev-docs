# TipUIPopoverViewController

**Framework**: TipKit  
**Kind**: class

A view controller that displays a popover tip in UIKit applications.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- visionOS 1.0+

## Declaration

```swift
@MainActor
@objc @preconcurrency final class TipUIPopoverViewController
```

#### Overview

Use this view controller to present a tip you want to display using [`UIPopoverPresentationController`](https://developer.apple.com/documentation/uikit/uipopoverpresentationcontroller).

Presenting or dismissing TipUIPopoverViewController is done by listening to a tip’s [`shouldDisplayUpdates`](tip/shoulddisplayupdates.md) or [`statusUpdates`](tip/statusupdates.md).

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
    @IBOutlet weak var catTracksFeatureButton: UIButton!

    private var catTracksFeatureTip = CatTracksFeatureTip()
    private var tipObservationTask: Task<Void, Never>?
    private weak var tipPopoverController: TipUIPopoverViewController?

    override func viewDidAppear(_ animated: Bool) {
        super.viewDidAppear(animated)

        tipObservationTask = tipObservationTask ?? Task { @MainActor in
            for await shouldDisplay in catTracksFeatureTip.shouldDisplayUpdates {
                if shouldDisplay {
                    let popoverController = TipUIPopoverViewController(catTracksFeatureTip, sourceItem: catTracksFeatureButton)
                    present(popoverController, animated: animated)
                    tipPopoverController = popoverController
                }
                else {
                    if presentedViewController is TipUIPopoverViewController {
                        dismiss(animated: animated)
                        tipPopoverController = nil
                    }
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
- [convenience init(any Tip, sourceItem: any UIPopoverPresentationControllerSourceItem, actionHandler: (Tips.Action) -> Void)](tipuipopoverviewcontroller/init(_:sourceitem:actionhandler:).md)
  Initializes a popover controller with the specified tip.
- [init?(coder: NSCoder)](tipuipopoverviewcontroller/init(coder:).md)
- [init(nibName: String?, bundle: Bundle?)](tipuipopoverviewcontroller/init(nibname:bundle:).md)
### Instance Properties
- [var backgroundColor: UIColor?](tipuipopoverviewcontroller/backgroundcolor.md)
  The background color to use for the tip view.
- [var backgroundStyle: any ShapeStyle](tipuipopoverviewcontroller/backgroundstyle.md)
  The background style to use for the tip view.
- [var imageSize: CGSize](tipuipopoverviewcontroller/imagesize.md)
  Size of the image displayed in the tip view.
- [var imageStyle: (any ShapeStyle)?](tipuipopoverviewcontroller/imagestyle.md)
  Foreground style for the tip’s image.
- [var presentationDelegate: (any UIPopoverPresentationControllerDelegate)?](tipuipopoverviewcontroller/presentationdelegate.md)
  The popover presentation delegate, which lets you customize the behavior of a popover-based presentation.
- [var sourceItem: (any UIPopoverPresentationControllerSourceItem)?](tipuipopoverviewcontroller/sourceitem.md)
  The item on which to anchor the tip popover.
- [var viewStyle: any TipViewStyle](tipuipopoverviewcontroller/viewstyle.md)
  The given style for TipView within the view hierarchy.

## Relationships

### Inherits From
- [UIViewController](../uikit/uiviewcontroller.md)
### Conforms To
- [CVarArg](../swift/cvararg.md)
- [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../swift/customstringconvertible.md)
- [Equatable](../swift/equatable.md)
- [Hashable](../swift/hashable.md)
- [NSCoding](../foundation/nscoding.md)
- [NSExtensionRequestHandling](../foundation/nsextensionrequesthandling.md)
- [NSObjectProtocol](../objectivec/nsobjectprotocol.md)
- [NSTouchBarProvider](../appkit/nstouchbarprovider.md)
- [UIActivityItemsConfigurationProviding](../uikit/uiactivityitemsconfigurationproviding.md)
- [UIAppearanceContainer](../uikit/uiappearancecontainer.md)
- [UIContentContainer](../uikit/uicontentcontainer.md)
- [UIFocusEnvironment](../uikit/uifocusenvironment.md)
- [UIPasteConfigurationSupporting](../uikit/uipasteconfigurationsupporting.md)
- [UIResponderStandardEditActions](../uikit/uiresponderstandardeditactions.md)
- [UIStateRestoring](../uikit/uistaterestoring.md)
- [UITraitChangeObservable](../uikit/uitraitchangeobservable-67e94.md)
- [UITraitEnvironment](../uikit/uitraitenvironment.md)
- [UIUserActivityRestoring](../uikit/uiuseractivityrestoring.md)

## See Also

- [class TipUIView](tipuiview.md)
  A user interface element that represents a tip in UIKit applications.
- [class TipUICollectionViewCell](tipuicollectionviewcell.md)
  A collection view cell that embeds a tip.
- [class TipUICollectionReusableView](tipuicollectionreusableview.md)
  A UICollectionReusableView subclass that represents a tip.


---

*[View on Apple Developer](https://developer.apple.com/documentation/tipkit/tipuipopoverviewcontroller)*