---
url: "https://swiftpackageindex.com/carekit-apple/CareKit/main/documentation/carekitui/ocklabel"
framework: "CareKit/CareKitUI"
---

# OCKLabel

**Framework**: CareKit/CareKitUI  
**Kind**: class  
**Role**: Class

A label that handles animating state changes and provides accessibility features.

## Declaration

```swift
@MainActor
class OCKLabel
```

#### Overview

To animate changes to the text, set `animatesTextChanges` to true.

To have the label automatically change its text size whenever the accessibility content size changes, use the initializer that takes a `textStyle` and `weight`.

## Topics

### Initializers
- [init()](./ocklabel/init%28%29.md)
  Create an instance of and `OCKLabel`. By default, the label will not animate text changes and will not scale with accessibility content size changes.
- [init?(coder: NSCoder)](./ocklabel/init%28coder%29.md)
- [init(textStyle: UIFont.TextStyle, weight: UIFont.Weight)](./ocklabel/init%28textstyle,weight%29.md)
  Create an instance of and `OCKLabel`. By default, the label will not animate text changes and will scale with accessibility content size changes.
### Instance Properties
- [var animatesTextChanges: Bool](./ocklabel/animatestextchanges.md)
  Flag determining whether to animate text changes.
- [var customStyle: OCKStyler?](./ocklabel/customstyle.md)
- [var text: String?](./ocklabel/text.md)
### Instance Methods
- [func didMoveToSuperview()](./ocklabel/didmovetosuperview%28%29.md)
- [func removeFromSuperview()](./ocklabel/removefromsuperview%28%29.md)
- [func styleDidChange()](./ocklabel/styledidchange%28%29.md)
- [func traitCollectionDidChange(UITraitCollection?)](./ocklabel/traitcollectiondidchange%28_%29.md)
### Default Implementations
- [OCKStylable Implementations](./ocklabel/ockstylable-implementations.md)

## Relationships

### Inherits From
- UIKit.UILabel
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
- UIKit.UIContentSizeCategoryAdjusting
- UIKit.UIDynamicItem
- UIKit.UIFocusEnvironment
- UIKit.UIFocusItem
- UIKit.UIFocusItemContainer
- UIKit.UILargeContentViewerItem
- UIKit.UILetterformAwareAdjusting
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
- [class OCKHeaderView](./ockheaderview.md)
  A title and detail label. The view can also be configured to show a separator, icon image, and a detail disclosure arrow.
- [class OCKStackView](./ockstackview.md)
  A stack view that supports animating showing/hiding arranged subviews, and has the option of dynamically creating separators when arranged subviews are added.
- [class OCKSeparatorView](./ockseparatorview.md)
  Horizontal separator view.
- [class OCKLabeledButton](./ocklabeledbutton.md)
  A button with a filled background color.
- [class OCKAnimatedButton](./ockanimatedbutton.md)
  A highlightable and selectable button that can be animated. The `isHighlighted` state can be specified with options, and the `isSelected` state can be handled automatically when the button is tapped.
- [class OCKView](./ockview.md)
- [struct OCKResponsiveLayout](./ockresponsivelayout.md)
  Accessible view configuration that contains layout information for different `UserInterfaceSizeClass` and `UIContentSizeCategory` combinations.


---

*[View on Swift Package Index](https://swiftpackageindex.com/carekit-apple/CareKit/main/documentation/carekitui/ocklabel)*