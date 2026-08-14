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
class PKPaymentButton
```

#### Overview

After creating a [`PKPaymentButton`](pkpaymentbutton.md) object, you choose the type and style of button, and the system provides a control with the correct content and appearance. See the [`Human Interface Guidelines > Apple Pay`](https://developer.apple.comhttps://developer.apple.com/design/human-interface-guidelines/apple-pay/overview/buttons-and-marks/) for more information.

To trigger a payment through Apple Pay in a WatchKit app, use [`WKInterfacePaymentButton`](https://developer.apple.com/documentation/watchkit/wkinterfacepaymentbutton) instead.

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
- [convenience init(paymentButtonType: PKPaymentButtonType, paymentButtonStyle: PKPaymentButtonStyle, disableCardArt: Bool)](pkpaymentbutton/init(paymentbuttontype:paymentbuttonstyle:disablecardart:).md)
- [convenience init(type: PKPaymentButtonType, style: PKPaymentButtonStyle, disableCardArt: Bool)](pkpaymentbutton/init(type:style:disablecardart:).md)

## Relationships

### Inherits From
- [NSButton](../appkit/nsbutton.md)
- [UIButton](../uikit/uibutton.md)
### Conforms To
- [CALayerDelegate](../quartzcore/calayerdelegate.md)
- [CLBodyIdentifiable](../corelocation/clbodyidentifiable.md)
- [CMBodyIdentifiable](../coremotion/cmbodyidentifiable.md)
- [CVarArg](../swift/cvararg.md)
- [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../swift/customstringconvertible.md)
- [Equatable](../swift/equatable.md)
- [Hashable](../swift/hashable.md)
- [NSAccessibilityButton](../appkit/nsaccessibilitybutton.md)
- [NSAccessibilityElementProtocol](../appkit/nsaccessibilityelementprotocol.md)
- [NSAccessibilityProtocol](../appkit/nsaccessibilityprotocol.md)
- [NSAnimatablePropertyContainer](../appkit/nsanimatablepropertycontainer.md)
- [NSAppearanceCustomization](../appkit/nsappearancecustomization.md)
- [NSCoding](../foundation/nscoding.md)
- [NSDraggingDestination](../appkit/nsdraggingdestination.md)
- [NSObjectProtocol](../objectivec/nsobjectprotocol.md)
- [NSStandardKeyBindingResponding](../appkit/nsstandardkeybindingresponding.md)
- [NSTouchBarProvider](../appkit/nstouchbarprovider.md)
- [NSUserActivityRestoring](../appkit/nsuseractivityrestoring.md)
- [NSUserInterfaceCompression](../appkit/nsuserinterfacecompression.md)
- [NSUserInterfaceItemIdentification](../appkit/nsuserinterfaceitemidentification.md)
- [NSUserInterfaceValidations](../appkit/nsuserinterfacevalidations.md)
- [Sendable](../swift/sendable.md)
- [SendableMetatype](../swift/sendablemetatype.md)
- [UIAccessibilityContentSizeCategoryImageAdjusting](../uikit/uiaccessibilitycontentsizecategoryimageadjusting.md)
- [UIAccessibilityIdentification](../uikit/uiaccessibilityidentification.md)
- [UIActivityItemsConfigurationProviding](../uikit/uiactivityitemsconfigurationproviding.md)
- [UIAppearance](../uikit/uiappearance.md)
- [UIAppearanceContainer](../uikit/uiappearancecontainer.md)
- [UIContextMenuInteractionDelegate](../uikit/uicontextmenuinteractiondelegate.md)
- [UICoordinateSpace](../uikit/uicoordinatespace.md)
- [UIDynamicItem](../uikit/uidynamicitem.md)
- [UIFocusEnvironment](../uikit/uifocusenvironment.md)
- [UIFocusItem](../uikit/uifocusitem.md)
- [UIFocusItemContainer](../uikit/uifocusitemcontainer.md)
- [UILargeContentViewerItem](../uikit/uilargecontentvieweritem.md)
- [UIPasteConfigurationSupporting](../uikit/uipasteconfigurationsupporting.md)
- [UIPopoverPresentationControllerSourceItem](../uikit/uipopoverpresentationcontrollersourceitem.md)
- [UIResponderStandardEditActions](../uikit/uiresponderstandardeditactions.md)
- [UISpringLoadedInteractionSupporting](../uikit/uispringloadedinteractionsupporting.md)
- [UITraitChangeObservable](../uikit/uitraitchangeobservable-67e94.md)
- [UITraitEnvironment](../uikit/uitraitenvironment.md)
- [UIUserActivityRestoring](../uikit/uiuseractivityrestoring.md)

## See Also

- [iOS Human Interface Guidelines](https://developer.apple.comhttps://developer.apple.com/ios/human-interface-guidelines/)
- [struct PayWithApplePayButton](paywithapplepaybutton.md)
  A type that provides a button to pay with Apple pay.
- [struct PayWithApplePayButtonLabel](paywithapplepaybuttonlabel.md)
- [struct PayWithApplePayButtonStyle](paywithapplepaybuttonstyle.md)
- [struct PayWithApplePayButtonLabel](paywithapplepaybuttonlabel.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/passkit/pkpaymentbutton)*