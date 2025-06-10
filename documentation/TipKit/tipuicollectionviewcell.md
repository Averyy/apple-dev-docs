# TipUICollectionViewCell

**Framework**: TipKit  
**Kind**: class

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

Use this cell to create a tip you want to display and layout as a [`UICollectionViewCell`](https://developer.apple.com/documentation/UIKit/UICollectionViewCell). To configure the content and appearance of your cell, use the [`configureTip(_:arrowEdge:actionHandler:)`](tipuicollectionviewcell/configuretip(_:arrowedge:actionhandler:).md) function and provide a tip along with an optional arrow edge and action handler. Set the background color of your tip view using [`backgroundColor`](tipuicollectionviewcell/backgroundcolor.md).

Adding or removing TipUICollectionViewCell is done by listening to a tip’s [`shouldDisplayUpdates`](tip/shoulddisplayupdates.md) or [`statusUpdates`](tip/statusupdates.md).

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
- [init?(coder: NSCoder)](tipuicollectionviewcell/init(coder:).md)
- [init(frame: CGRect)](tipuicollectionviewcell/init(frame:).md)
### Instance Properties
- [var backgroundColor: UIColor?](tipuicollectionviewcell/backgroundcolor.md)
  The background color to use for the tip view.
- [var backgroundStyle: any ShapeStyle](tipuicollectionviewcell/backgroundstyle.md)
  The background style to use for the tip view.
- [var cornerRadius: CGFloat](tipuicollectionviewcell/cornerradius.md)
  Corner radius for the tip view.
- [var imageSize: CGSize](tipuicollectionviewcell/imagesize.md)
  Size of the image displayed in the tip view.
- [var imageStyle: (any ShapeStyle)?](tipuicollectionviewcell/imagestyle.md)
  Foreground style for the tip’s image.
- [var viewStyle: any TipViewStyle](tipuicollectionviewcell/viewstyle.md)
  The given style for TipView within the view hierarchy
### Instance Methods
- [func configureTip(any Tip, arrowEdge: Edge?, actionHandler: (Tips.Action) -> Void) -> Self](tipuicollectionviewcell/configuretip(_:arrowedge:actionhandler:).md)
  Configures the cell to display an embedded tip view.

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
- [class TipUICollectionReusableView](tipuicollectionreusableview.md)
  A UICollectionReusableView subclass that represents a tip.


---

*[View on Apple Developer](https://developer.apple.com/documentation/tipkit/tipuicollectionviewcell)*