# ASAuthorizationAppleIDButton

**Framework**: Authentication Services  
**Kind**: class  
**Role**: Class

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

*iOS, iPadOS, Mac Catalyst, tvOS, visionOS*

```objc
@interface ASAuthorizationAppleIDButton : UIControl
```

*macOS*

```objc
@interface ASAuthorizationAppleIDButton : NSControl
```

## Overview

Choose one of the built-in button styles and types, and change the corner radius of the button by setting the [`cornerRadius`](./asauthorizationappleidbutton/cornerradius.md) property, but don’t otherwise modify the style of the button. Don’t use an Apple ID authorization button for any purpose other than to initiate the Sign In with Apple flow.

After the user taps the button, create a request using the provider, and then use an instance of [`ASAuthorizationController`](./asauthorizationcontroller.md) to execute the request.

For more information about which Sign in with Apple buttons are available on different Apple platforms, see [Displaying Sign in with Apple buttons in your app](../SigninwithApple/displaying-sign-in-with-apple-buttons-in-your-app.md).

## Topics

### Initializers
- [init(authorizationButtonType: ASAuthorizationAppleIDButton.ButtonType, authorizationButtonStyle: ASAuthorizationAppleIDButton.Style)](./asauthorizationappleidbutton/init%28authorizationbuttontype,authorizationbuttonstyle%29.md)
  Creates a new Sign In with Apple authorization button with the given type and style.
- [convenience init(type: ASAuthorizationAppleIDButton.ButtonType, style: ASAuthorizationAppleIDButton.Style)](./asauthorizationappleidbutton/init%28type,style%29.md)
  Creates a new Sign In with Apple authorization button with the given type and style.
### Styling the Button
- [var cornerRadius: CGFloat](./asauthorizationappleidbutton/cornerradius.md)
  The radius, in points, for the rounded corners on the Apple ID sign-in button.
- [ASAuthorizationAppleIDButton.Style](./asauthorizationappleidbutton/style.md)
  A style for the authorization button.
- [ASAuthorizationAppleIDButton.ButtonType](./asauthorizationappleidbutton/buttontype.md)
  A type for the authorization button.

## Relationships

### Inherits From
- [NSControl](../AppKit/nscontrol.md)
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
- [NSUserInterfaceItemIdentification](../AppKit/nsuserinterfaceitemidentification.md)
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

### Offering Sign In with Apple
- [class WKInterfaceAuthorizationAppleIDButton](../WatchKit/wkinterfaceauthorizationappleidbutton.md)
  A button that you can use to trigger a Sign in with Apple request.


---

*[View on Apple Developer](https://developer.apple.com/documentation/authenticationservices/asauthorizationappleidbutton)*