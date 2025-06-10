# PKPaymentButton

**Framework**: PassKit (Apple Pay and Wallet)  
**Kind**: class

An object that displays a button either to trigger payments through Apple Pay or to prompt the user to set up a card.

**Availability**:
- iOS 8.3+
- iPadOS 8.3+
- Mac Catalyst 13.1+
- macOS 11.0+
- visionOS 1.0+

## Declaration

```swift
@MainActor
class PKPaymentButton
```

#### Overview

After creating a [`PKPaymentButton`](pkpaymentbutton.md) object, you choose the type and style of button, and the system provides a control with the correct content and appearance. See the [`Human Interface Guidelines > Apple Pay`](https://developer.apple.comhttps://developer.apple.com/design/human-interface-guidelines/apple-pay/overview/buttons-and-marks/) for more information.

To trigger a payment through Apple Pay in a WatchKit app, use [`WKInterfacePaymentButton`](https://developer.apple.com/documentation/WatchKit/WKInterfacePaymentButton) instead.

## Topics

### Creating payment buttons
- [init(paymentButtonType: PKPaymentButtonType, paymentButtonStyle: PKPaymentButtonStyle)](pkpaymentbutton/init(paymentbuttontype:paymentbuttonstyle:).md)
  Creates a new payment button with the specified type and style.
### Configuring the appearance
- [enum PKPaymentButtonType](pkpaymentbuttontype.md)
  The Apple Pay button types you can display to initiate Apple Pay transactions.
- [enum PKPaymentButtonStyle](pkpaymentbuttonstyle.md)
  A type that indicates the available appearances for an Apple Pay button.
- [var cornerRadius: CGFloat](pkpaymentbutton/cornerradius.md)
  The radius, in points, for the rounded corners on the button.
### Initializers
- [convenience init(type: PKPaymentButtonType, style: PKPaymentButtonStyle, disableCardArt: Bool)](pkpaymentbutton/init(type:style:disablecardart:).md)

## Relationships

### Inherits From
- [NSButton](../AppKit/NSButton.md)
- [UIButton](../UIKit/UIButton.md)
### Conforms To
- [CALayerDelegate](../QuartzCore/CALayerDelegate.md)
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSAccessibilityButton](../AppKit/NSAccessibilityButton.md)
- [NSAccessibilityElementProtocol](../AppKit/NSAccessibilityElementProtocol.md)
- [NSAccessibilityProtocol](../AppKit/NSAccessibilityProtocol.md)
- [NSAnimatablePropertyContainer](../AppKit/NSAnimatablePropertyContainer.md)
- [NSAppearanceCustomization](../AppKit/NSAppearanceCustomization.md)
- [NSCoding](../Foundation/NSCoding.md)
- [NSDraggingDestination](../AppKit/NSDraggingDestination.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [NSStandardKeyBindingResponding](../AppKit/NSStandardKeyBindingResponding.md)
- [NSTouchBarProvider](../AppKit/NSTouchBarProvider.md)
- [NSUserActivityRestoring](../AppKit/NSUserActivityRestoring.md)
- [NSUserInterfaceCompression](../AppKit/NSUserInterfaceCompression.md)
- [NSUserInterfaceItemIdentification](../AppKit/NSUserInterfaceItemIdentification.md)
- [NSUserInterfaceValidations](../AppKit/NSUserInterfaceValidations.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)
- [UIAccessibilityContentSizeCategoryImageAdjusting](../UIKit/UIAccessibilityContentSizeCategoryImageAdjusting.md)
- [UIAccessibilityIdentification](../UIKit/UIAccessibilityIdentification.md)
- [UIActivityItemsConfigurationProviding](../UIKit/UIActivityItemsConfigurationProviding.md)
- [UIAppearance](../UIKit/UIAppearance.md)
- [UIAppearanceContainer](../UIKit/UIAppearanceContainer.md)
- [UIContextMenuInteractionDelegate](../UIKit/UIContextMenuInteractionDelegate.md)
- [UICoordinateSpace](../UIKit/UICoordinateSpace.md)
- [UIDynamicItem](../UIKit/UIDynamicItem.md)
- [UIFocusEnvironment](../UIKit/UIFocusEnvironment.md)
- [UIFocusItem](../UIKit/UIFocusItem.md)
- [UIFocusItemContainer](../UIKit/UIFocusItemContainer.md)
- [UILargeContentViewerItem](../UIKit/UILargeContentViewerItem.md)
- [UIPasteConfigurationSupporting](../UIKit/UIPasteConfigurationSupporting.md)
- [UIPopoverPresentationControllerSourceItem](../UIKit/UIPopoverPresentationControllerSourceItem.md)
- [UIResponderStandardEditActions](../UIKit/UIResponderStandardEditActions.md)
- [UISpringLoadedInteractionSupporting](../UIKit/UISpringLoadedInteractionSupporting.md)
- [UITraitChangeObservable](../UIKit/UITraitChangeObservable-67e94.md)
- [UITraitEnvironment](../UIKit/UITraitEnvironment.md)
- [UIUserActivityRestoring](../UIKit/UIUserActivityRestoring.md)

## See Also

- [iOS Human Interface Guidelines](https://developer.apple.comhttps://developer.apple.com/ios/human-interface-guidelines/)
- [struct PayWithApplePayButton](paywithapplepaybutton.md)
- [struct PayWithApplePayButtonLabel](paywithapplepaybuttonlabel.md)
- [struct PayWithApplePayButtonStyle](paywithapplepaybuttonstyle.md)
- [struct PayWithApplePayButtonLabel](paywithapplepaybuttonlabel.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/passkit/pkpaymentbutton)*