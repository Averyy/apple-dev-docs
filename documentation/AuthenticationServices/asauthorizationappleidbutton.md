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
@MainActor
class ASAuthorizationAppleIDButton
```

#### Overview

Choose one of the built-in button styles and types, and change the corner radius of the button by setting the [`cornerRadius`](asauthorizationappleidbutton/cornerradius.md) property, but don’t otherwise modify the style of the button. Don’t use an Apple ID authorization button for any purpose other than to initiate the Sign In with Apple flow.

After the user taps the button, create a request using the provider, and then use an instance of [`ASAuthorizationController`](asauthorizationcontroller.md) to execute the request.

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
- [NSControl](../AppKit/NSControl.md)
- [UIControl](../UIKit/UIControl.md)
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
- [NSUserInterfaceItemIdentification](../AppKit/NSUserInterfaceItemIdentification.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)
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
- [UITraitChangeObservable](../UIKit/UITraitChangeObservable-67e94.md)
- [UITraitEnvironment](../UIKit/UITraitEnvironment.md)
- [UIUserActivityRestoring](../UIKit/UIUserActivityRestoring.md)

## See Also

- [class WKInterfaceAuthorizationAppleIDButton](../WatchKit/WKInterfaceAuthorizationAppleIDButton.md)
  A button that you can use to trigger a Sign in with Apple request.


---

*[View on Apple Developer](https://developer.apple.com/documentation/authenticationservices/asauthorizationappleidbutton)*