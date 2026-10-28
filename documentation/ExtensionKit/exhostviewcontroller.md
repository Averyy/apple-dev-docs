# EXHostViewController

**Framework**: ExtensionKit  
**Kind**: class  
**Role**: Class

A view controller that hosts remote views provided by an app extension.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 13.0+

## Declaration

```swift
class EXHostViewController
```

## Mentions

- [Including extension-based UI in your interface](./including-extension-based-ui-in-your-interface.md)

## Overview

Present this view controller from your app’s interface to display the content for an associated app extension. Configure the view controller with the app extension identity and the specific scene you want to display. Use the associated delegate object to receive notifications when the app extension becomes active or inactive.

For more information about presenting this view controller and using it to display an app extension’s UI, see [Including extension-based UI in your interface](./including-extension-based-ui-in-your-interface.md).

## Topics

### Configuring the view controller
- [var configuration: EXHostViewController.Configuration?](./exhostviewcontroller/configuration-swift.property.md)
  The information the host view controller uses to fetch the appropriate scene from an app extension.
- [EXHostViewController.Configuration](./exhostviewcontroller/configuration-swift.struct.md)
  An object that holds configuration options for a host view controller.
- [var placeholderView: UIView](./exhostviewcontroller/placeholderview.md)
  The view to display when the view controller has no app extension content to display.
### Connecting to the app extension
- [func makeXPCConnection() throws -> NSXPCConnection](./exhostviewcontroller/makexpcconnection%28%29.md)
  Initiates an XPC connection to the app extension’s scene.
### Responding to activation and deactivation events
- [var delegate: (any EXHostViewControllerDelegate)?](./exhostviewcontroller/delegate.md)
  A custom delegate object you use to receive notifications about the activation and deactivation of the app extension.
- [protocol EXHostViewControllerDelegate](./exhostviewcontrollerdelegate.md)
  An interface you use to track the activation and deactivation of an app extension.

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

### Host app presentation
- [Displaying the app extensions available to your app](./displaying-the-app-extensions-available-to-your-app.md)
  Show the app extensions available to your app, so that people can approve, enable, or disable them.
- [class EXAppExtensionBrowserViewController](./exappextensionbrowserviewcontroller.md)
  A view controller that displays an interface to enable or disable the host app’s extensions.


---

*[View on Apple Developer](https://developer.apple.com/documentation/extensionkit/exhostviewcontroller)*