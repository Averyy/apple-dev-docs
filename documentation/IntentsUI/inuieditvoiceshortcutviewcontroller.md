# INUIEditVoiceShortcutViewController

**Framework**: IntentsUI  
**Kind**: class  
**Role**: Class

A view controller that lets the user edit or remove an existing shortcut.

**Availability**:
- iOS 12.0+
- iPadOS 12.0+
- Mac Catalyst 13.1+
- macOS 12.0+
- visionOS 1.0+

## Declaration

```swift
class INUIEditVoiceShortcutViewController
```

*iOS, iPadOS, Mac Catalyst, tvOS, visionOS*

```objc
@interface INUIEditVoiceShortcutViewController : UIViewController
```

*macOS*

```objc
@interface INUIEditVoiceShortcutViewController : NSViewController
```

#### Overview

To let the user edit or remove a shortcut, create an instance of [`INUIEditVoiceShortcutViewController`](./inuieditvoiceshortcutviewcontroller.md) with the [`INVoiceShortcut`](../Intents/invoiceshortcut.md). Then present the view controller to the user. To receive notifications of changes made to the shortcut, set the controller’s [`delegate`](./inuieditvoiceshortcutviewcontroller/delegate.md) to an object that conforms to the [`INUIEditVoiceShortcutViewControllerDelegate`](./inuieditvoiceshortcutviewcontrollerdelegate.md) protocol.

## Topics

### Creating a Shortcut Editor
- [init(voiceShortcut: INVoiceShortcut)](./inuieditvoiceshortcutviewcontroller/init%28voiceshortcut%29.md)
  Creates a view controller with the shortcut to edit or remove.
### Handling View Controller Events
- [var delegate: (any INUIEditVoiceShortcutViewControllerDelegate)?](./inuieditvoiceshortcutviewcontroller/delegate.md)
  The object that retrieves notifications from the view controller.
- [protocol INUIEditVoiceShortcutViewControllerDelegate](./inuieditvoiceshortcutviewcontrollerdelegate.md)
  The protocol an object implements to receive notifications from the view controller that edits or removes a shortcut in Siri.

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
- [class INUIAddVoiceShortcutViewController](./inuiaddvoiceshortcutviewcontroller.md)
  A view controller that guides the user through the steps for adding a shortcut to Siri.


---

*[View on Apple Developer](https://developer.apple.com/documentation/intentsui/inuieditvoiceshortcutviewcontroller)*