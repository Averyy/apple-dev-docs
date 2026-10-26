# PKIdentityButton

**Framework**: PassKit (Apple Pay and Wallet)  
**Kind**: class  
**Role**: Class

An object that displays a button to trigger the identity verification flow.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- visionOS 1.0+

## Declaration

```swift
class PKIdentityButton
```

```objc
@interface PKIdentityButton : UIControl
```

## Mentions

- [Requesting identity data from a Wallet pass](./requesting-identity-data-from-a-wallet-pass.md)

## Topics

### Creating an identity button
- [init(label: PKIdentityButton.Label, style: PKIdentityButton.Style)](./pkidentitybutton/init%28label,style%29.md)
  Creates a new identity button with the label and style.
- [+ buttonWithLabel:style:](./pkidentitybutton/buttonwithlabel_style_.md)
  Creates a new identity button with the label and style.
### Configuring the appearance
- [PKIdentityButton.Label](./pkidentitybutton/label.md)
  A type that indicates the available labels for an identity button.
- [PKIdentityButton.Style](./pkidentitybutton/style.md)
  A type that indicates the available appearances for an identity button.
- [var cornerRadius: CGFloat](./pkidentitybutton/cornerradius.md)
  The radius for the rounded corners on the button, in points.

## Relationships

### Inherits From
- [UIControl](../UIKit/uicontrol.md)
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
- [NSTouchBarProvider](../AppKit/nstouchbarprovider.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)
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
- [UITraitChangeObservable](../UIKit/uitraitchangeobservable-67e94.md)
- [UITraitEnvironment](../UIKit/uitraitenvironment.md)
- [UIUserActivityRestoring](../UIKit/uiuseractivityrestoring.md)

## See Also

### Identity sheet interactions and authorization
- [class PKIdentityAuthorizationController](./pkidentityauthorizationcontroller.md)
  An object that presents a sheet that prompts the user to allow a request for identity information.
- [class PKIdentityRequest](./pkidentityrequest.md)
  An object that represents a request for identity information from a Wallet pass.
- [class PKIdentityDocument](./pkidentitydocument.md)
  An object that represents the response to a request.
- [class PKIdentityElement](./pkidentityelement.md)
  An object that represents the elements an app requests from identity documents.
- [struct VerifyIdentityWithWalletButton](./verifyidentitywithwalletbutton.md)
  A type that displays a button to present the identity verification flow.
- [struct VerifyIdentityWithWalletButtonLabel](./verifyidentitywithwalletbuttonlabel.md)
  A type that represents the label you use with a verify identity button.
- [struct VerifyIdentityWithWalletButtonStyle](./verifyidentitywithwalletbuttonstyle.md)
  A type that represents the style you use with a verify identity button.


---

*[View on Apple Developer](https://developer.apple.com/documentation/passkit/pkidentitybutton)*