# TipUICollectionViewCell

**Framework**: TipKit  
**Kind**: class  
**Role**: Class

A collection view cell that embeds a tip.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- visionOS 1.0+

## Declaration

```swift
@MainActor
@objc @preconcurrency final class TipUICollectionViewCell
```

#### Overview

Use this cell to create a tip you want to display and layout as a [`UICollectionViewCell`](../UIKit/uicollectionviewcell.md). To configure the content and appearance of your cell, use the [`configureTip(_:arrowEdge:actionHandler:)`](./tipuicollectionviewcell/configuretip%28_,arrowedge,actionhandler%29.md) function and provide a tip along with an optional arrow edge and action handler. Set the background color of your tip view using [`backgroundColor`](./tipuicollectionviewcell/backgroundcolor.md).

Adding or removing TipUICollectionViewCell is done by listening to a tip’s [`shouldDisplayUpdates`](./tip/shoulddisplayupdates.md) or [`statusUpdates`](./tip/statusupdates.md).

```swift
import TipKit
import UIKit

class CatTracksCollectionViewController: UIViewController, UICollectionViewDataSource {
    var collectionView: UICollectionView
    var catTracksFeatureTip = CatTracksFeatureTip()

    override func viewDidLoad() {
        super.viewDidLoad()
        collectionView.register(TipUICollectionViewCell.self, forCellWithReuseIdentifier: "TipUICollectionViewCell")
    }

    override func viewDidAppear(_ animated: Bool) {
        super.viewDidAppear(animated)

        Task { @MainActor in
            for await shouldDisplay in catTracksFeatureTip.shouldDisplayUpdates {
                collectionView.reloadData()
            }
        }
    }
    
    func collectionView(_ collectionView: UICollectionView, numberOfItemsInSection section: Int) -> Int {
        if section == 0 {
            return catTracksFeatureTip.shouldDisplay ? 1 : 0
        }
        return dataStore.numberOfItemsInSection(section - 1)
    }

    func collectionView(_ collectionView: UICollectionView, cellForItemAt indexPath: IndexPath) -> UICollectionViewCell {
        if let indexPath.section == 0, let catTracksTipCell = collectionView.dequeueReusableCell(withReuseIdentifier: "TipUICollectionViewCell", for: indexPath) as? TipUICollectionViewCell {
            catTracksTipCell.configureTip(catTracksFeatureTip)
            return catTracksTipCell
        }
    }
}
```

## Topics

### Initializers
- [init?(coder: NSCoder)](./tipuicollectionviewcell/init%28coder%29.md)
- [init(frame: CGRect)](./tipuicollectionviewcell/init%28frame%29.md)
### Instance Properties
- [var backgroundColor: UIColor?](./tipuicollectionviewcell/backgroundcolor.md)
  The background color to use for the tip view.
- [var backgroundStyle: any ShapeStyle](./tipuicollectionviewcell/backgroundstyle.md)
  The background style to use for the tip view.
- [var cornerRadius: CGFloat](./tipuicollectionviewcell/cornerradius.md)
  Corner radius for the tip view.
- [var imageSize: CGSize](./tipuicollectionviewcell/imagesize.md)
  Size of the image displayed in the tip view.
- [var imageStyle: (any ShapeStyle)?](./tipuicollectionviewcell/imagestyle.md)
  Foreground style for the tip’s image.
- [var viewStyle: any TipViewStyle](./tipuicollectionviewcell/viewstyle.md)
  The given style for TipView within the view hierarchy
### Instance Methods
- [func configureTip(any Tip, arrowEdge: Edge?, actionHandler: (Tips.Action) -> Void) -> Self](./tipuicollectionviewcell/configuretip%28_,arrowedge,actionhandler%29.md)
  Configures the cell to display an embedded tip view.

## Relationships

### Inherits From
- [UICollectionViewCell](../UIKit/uicollectionviewcell.md)
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
- [class TipUICollectionReusableView](./tipuicollectionreusableview.md)
  A UICollectionReusableView subclass that represents a tip.


---

*[View on Apple Developer](https://developer.apple.com/documentation/tipkit/tipuicollectionviewcell)*