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
- [UIView](../uikit/uiview.md)
### Conforms To
- [CALayerDelegate](../quartzcore/calayerdelegate.md)
- [CLBodyIdentifiable](../corelocation/clbodyidentifiable.md)
- [CMBodyIdentifiable](../coremotion/cmbodyidentifiable.md)
- [CVarArg](../swift/cvararg.md)
- [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../swift/customstringconvertible.md)
- [Equatable](../swift/equatable.md)
- [Hashable](../swift/hashable.md)
- [NSCoding](../foundation/nscoding.md)
- [NSObjectProtocol](../objectivec/nsobjectprotocol.md)
- [Sendable](../swift/sendable.md)
- [SendableMetatype](../swift/sendablemetatype.md)
- [UIAccessibilityIdentification](../uikit/uiaccessibilityidentification.md)
- [UIActivityItemsConfigurationProviding](../uikit/uiactivityitemsconfigurationproviding.md)
- [UIAppearance](../uikit/uiappearance.md)
- [UIAppearanceContainer](../uikit/uiappearancecontainer.md)
- [UICoordinateSpace](../uikit/uicoordinatespace.md)
- [UIDynamicItem](../uikit/uidynamicitem.md)
- [UIFocusEnvironment](../uikit/uifocusenvironment.md)
- [UIFocusItem](../uikit/uifocusitem.md)
- [UIFocusItemContainer](../uikit/uifocusitemcontainer.md)
- [UILargeContentViewerItem](../uikit/uilargecontentvieweritem.md)
- [UIPasteConfigurationSupporting](../uikit/uipasteconfigurationsupporting.md)
- [UIPopoverPresentationControllerSourceItem](../uikit/uipopoverpresentationcontrollersourceitem.md)
- [UIResponderStandardEditActions](../uikit/uiresponderstandardeditactions.md)
- [UITraitChangeObservable](../uikit/uitraitchangeobservable-67e94.md)
- [UITraitEnvironment](../uikit/uitraitenvironment.md)
- [UIUserActivityRestoring](../uikit/uiuseractivityrestoring.md)

## See Also

- [struct PayLaterView](paylaterview.md)
  A view that displays the Apple Pay Later visual merchandising widget.


---

*[View on Apple Developer](https://developer.apple.com/documentation/passkit/pkpaylaterview)*