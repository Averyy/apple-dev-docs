---
url: "https://swiftpackageindex.com/carekit-apple/CareKit/main/documentation/carekitui/ockanimatedbutton"
framework: "CareKit/CareKitUI"
---

# OCKAnimatedButton

**Framework**: CareKit/CareKitUI  
**Kind**: class  
**Role**: Class

A highlightable and selectable button that can be animated. The `isHighlighted` state can be specified with options, and the `isSelected` state can be handled automatically when the button is tapped.

## Declaration

```swift
@MainActor
class OCKAnimatedButton<Content> where Content : UIView
```

## Overview

The content view can be injected into the button. By default, the content is constrained to the button’s `layoutMarginGuide`.

## Topics

### Initializers
- [init?(coder: NSCoder)](./ockanimatedbutton/init%28coder%29.md)
- [init(contentView: Content?, highlightOptions: Set<HighlightOption>, handlesSelection: Bool)](./ockanimatedbutton/init%28contentview,highlightoptions,handlesselection%29.md)
  Create an animated button with injected content. The content will automatically be constrained to the button’s `layoutMarginGuide`.
### Instance Properties
- [let contentView: Content?](./ockanimatedbutton/contentview.md)
  The content inside the button.
- [var customStyle: OCKStyler?](./ockanimatedbutton/customstyle.md)
- [var handlesSelection: Bool](./ockanimatedbutton/handlesselection.md)
  Handle the selection state automatically when the button is tapped.
- [let highlightOptions: Set<HighlightOption>](./ockanimatedbutton/highlightoptions.md)
  The highlighted state options.
- [var isHighlighted: Bool](./ockanimatedbutton/ishighlighted.md)
  Set the highlighted state for the button. By default the highlighted state is animated.
- [var isSelected: Bool](./ockanimatedbutton/isselected.md)
  Set the selected state for the button. By default the selected state is not animated.
### Instance Methods
- [func didMoveToSuperview()](./ockanimatedbutton/didmovetosuperview%28%29.md)
- [func removeFromSuperview()](./ockanimatedbutton/removefromsuperview%28%29.md)
- [func setHighlighted(Bool, animated: Bool)](./ockanimatedbutton/sethighlighted%28_,animated%29.md)
  Set the highlighted state and update the `isHighlighted` property.
- [func setSelected(Bool, animated: Bool)](./ockanimatedbutton/setselected%28_,animated%29.md)
  Set the selected state and update the `isSelected` property.
- [func setStyleForHighlightedState(Bool)](./ockanimatedbutton/setstyleforhighlightedstate%28_%29.md)
  Set the style for the highlighted state. This function may be called in an animation block if the state is being animated.
- [func setStyleForSelectedState(Bool)](./ockanimatedbutton/setstyleforselectedstate%28_%29.md)
  Set the style for the selected state. This function may be called in an animation block if the state is being animated.
- [func styleDidChange()](./ockanimatedbutton/styledidchange%28%29.md)
- [func touchesEnded(Set<UITouch>, with: UIEvent?)](./ockanimatedbutton/touchesended%28_,with%29.md)
### Enumerations
- [OCKAnimatedButton.HighlightOption](./ockanimatedbutton/highlightoption.md)
  Options for displaying the the highlighted state of an `OCKAnimatedButton`.
### Default Implementations
- [OCKStylable Implementations](./ockanimatedbutton/ockstylable-implementations.md)

## Relationships

### Inherits From
- UIKit.UIControl
### Inherited By
- [OCKAddressButton](./ockaddressbutton.md)
- [OCKChecklistItemButton](./ockchecklistitembutton.md)
- [OCKCheckmarkButton](./ockcheckmarkbutton.md)
- [OCKCompletionRingButton](./ockcompletionringbutton.md)
- [OCKContactButton](./ockcontactbutton.md)
- [OCKLabeledButton](./ocklabeledbutton.md)
- [OCKLabeledCheckmarkButton](./ocklabeledcheckmarkbutton.md)
- [OCKLogItemButton](./ocklogitembutton.md)
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
- UIKit.UIContextMenuInteractionDelegate
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
- [class OCKHeaderView](./ockheaderview.md)
  A title and detail label. The view can also be configured to show a separator, icon image, and a detail disclosure arrow.
- [class OCKStackView](./ockstackview.md)
  A stack view that supports animating showing/hiding arranged subviews, and has the option of dynamically creating separators when arranged subviews are added.
- [class OCKSeparatorView](./ockseparatorview.md)
  Horizontal separator view.
- [class OCKLabel](./ocklabel.md)
  A label that handles animating state changes and provides accessibility features.
- [class OCKLabeledButton](./ocklabeledbutton.md)
  A button with a filled background color.
- [class OCKView](./ockview.md)
- [struct OCKResponsiveLayout](./ockresponsivelayout.md)
  Accessible view configuration that contains layout information for different `UserInterfaceSizeClass` and `UIContentSizeCategory` combinations.


---

*[View on Swift Package Index](https://swiftpackageindex.com/carekit-apple/CareKit/main/documentation/carekitui/ockanimatedbutton)*