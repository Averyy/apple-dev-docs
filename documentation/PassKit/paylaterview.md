# PayLaterView

**Framework**: PassKit (Apple Pay and Wallet)  
**Kind**: struct

A view that displays the Apple Pay Later visual merchandising widget.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- visionOS ?+

## Declaration

```swift
@MainActor
@preconcurrency struct PayLaterView<FallbackView> where FallbackView : View
```

#### Overview

Use this view to display a widget that allows people to learn more about the Apple Pay Later feature.

## Topics

### Setting the view’s action
- [struct PayLaterViewAction](paylaterviewaction.md)
  Values you use to set the Apple Pay Later action.
### Styling the view
- [struct PayLaterViewDisplayStyle](paylaterviewdisplaystyle.md)
  Values you use to style an Apple Pay Later visual merchandising widget.
### Initializers
- [init(amount: Decimal, currency: Locale.Currency)](paylaterview/init(amount:currency:).md)

## Relationships

### Conforms To
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)
- [View](../SwiftUI/View.md)

## See Also

- [class PKPayLaterView](pkpaylaterview.md)
  A view that displays the Apple Pay Later visual merchandising widget.


---

*[View on Apple Developer](https://developer.apple.com/documentation/passkit/paylaterview)*