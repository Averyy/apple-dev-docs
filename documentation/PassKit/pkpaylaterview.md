# PKPayLaterView

**Framework**: PassKit (Apple Pay and Wallet)  
**Kind**: class  
**Role**: Class

A view that displays the Apple Pay Later visual merchandising widget.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- visionOS 1.0+

> **Deprecated**: Apple Pay Later is deprecated.

## Declaration

```swift
class PKPayLaterView
```

```objc
@interface PKPayLaterView : UIView
```

## Overview

Use this view to display a widget that allows people to learn more about the Apple Pay Later feature.

## Topics

### Creating the widget
- [convenience init(amount: Decimal, currency: Locale.Currency)](./pkpaylaterview/init%28amount,currency%29.md)
  Creates a new Apple Pay Later visual merchandising widget view with the shopping cart amount and currency you specify.
- [- initWithAmount:currencyCode:](./pkpaylaterview/initwithamount_currencycode_.md)
  Creates a new Apple Pay Later visual merchandising widget view with the amount and currency code you specify.
### Accessing information about the transaction
- [var amount: Decimal](./pkpaylaterview/amount-f3gs.md)
  The decimal value that represents the amount of the customer’s shopping cart or item pricing.
- [var currency: Locale.Currency](./pkpaylaterview/currency.md)
  The ISO-4217 currency code for the country or region of the merchant’s principle place of business.
- [amount](./pkpaylaterview/amount-1jzg2.md)
  The decimal value that represents the amount of the customer’s shopping cart or item pricing.
- [currencyCode](./pkpaylaterview/currencycode.md)
  A string that represents the ISO-4217 currency code for the country or region of the merchant’s principle place of business.
### Responding to changes in the view’s height
- [var delegate: any PKPayLaterViewDelegate](./pkpaylaterview/delegate.md)
  A delegate object that receives messages about the changes to the Apple Pay Later view.
- [protocol PKPayLaterViewDelegate](./pkpaylaterviewdelegate.md)
  Methods the framework calls when the Apple Pay Later view’s size changes.
### Setting the user action
- [var action: PKPayLaterAction](./pkpaylaterview/action.md)
  The information style that the Apple Pay Later view presents.
- [enum PKPayLaterAction](./pkpaylateraction.md)
  Values you use to set the Apple Pay Later action.
### Styling the view
- [var displayStyle: PKPayLaterDisplayStyle](./pkpaylaterview/displaystyle.md)
  The style to use when presenting the Apple Pay Later visual merchandising widget view.
- [enum PKPayLaterDisplayStyle](./pkpaylaterdisplaystyle.md)
  Values you use to style an Apple Pay Later visual merchandising widget.
### Validating transactions
- [enum PKPayLater](./pkpaylater.md)
  Functions for validating information the framework displays in an Apple Pay Later visual merchandising widget.
- [PKPayLaterValidateAmount](./pkpaylatervalidateamount.md)
  Checks if the framework can display Apple Pay Later visual merchandising widget information for the given amount and currency.

## Relationships

### Inherits From
- [UIView](../UIKit/uiview.md)
### Conforms To
- [CALayerDelegate](../QuartzCore/calayerdelegate.md)
- [CLBodyIdentifiable](../CoreLocation/clbodyidentifiable.md)
- [CMBodyIdentifiable](../CoreMotion/cmbodyidentifiable.md)
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSCoding](../Foundation/nscoding.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)
- [UIAccessibilityIdentification](../UIKit/uiaccessibilityidentification.md)
- [UIActivityItemsConfigurationProviding](../UIKit/uiactivityitemsconfigurationproviding.md)
- [UIAppearance](../UIKit/uiappearance.md)
- [UIAppearanceContainer](../UIKit/uiappearancecontainer.md)
- [UICoordinateSpace](../UIKit/uicoordinatespace.md)
- [UIDynamicItem](../UIKit/uidynamicitem.md)
- [UIFocusEnvironment](../UIKit/uifocusenvironment.md)
- [UIFocusItem](../UIKit/uifocusitem.md)
- [UIFocusItemContainer](../UIKit/uifocusitemcontainer.md)
- [UILargeContentViewerItem](../UIKit/uilargecontentvieweritem.md)
- [UIPasteConfigurationSupporting](../UIKit/uipasteconfigurationsupporting.md)
- [UIPopoverPresentationControllerSourceItem](../UIKit/uipopoverpresentationcontrollersourceitem.md)
- [UIResponderStandardEditActions](../UIKit/uiresponderstandardeditactions.md)
- [UITraitChangeObservable](../UIKit/uitraitchangeobservable-67e94.md)
- [UITraitEnvironment](../UIKit/uitraitenvironment.md)
- [UIUserActivityRestoring](../UIKit/uiuseractivityrestoring.md)

## See Also

### Deprecated
- [struct PayLaterView](./paylaterview.md)
  A view that displays the Apple Pay Later visual merchandising widget.


---

*[View on Apple Developer](https://developer.apple.com/documentation/passkit/pkpaylaterview)*