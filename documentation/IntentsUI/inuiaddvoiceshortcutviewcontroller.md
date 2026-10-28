# INUIAddVoiceShortcutViewController

**Framework**: IntentsUI  
**Kind**: class  
**Role**: Class

A view controller that guides the user through the steps for adding a shortcut to Siri.

**Availability**:
- iOS 12.0+
- iPadOS 12.0+
- Mac Catalyst 13.1+
- macOS 12.0+
- visionOS 1.0+

## Declaration

```swift
class INUIAddVoiceShortcutViewController
```

*iOS, iPadOS, Mac Catalyst, tvOS, visionOS*

```objc
@interface INUIAddVoiceShortcutViewController : UIViewController
```

*macOS*

```objc
@interface INUIAddVoiceShortcutViewController : NSViewController
```

## Overview

When the user performs an action such as placing an order for tomato soup, the app should provide the option to add the action to Siri as a shortcut. To present this option in your app, use [`INUIAddVoiceShortcutButton`](./inuiaddvoiceshortcutbutton.md) to display an *Add to Siri* button. Using this button makes your app consistent with other apps that support Siri Shortcuts.

After creating the button, assign its action to a method that displays [`INUIAddVoiceShortcutViewController`](./inuiaddvoiceshortcutviewcontroller.md). This controller steps the user through the process of adding the shortcut to Siri.

To receive notifications of events from the view controller, set the delegate to an object that conforms to the [`INUIAddVoiceShortcutViewControllerDelegate`](./inuiaddvoiceshortcutviewcontrollerdelegate.md) protocol.

The listing below adds an *Add to Siri* button to a view and let the user record an invocation phrase.

```swift
// Add an "Add to Siri" button to a view.
func addSiriButton(to view: UIView) {
    let button = INUIAddVoiceShortcutButton(style: .blackOutline)
    button.translatesAutoresizingMaskIntoConstraints = false

    view.addSubview(button)
    view.centerXAnchor.constraint(equalTo: button.centerXAnchor).isActive = true
    view.centerYAnchor.constraint(equalTo: button.centerYAnchor).isActive = true

    button.addTarget(self, action: #selector(addToSiri(_:)), for: .touchUpInside)
}

// Present the Add Shortcut view controller after the
// user taps the "Add to Siri" button.
@objc
func addToSiri(_ sender: Any) {
    if let shortcut = INShortcut(intent: orderSoupOfTheDayIntent) {
        let viewController = INUIAddVoiceShortcutViewController(shortcut: shortcut)
        viewController.modalPresentationStyle = .formSheet
        viewController.delegate = self // Object conforming to `INUIAddVoiceShortcutViewControllerDelegate`.
        present(viewController, animated: true, completion: nil)
    }
}

```

## Topics

### Creating an Add Shortcut View Controller
- [init(shortcut: INShortcut)](./inuiaddvoiceshortcutviewcontroller/init%28shortcut%29.md)
  Creates a view controller with a shortcut the user can add to Siri.
### Handling View Controller Events
- [var delegate: (any INUIAddVoiceShortcutViewControllerDelegate)?](./inuiaddvoiceshortcutviewcontroller/delegate.md)
  The object that retrieves notifications from the view controller.
- [protocol INUIAddVoiceShortcutViewControllerDelegate](./inuiaddvoiceshortcutviewcontrollerdelegate.md)
  The protocol an object implements to receive notifications from the view controller adding a shortcut to Siri.

## Relationships

### Inherits From
- [NSViewController](../AppKit/nsviewcontroller.md)
- [UIViewController](../UIKit/uiviewcontroller.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSCoding](../Foundation/nscoding.md)
- [NSEditor](../AppKit/nseditor.md)
- [NSExtensionRequestHandling](../Foundation/nsextensionrequesthandling.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)
- [NSSeguePerforming](../AppKit/nssegueperforming.md)
- [NSStandardKeyBindingResponding](../AppKit/nsstandardkeybindingresponding.md)
- [NSTouchBarProvider](../AppKit/nstouchbarprovider.md)
- [NSUserActivityRestoring](../AppKit/nsuseractivityrestoring.md)
- [NSUserInterfaceItemIdentification](../AppKit/nsuserinterfaceitemidentification.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)
- [UIActivityItemsConfigurationProviding](../UIKit/uiactivityitemsconfigurationproviding.md)
- [UIAppearanceContainer](../UIKit/uiappearancecontainer.md)
- [UIContentContainer](../UIKit/uicontentcontainer.md)
- [UIFocusEnvironment](../UIKit/uifocusenvironment.md)
- [UIPasteConfigurationSupporting](../UIKit/uipasteconfigurationsupporting.md)
- [UIResponderStandardEditActions](../UIKit/uiresponderstandardeditactions.md)
- [UIStateRestoring](../UIKit/uistaterestoring.md)
- [UITraitChangeObservable](../UIKit/uitraitchangeobservable-67e94.md)
- [UITraitEnvironment](../UIKit/uitraitenvironment.md)
- [UIUserActivityRestoring](../UIKit/uiuseractivityrestoring.md)

## See Also

### Shortcut Editors
- [class INUIEditVoiceShortcutViewController](./inuieditvoiceshortcutviewcontroller.md)
  A view controller that lets the user edit or remove an existing shortcut.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intentsui/inuiaddvoiceshortcutviewcontroller)*