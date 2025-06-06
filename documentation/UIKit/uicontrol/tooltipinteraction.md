# toolTipInteraction

**Framework**: UIKit  
**Kind**: property

The tooltip interaction associated with the control.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- visionOS 1.0+

## Declaration

```swift
@MainActor
var toolTipInteraction: UIToolTipInteraction? { get }
```

#### Discussion

When you set the [`toolTip`](uicontrol/tooltip.md) property, the control creates a [`UIToolTipInteraction`](uitooltipinteraction.md) object and assigns it to the [`toolTipInteraction`](uicontrol/tooltipinteraction.md) property.

If you want to change the text of the tooltip based the current state of your app or application logic, assign a [`UIToolTipInteractionDelegate`](uitooltipinteractiondelegate.md) object to [`toolTipInteraction`](uicontrol/tooltipinteraction.md)‘s [`delegate`](uitooltipinteraction/delegate.md) property. For example, the following code listing sets the tooltip’s default text and delegate for a shopping cart button:

```swift
lazy var shoppingCartButtonWithTooltip: UIButton = {
    var configuration = UIButton.Configuration.filled()
    configuration.title = "Add to Cart"
    configuration.image = UIImage(systemName: "cart", variant: .circle)
    configuration.imagePlacement = NSDirectionalRectEdge.leading
    configuration.imagePadding = 4
    
    let action = UIAction { [unowned self] _ in self.cartItemCount += 1 }
    
    let button = UIButton(configuration: configuration, primaryAction: action)
    button.toolTip = "Click to add the item to your cart. Your cart is empty."
    button.toolTipInteraction?.delegate = self
    
    return button
}()
```

Then the delegate returns a tooltip configuration containing text that states the number of items in the shopping cart by implementing the [`toolTipInteraction(_:configurationAt:)`](uitooltipinteractiondelegate/tooltipinteraction(_:configurationat:).md) method:

```swift
func toolTipInteraction(_ interaction: UIToolTipInteraction, configurationAt point: CGPoint) -> UIToolTipConfiguration? {
    
    let text: String
    switch cartItemCount {
    case 0:
        text = "Click to add the item to your cart. Your cart is empty."
    case 1:
        text = "Click to add the item to your cart. Your cart contains \(cartItemCount) item."
    default:
        text = "Click to add the item to your cart. Your cart contains \(cartItemCount) items."
    }
    
    return UIToolTipConfiguration(toolTip: text)
}
```

## See Also

- [var toolTip: String?](uicontrol/tooltip.md)
  The default text to display in the control’s tooltip.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uicontrol/tooltipinteraction)*