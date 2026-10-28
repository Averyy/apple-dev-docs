---
url: "https://swiftpackageindex.com/carekit-apple/CareKit/main/documentation/carekitui/ockheaderview"
framework: "CareKit/CareKitUI"
---

# OCKHeaderView

**Framework**: CareKit/CareKitUI  
**Kind**: class  
**Role**: Class

A title and detail label. The view can also be configured to show a separator, icon image, and a detail disclosure arrow.

## Declaration

```swift
@MainActor
class OCKHeaderView
```

## Overview

```
   +----------------------------------------+
   | +----+                                 |
   | |icon|  Title             [detail      |
   | |img |  Detail             disclosure] |
   | +----+                                 |
   |                                        |
   |  ------------------------------------  |
   |                                        |
   +----------------------------------------+
```

## Topics

### Structures
- [OCKHeaderView.Configuration](./ockheaderview/configuration.md)
  Configuration for a header view.
### Initializers
- [init?(coder: NSCoder)](./ockheaderview/init%28coder%29.md)
- [init(configurationHandler: (inout Configuration) -> Void)](./ockheaderview/init%28configurationhandler%29.md)
  Create the view with a configuration block. The configuration block determines which views the header should show.
### Instance Properties
- [let contentStackView: OCKStackView](./ockheaderview/contentstackview.md)
  Vertical stack view that holds the main content.
- [let detailDisclosureImage: UIImageView?](./ockheaderview/detaildisclosureimage.md)
  The image on the trialing end of the view. The default image is an arrow. Depending on the configuration, this may be nil.
- [let detailLabel: OCKLabel](./ockheaderview/detaillabel.md)
  Multi-line detail label below `titleLabel`.
- [let iconImageView: UIImageView?](./ockheaderview/iconimageview.md)
  The image on the leading end of the text in the view. Depending on the configuration, this may be ni.
- [let titleLabel: OCKLabel](./ockheaderview/titlelabel.md)
  Multi-line title label above `detailLabel`
### Instance Methods
- [func styleDidChange()](./ockheaderview/styledidchange%28%29.md)
- [func traitCollectionDidChange(UITraitCollection?)](./ockheaderview/traitcollectiondidchange%28_%29.md)

## Relationships

### Inherits From
- [OCKView](./ockview.md)
### Conforms To
- Foundation.NSCoding
- [OCKStylable](./ockstylable.md)
- ObjectiveC.NSObjectProtocol
- QuartzCore.CALayerDelegate
- Swift.CVarArg
- Swift.CustomDebugStringConvertible
- Swift.CustomStringConvertible
- Swift.Equatable
- Swift.Hashable
- Swift.Sendable
- Swift.SendableMetatype
- UIKit.UIAccessibilityIdentification
- UIKit.UIActivityItemsConfigurationProviding
- UIKit.UIAppearance
- UIKit.UIAppearanceContainer
- UIKit.UIDynamicItem
- UIKit.UIFocusEnvironment
- UIKit.UIFocusItem
- UIKit.UIFocusItemContainer
- UIKit.UILargeContentViewerItem
- UIKit.UIPasteConfigurationSupporting
- UIKit.UIPopoverPresentationControllerSourceItem
- UIKit.UIResponderStandardEditActions
- UIKit.UITraitChangeObservable
- UIKit.UITraitEnvironment
- UIKit.UIUserActivityRestoring
- UIUtilities.UICoordinateSpace

## See Also

### Common view components
- [struct CardView](./cardview.md)
  A card whose content can be injected.
- [protocol OCKCardable](./ockcardable.md)
  Has the ability to display one’s self as a card. A card has a particular corner radius and shadow.
- [struct HeaderView](./headerview.md)
  Header used for most CareKit cards.
- [class OCKStackView](./ockstackview.md)
  A stack view that supports animating showing/hiding arranged subviews, and has the option of dynamically creating separators when arranged subviews are added.
- [class OCKSeparatorView](./ockseparatorview.md)
  Horizontal separator view.
- [class OCKLabel](./ocklabel.md)
  A label that handles animating state changes and provides accessibility features.
- [class OCKLabeledButton](./ocklabeledbutton.md)
  A button with a filled background color.
- [class OCKAnimatedButton](./ockanimatedbutton.md)
  A highlightable and selectable button that can be animated. The `isHighlighted` state can be specified with options, and the `isSelected` state can be handled automatically when the button is tapped.
- [class OCKView](./ockview.md)
- [struct OCKResponsiveLayout](./ockresponsivelayout.md)
  Accessible view configuration that contains layout information for different `UserInterfaceSizeClass` and `UIContentSizeCategory` combinations.


---

*[View on Swift Package Index](https://swiftpackageindex.com/carekit-apple/CareKit/main/documentation/carekitui/ockheaderview)*