# ASAuthorizationAppleIDButton

**Framework**: Authentication Services  
**Kind**: class

A control you add to your interface that enables users to initiate the Sign In with Apple flow.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- macOS 10.15+
- tvOS 13.0+
- visionOS 1.0+

## Declaration

```swift
class ASAuthorizationAppleIDButton
```

#### Overview

Choose one of the built-in button styles and types, and change the corner radius of the button by setting the [`cornerRadius`](asauthorizationappleidbutton/cornerradius.md) property, but don’t otherwise modify the style of the button. Don’t use an Apple ID authorization button for any purpose other than to initiate the Sign In with Apple flow.

After the user taps the button, create a request using the provider, and then use an instance of [`ASAuthorizationController`](asauthorizationcontroller.md) to execute the request.

For more information about which Sign in with Apple buttons are available on different Apple platforms, see [`Displaying Sign in with Apple buttons in your app`](https://developer.apple.com/documentation/signinwithapple/displaying-sign-in-with-apple-buttons-in-your-app).

## Topics

### Initializers
- [init(authorizationButtonType: ASAuthorizationAppleIDButton.ButtonType, authorizationButtonStyle: ASAuthorizationAppleIDButton.Style)](asauthorizationappleidbutton/init(authorizationbuttontype:authorizationbuttonstyle:).md)
  Creates a new Sign In with Apple authorization button with the given type and style.
- [convenience init(type: ASAuthorizationAppleIDButton.ButtonType, style: ASAuthorizationAppleIDButton.Style)](asauthorizationappleidbutton/init(type:style:).md)
  Creates a new Sign In with Apple authorization button with the given type and style.
### Styling the Button
- [var cornerRadius: CGFloat](asauthorizationappleidbutton/cornerradius.md)
  The radius, in points, for the rounded corners on the Apple ID sign-in button.
- [ASAuthorizationAppleIDButton.Style](asauthorizationappleidbutton/style.md)
  A style for the authorization button.
- [ASAuthorizationAppleIDButton.ButtonType](asauthorizationappleidbutton/buttontype.md)
  A type for the authorization button.

## Relationships

### Inherits From
- [NSControl](../appkit/nscontrol.md)
- [UIControl](../uikit/uicontrol.md)
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
- [NSUserInterfaceItemIdentification](../appkit/nsuserinterfaceitemidentification.md)
- [Sendable](../swift/sendable.md)
- [SendableMetatype](../swift/sendablemetatype.md)
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
- [UITraitChangeObservable](../uikit/uitraitchangeobservable-67e94.md)
- [UITraitEnvironment](../uikit/uitraitenvironment.md)
- [UIUserActivityRestoring](../uikit/uiuseractivityrestoring.md)

## See Also

- [class WKInterfaceAuthorizationAppleIDButton](../watchkit/wkinterfaceauthorizationappleidbutton.md)
  A button that you can use to trigger a Sign in with Apple request.


---

*[View on Apple Developer](https://developer.apple.com/documentation/authenticationservices/asauthorizationappleidbutton)*