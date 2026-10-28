---
url: "https://swiftpackageindex.com/carekit-apple/CareKit/main/documentation/carekitui/headerview"
framework: "CareKit/CareKitUI"
---

# HeaderView

**Framework**: CareKit/CareKitUI  
**Kind**: struct  
**Role**: Structure

Header used for most CareKit cards.

## Declaration

```swift
@MainActor
struct HeaderView
```

## Style

The image color can be set using the `.foregroundColor` modifier on the `HeaderView`. The card also supports styling using `careKitStyle(_:)`.

```
   +----------------------------------------+
   |                                        |
   |  <Title>                               |
   |  <Detail>                              |
   |                                        |
   +----------------------------------------+
```

## Topics

### Initializers
- [init(title: Text, detail: Text?, image: Image?)](./headerview/init%28title,detail,image%29.md)
  Create an instance.
### Instance Properties
- [var body: some View](./headerview/body.md)
### Default Implementations
- [View Implementations](./headerview/view-implementations.md)
- [View Implementations](./headerview/view-implementations.md)

## Relationships

### Conforms To
- Swift.Sendable
- SwiftUICore.View

## See Also

### Common view components
- [struct CardView](./cardview.md)
  A card whose content can be injected.
- [protocol OCKCardable](./ockcardable.md)
  Has the ability to display one’s self as a card. A card has a particular corner radius and shadow.
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

*[View on Swift Package Index](https://swiftpackageindex.com/carekit-apple/CareKit/main/documentation/carekitui/headerview)*