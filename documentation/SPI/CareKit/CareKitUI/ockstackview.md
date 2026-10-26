---
url: "https://swiftpackageindex.com/carekit-apple/CareKit/main/documentation/carekitui/ockstackview"
framework: "CareKit/CareKitUI"
---

# OCKStackView

**Framework**: CareKit/CareKitUI  
**Kind**: class  
**Role**: Class

A stack view that supports animating showing/hiding arranged subviews, and has the option of dynamically creating separators when arranged subviews are added.

## Declaration

```swift
@MainActor
class OCKStackView
```

## Topics

### Initializers
- [init(style: Style)](./ockstackview/init%28style%29.md)
  Create the stack view with a style. A plain style is a typical stack view. A separated style will automatically create separators between arranged subviews whenever they’re added.
### Instance Properties
- [var arrangedSubviews: [UIView]](./ockstackview/arrangedsubviews.md)
  The ordered subviews. When the stack view is a separated style, this will not include the separators.
- [var customStyle: OCKStyler?](./ockstackview/customstyle.md)
- [var showsOuterSeparators: Bool](./ockstackview/showsouterseparators.md)
  Flag determines if the top and bottom separators are shown when the style of the stack view is separated
- [let style: Style](./ockstackview/style-swift.property.md)
  The style of the stack view.
### Instance Methods
- [func addArrangedSubview(UIView)](./ockstackview/addarrangedsubview%28_%29.md)
  Add a subview to the end of the stack view. If the style is separated, separators will automatically be added.
- [func addArrangedSubview(UIView, animated: Bool)](./ockstackview/addarrangedsubview%28_,animated%29.md)
  Add a subview to the end of the stack view. If the style is separated, separators will automatically be added. Provides the option to animate showing the new view.
- [func clear(animated: Bool)](./ockstackview/clear%28animated%29.md)
  Clear the views in the stack view.
- [func didMoveToSuperview()](./ockstackview/didmovetosuperview%28%29.md)
- [func insertArrangedSubview(UIView, at: Int)](./ockstackview/insertarrangedsubview%28_,at%29.md)
  Insert an arranged subview at a particular index in the stack view. If the style is separated, separators will automatically be added.
- [func insertArrangedSubview(UIView, at: Int, animated: Bool)](./ockstackview/insertarrangedsubview%28_,at,animated%29.md)
  Insert an arranged subview at a particular index in the stack view. If the style is separated, separators will be automatically added.  Provides the option to animate showing the new view.
- [func removeArrangedSubview(UIView)](./ockstackview/removearrangedsubview%28_%29.md)
  Remove an arranged subview from the stack view. If the style is separated, the separators will be automatically removed.
- [func removeArrangedSubview(UIView, animated: Bool)](./ockstackview/removearrangedsubview%28_,animated%29.md)
  Remove an arranged subview from the stack view. If the style is separated, the separators will be automatically removed. Option to animated the removal of the view.
- [func removeFromSuperview()](./ockstackview/removefromsuperview%28%29.md)
- [func styleDidChange()](./ockstackview/styledidchange%28%29.md)
### Enumerations
- [OCKStackView.Style](./ockstackview/style-swift.enum.md)
  The style for the stack view.
### Default Implementations
- [OCKStylable Implementations](./ockstackview/ockstylable-implementations.md)

## Relationships

### Inherits From
- UIKit.UIStackView
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
- [class OCKHeaderView](./ockheaderview.md)
  A title and detail label. The view can also be configured to show a separator, icon image, and a detail disclosure arrow.
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

*[View on Swift Package Index](https://swiftpackageindex.com/carekit-apple/CareKit/main/documentation/carekitui/ockstackview)*