# PKPayLaterView

**Framework**: PassKit (Apple Pay and Wallet)  
**Kind**: class

A view that displays the Apple Pay Later visual merchandising widget.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- visionOS 1.0+

## Declaration

```swift
@MainActor
class PKPayLaterView
```

#### Overview

Use this view to display a widget that allows people to learn more about the Apple Pay Later feature.

## Topics

### Creating the widget
- [convenience init(amount: Decimal, currency: Locale.Currency)](pkpaylaterview/init(amount:currency:).md)
  Creates a new Apple Pay Later visual merchandising widget view with the shopping cart amount and currency you specify.
### Accessing information about the transaction
- [var amount: Decimal](pkpaylaterview/amount-f3gs.md)
  The decimal value that represents the amount of the customer’s shopping cart or item pricing.
- [var currency: Locale.Currency](pkpaylaterview/currency.md)
  The ISO-4217 currency code for the country or region of the merchant’s principle place of business.
### Responding to changes in the view’s height
- [var delegate: any PKPayLaterViewDelegate](pkpaylaterview/delegate.md)
  A delegate object that receives messages about the changes to the Apple Pay Later view.
- [protocol PKPayLaterViewDelegate](pkpaylaterviewdelegate.md)
  Methods the framework calls when the Apple Pay Later view’s size changes.
### Setting the user action
- [var action: PKPayLaterAction](pkpaylaterview/action.md)
  The information style that the Apple Pay Later view presents.
- [enum PKPayLaterAction](pkpaylateraction.md)
  Values you use to set the Apple Pay Later action.
### Styling the view
- [var displayStyle: PKPayLaterDisplayStyle](pkpaylaterview/displaystyle.md)
  The style to use when presenting the Apple Pay Later visual merchandising widget view.
- [enum PKPayLaterDisplayStyle](pkpaylaterdisplaystyle.md)
  Values you use to style an Apple Pay Later visual merchandising widget.
### Validating transactions
- [enum PKPayLater](pkpaylater.md)
  Functions for validating information the framework displays in an Apple Pay Later visual merchandising widget.

## Relationships

### Inherits From
- [UIView](../UIKit/UIView.md)
### Conforms To
- [CALayerDelegate](../QuartzCore/CALayerDelegate.md)
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSCoding](../Foundation/NSCoding.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)
- [UIAccessibilityIdentification](../UIKit/UIAccessibilityIdentification.md)
- [UIActivityItemsConfigurationProviding](../UIKit/UIActivityItemsConfigurationProviding.md)
- [UIAppearance](../UIKit/UIAppearance.md)
- [UIAppearanceContainer](../UIKit/UIAppearanceContainer.md)
- [UICoordinateSpace](../UIKit/UICoordinateSpace.md)
- [UIDynamicItem](../UIKit/UIDynamicItem.md)
- [UIFocusEnvironment](../UIKit/UIFocusEnvironment.md)
- [UIFocusItem](../UIKit/UIFocusItem.md)
- [UIFocusItemContainer](../UIKit/UIFocusItemContainer.md)
- [UILargeContentViewerItem](../UIKit/UILargeContentViewerItem.md)
- [UIPasteConfigurationSupporting](../UIKit/UIPasteConfigurationSupporting.md)
- [UIPopoverPresentationControllerSourceItem](../UIKit/UIPopoverPresentationControllerSourceItem.md)
- [UIResponderStandardEditActions](../UIKit/UIResponderStandardEditActions.md)
- [UITraitChangeObservable](../UIKit/UITraitChangeObservable-67e94.md)
- [UITraitEnvironment](../UIKit/UITraitEnvironment.md)
- [UIUserActivityRestoring](../UIKit/UIUserActivityRestoring.md)

## See Also

- [struct PayLaterView](paylaterview.md)
  A view that displays the Apple Pay Later visual merchandising widget.


---

*[View on Apple Developer](https://developer.apple.com/documentation/passkit/pkpaylaterview)*