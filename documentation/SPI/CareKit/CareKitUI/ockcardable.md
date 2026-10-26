---
url: "https://swiftpackageindex.com/carekit-apple/CareKit/main/documentation/carekitui/ockcardable"
framework: "CareKit/CareKitUI"
---

# OCKCardable

**Framework**: CareKit/CareKitUI  
**Kind**: protocol  
**Role**: Protocol

Has the ability to display one’s self as a card. A card has a particular corner radius and shadow.

## Declaration

```swift
protocol OCKCardable
```

## Topics

### Instance Properties
- [var cardView: UIView](./ockcardable/cardview.md)
  View that will be styled as a card. Should hold the `contentView`.
- [var contentView: UIView](./ockcardable/contentview.md)
  Holds the main content. Subviews should be added to this view.
### Instance Methods
- [func enableCardStyling(Bool, style: OCKStyler)](./ockcardable/enablecardstyling%28_,style%29.md)
  Turn the card styling on/off. If this view is stylable, this method should be called from the `styleDidChange` method. Note that shadow rasterizing is set on by default, and consequently a shadow cannot be set over a clear background.

## Relationships

### Conforming Types
- [OCKFeaturedContentView](./ockfeaturedcontentview.md)

## See Also

### Common view components
- [struct CardView](./cardview.md)
  A card whose content can be injected.
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
- [struct OCKResponsiveLayout](./ockresponsivelayout.md)
  Accessible view configuration that contains layout information for different `UserInterfaceSizeClass` and `UIContentSizeCategory` combinations.


---

*[View on Swift Package Index](https://swiftpackageindex.com/carekit-apple/CareKit/main/documentation/carekitui/ockcardable)*