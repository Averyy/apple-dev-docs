---
url: "https://swiftpackageindex.com/carekit-apple/CareKit/main/documentation/carekitui/ockresponsivelayout"
framework: "CareKit/CareKitUI"
---

# OCKResponsiveLayout

**Framework**: CareKit/CareKitUI  
**Kind**: struct  
**Role**: Structure

Accessible view configuration that contains layout information for different `UserInterfaceSizeClass` and `UIContentSizeCategory` combinations.

## Declaration

```swift
struct OCKResponsiveLayout<LayoutOption>
```

## Topics

### Structures
- [OCKResponsiveLayout.Rule](./ockresponsivelayout/rule.md)
  A layout rule for a given `UIContentSizeCategory`.
- [OCKResponsiveLayout.SizeClassRuleSet](./ockresponsivelayout/sizeclassruleset.md)
  A set of `UIContentSizeCategory` specific rules for a given size class.
### Initializers
- [init(defaultLayout: LayoutOption, anySizeClassRuleSet: [OCKResponsiveLayout.Rule<LayoutOption>], sizeClassSpecificRuleSets: [SizeClassRuleSet])](./ockresponsivelayout/init%28defaultlayout,anysizeclassruleset,sizeclassspecificrulesets%29.md)
  Initialize a `OCKResponsiveLayout` with default and specific size class rules.
### Instance Properties
- [let defaultRuleSet: SizeClassRuleSet](./ockresponsivelayout/defaultruleset.md)
  A default `SizeClassRuleSet` to apply for different `UIContentSizeCategory`’s when the exact `UserInterfaceSizeClass` is not important.
- [let sizeClassSpecificRuleSets: [SizeClassRuleSet]](./ockresponsivelayout/sizeclassspecificrulesets.md)
  A set of `UserInterfaceSizeClass` specific rule sets to provide different accessible layouts for specific size class combinations.
### Instance Methods
- [func responsiveLayoutRule(traitCollection: UITraitCollection) -> LayoutOption](./ockresponsivelayout/responsivelayoutrule%28traitcollection%29.md)
  Get a generic `LayoutOption` that has been mapped to a `UserInterfaceSizeClass` and `UIContentSizeCategory` for comparison provided by a given `UITraitCollection`.
### Type Aliases
- [OCKResponsiveLayout.SizeClass](./ockresponsivelayout/sizeclass.md)
  A lightweight typealias for a horizontal and vertical `UIUserInterfaceSizeClass` definition.

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
- [class OCKAnimatedButton](./ockanimatedbutton.md)
  A highlightable and selectable button that can be animated. The `isHighlighted` state can be specified with options, and the `isSelected` state can be handled automatically when the button is tapped.
- [class OCKView](./ockview.md)


---

*[View on Swift Package Index](https://swiftpackageindex.com/carekit-apple/CareKit/main/documentation/carekitui/ockresponsivelayout)*