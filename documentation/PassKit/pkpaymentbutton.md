# PKPaymentButton

**Framework**: PassKit (Apple Pay and Wallet)  
**Kind**: class  
**Role**: Class

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

*iOS, iPadOS, Mac Catalyst, visionOS*

```objc
@interface PKPaymentButton : UIButton
```

*macOS*

```objc
@interface PKPaymentButton : NSButton
```

#### Overview

After creating a [`PKPaymentButton`](./pkpaymentbutton.md) object, you choose the type and style of button, and the system provides a control with the correct content and appearance. See the [Human Interface Guidelines > Apple Pay](https://developer.apple.com/design/human-interface-guidelines/apple-pay/overview/buttons-and-marks/) for more information.

To trigger a payment through Apple Pay in a WatchKit app, use [`WKInterfacePaymentButton`](../WatchKit/wkinterfacepaymentbutton.md) instead.

## Topics

### Creating payment buttons
- [init(paymentButtonType: PKPaymentButtonType, paymentButtonStyle: PKPaymentButtonStyle)](./pkpaymentbutton/init%28paymentbuttontype,paymentbuttonstyle%29.md)
  Creates a new payment button with the specified type and style.
- [+ buttonWithType:style:](./pkpaymentbutton/buttonwithtype_style_.md)
  Creates a new payment button with the specified type and style.
### Configuring the appearance
- [enum PKPaymentButtonType](./pkpaymentbuttontype.md)
  The Apple Pay button types you can display to initiate Apple Pay transactions.
- [enum PKPaymentButtonStyle](./pkpaymentbuttonstyle.md)
  A type that indicates the available appearances for an Apple Pay button.
- [var cornerRadius: CGFloat](./pkpaymentbutton/cornerradius.md)
  The radius, in points, for the rounded corners on the button.
### Initializers
- [convenience init(paymentButtonType: PKPaymentButtonType, paymentButtonStyle: PKPaymentButtonStyle, disableCardArt: Bool)](./pkpaymentbutton/init%28paymentbuttontype,paymentbuttonstyle,disablecardart%29.md)
- [convenience init(type: PKPaymentButtonType, style: PKPaymentButtonStyle, disableCardArt: Bool)](./pkpaymentbutton/init%28type,style,disablecardart%29.md)
### Type Methods
- [+ buttonWithType:style:disableCardArt:](./pkpaymentbutton/buttonwithtype_style_disablecardart_.md)

## Relationships

### Inherits From
- [NSButton](../AppKit/nsbutton.md)
- [UIButton](../UIKit/uibutton.md)
### Conforms To
- [CALayerDelegate](../QuartzCore/calayerdelegate.md)
- [CLBodyIdentifiable](../CoreLocation/clbodyidentifiable.md)
- [CMBodyIdentifiable](../CoreMotion/cmbodyidentifiable.md)
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSAccessibilityButton](../AppKit/nsaccessibilitybutton.md)
- [NSAccessibilityElementProtocol](../AppKit/nsaccessibilityelementprotocol.md)
- [NSAccessibilityProtocol](../AppKit/nsaccessibilityprotocol.md)
- [NSAnimatablePropertyContainer](../AppKit/nsanimatablepropertycontainer.md)
- [NSAppearanceCustomization](../AppKit/nsappearancecustomization.md)
- [NSCoding](../Foundation/nscoding.md)
- [NSDraggingDestination](../AppKit/nsdraggingdestination.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)
- [NSStandardKeyBindingResponding](../AppKit/nsstandardkeybindingresponding.md)
- [NSTouchBarProvider](../AppKit/nstouchbarprovider.md)
- [NSUserActivityRestoring](../AppKit/nsuseractivityrestoring.md)
- [NSUserInterfaceCompression](../AppKit/nsuserinterfacecompression.md)
- [NSUserInterfaceItemIdentification](../AppKit/nsuserinterfaceitemidentification.md)
- [NSUserInterfaceValidations](../AppKit/nsuserinterfacevalidations.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)
- [UIAccessibilityContentSizeCategoryImageAdjusting](../UIKit/uiaccessibilitycontentsizecategoryimageadjusting.md)
- [UIAccessibilityIdentification](../UIKit/uiaccessibilityidentification.md)
- [UIActivityItemsConfigurationProviding](../UIKit/uiactivityitemsconfigurationproviding.md)
- [UIAppearance](../UIKit/uiappearance.md)
- [UIAppearanceContainer](../UIKit/uiappearancecontainer.md)
- [UIContextMenuInteractionDelegate](../UIKit/uicontextmenuinteractiondelegate.md)
- [UICoordinateSpace](../UIKit/uicoordinatespace.md)
- [UIDynamicItem](../UIKit/uidynamicitem.md)
- [UIFocusEnvironment](../UIKit/uifocusenvironment.md)
- [UIFocusItem](../UIKit/uifocusitem.md)
- [UIFocusItemContainer](../UIKit/uifocusitemcontainer.md)
- [UILargeContentViewerItem](../UIKit/uilargecontentvieweritem.md)
- [UIPasteConfigurationSupporting](../UIKit/uipasteconfigurationsupporting.md)
- [UIPopoverPresentationControllerSourceItem](../UIKit/uipopoverpresentationcontrollersourceitem.md)
- [UIResponderStandardEditActions](../UIKit/uiresponderstandardeditactions.md)
- [UISpringLoadedInteractionSupporting](../UIKit/uispringloadedinteractionsupporting.md)
- [UITraitChangeObservable](../UIKit/uitraitchangeobservable-67e94.md)
- [UITraitEnvironment](../UIKit/uitraitenvironment.md)
- [UIUserActivityRestoring](../UIKit/uiuseractivityrestoring.md)

## See Also

### Related Documentation
- [iOS Human Interface Guidelines](https://developer.apple.com/ios/human-interface-guidelines/)
### Apple Pay buttons
- [struct PayWithApplePayButton](./paywithapplepaybutton.md)
  A type that provides a button to pay with Apple pay.
- [struct PayWithApplePayButtonLabel](./paywithapplepaybuttonlabel.md)
- [struct PayWithApplePayButtonStyle](./paywithapplepaybuttonstyle.md)
- [struct PayWithApplePayButtonLabel](./paywithapplepaybuttonlabel.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/passkit/pkpaymentbutton)*