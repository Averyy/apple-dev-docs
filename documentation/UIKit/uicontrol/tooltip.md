# toolTip

**Framework**: UIKit  
**Kind**: property

The default text to display in the control’s tooltip.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- visionOS 1.0+

## Declaration

```swift
@MainActor
var toolTip: String? { get set }
```

#### Discussion

Set this property to the text that should appear in the tooltip. If you want your app to determine the tooltip text at a later time — for instance, to determine the text based on the current state of your app — set the [`delegate`](uitooltipinteraction/delegate.md) property of [`toolTipInteraction`](uicontrol/tooltipinteraction.md) after setting [`toolTip`](uicontrol/tooltip.md) with the default text. For example, the following code listing sets the tooltip’s default text and delegate for a shopping cart button:

```swift
let button = UIButton(configuration: configuration, primaryAction: action)
button.toolTip = "Click to add the item to your cart. Your cart is empty."
button.toolTipInteraction?.delegate = self
```

If the delegate implements the method [`toolTipInteraction(_:configurationAt:)`](uitooltipinteractiondelegate/tooltipinteraction(_:configurationat:).md), the tooltip ignores the default text set in the [`toolTip`](uicontrol/tooltip.md) property. For more information, see [`toolTipInteraction`](uicontrol/tooltipinteraction.md).

## See Also

- [var toolTipInteraction: UIToolTipInteraction?](uicontrol/tooltipinteraction.md)
  The tooltip interaction associated with the control.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uicontrol/tooltip)*