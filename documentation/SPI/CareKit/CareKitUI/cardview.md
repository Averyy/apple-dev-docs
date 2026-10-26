---
url: "https://swiftpackageindex.com/carekit-apple/CareKit/main/documentation/carekitui/cardview"
framework: "CareKit/CareKitUI"
---

# CardView

**Framework**: CareKit/CareKitUI  
**Kind**: struct  
**Role**: Structure

A card whose content can be injected.

## Declaration

```swift
@MainActor
struct CardView<Content> where Content : View
```

### Style

The card supports styling using `careKitStyle(_:)`.

### Composing Cards

To combine SwiftUI views with CareKit views that are already inside of a `CardView`, wrap the views in a new `CardView`. A CareKit view inside of a `CardView` is rendered without its border and background, since it inherits those visual affordances from the surrounding `CardView`.

```
CardView {
    CardView {
        Text("Only the outer card's visual features are rendered.")
    }
}
```

## Topics

### Initializers
- [init(content: () -> Content)](./cardview/init%28content%29.md)
  Create a card with injected content.
### Instance Properties
- [var body: some View](./cardview/body.md)
### Default Implementations
- [View Implementations](./cardview/view-implementations.md)
- [View Implementations](./cardview/view-implementations.md)

## Relationships

### Conforms To
- Swift.Sendable
- SwiftUICore.View

## See Also

### Common view components
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
- [struct OCKResponsiveLayout](./ockresponsivelayout.md)
  Accessible view configuration that contains layout information for different `UserInterfaceSizeClass` and `UIContentSizeCategory` combinations.


---

*[View on Swift Package Index](https://swiftpackageindex.com/carekit-apple/CareKit/main/documentation/carekitui/cardview)*