# EXHostViewController

**Framework**: ExtensionKit  
**Kind**: class

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

- [Including extension-based UI in your interface](including-extension-based-ui-in-your-interface.md)

#### Overview

Present this view controller from your app’s interface to display the content for an associated app extension. Configure the view controller with the app extension identity and the specific scene you want to display. Use the associated delegate object to receive notifications when the app extension becomes active or inactive.

For more information about presenting this view controller and using it to display an app extension’s UI, see [`Including extension-based UI in your interface`](including-extension-based-ui-in-your-interface.md).

## Topics

### Configuring the view controller
- [var configuration: EXHostViewController.Configuration?](exhostviewcontroller/configuration-swift.property.md)
  The information the host view controller uses to fetch the appropriate scene from an app extension.
- [EXHostViewController.Configuration](exhostviewcontroller/configuration-swift.struct.md)
  An object that holds configuration options for a host view controller.
- [var placeholderView: UIView](exhostviewcontroller/placeholderview.md)
  The view to display when the view controller has no app extension content to display.
### Connecting to the app extension
- [func makeXPCConnection() throws -> NSXPCConnection](exhostviewcontroller/makexpcconnection.md)
  Initiates an XPC connection to the app extension’s scene.
### Responding to activation and deactivation events
- [var delegate: (any EXHostViewControllerDelegate)?](exhostviewcontroller/delegate.md)
  A custom delegate object you use to receive notifications about the activation and deactivation of the app extension.
- [protocol EXHostViewControllerDelegate](exhostviewcontrollerdelegate.md)
  An interface you use to track the activation and deactivation of an app extension.

## Relationships

### Inherits From
- [NSViewController](../appkit/nsviewcontroller.md)
- [UIViewController](../uikit/uiviewcontroller.md)
### Conforms To
- [CVarArg](../swift/cvararg.md)
- [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../swift/customstringconvertible.md)
- [Equatable](../swift/equatable.md)
- [Hashable](../swift/hashable.md)
- [NSCoding](../foundation/nscoding.md)
- [NSEditor](../appkit/nseditor.md)
- [NSExtensionRequestHandling](../foundation/nsextensionrequesthandling.md)
- [NSObjectProtocol](../objectivec/nsobjectprotocol.md)
- [NSSeguePerforming](../appkit/nssegueperforming.md)
- [NSStandardKeyBindingResponding](../appkit/nsstandardkeybindingresponding.md)
- [NSTouchBarProvider](../appkit/nstouchbarprovider.md)
- [NSUserActivityRestoring](../appkit/nsuseractivityrestoring.md)
- [NSUserInterfaceItemIdentification](../appkit/nsuserinterfaceitemidentification.md)
- [UIActivityItemsConfigurationProviding](../uikit/uiactivityitemsconfigurationproviding.md)
- [UIAppearanceContainer](../uikit/uiappearancecontainer.md)
- [UIContentContainer](../uikit/uicontentcontainer.md)
- [UIFocusEnvironment](../uikit/uifocusenvironment.md)
- [UIPasteConfigurationSupporting](../uikit/uipasteconfigurationsupporting.md)
- [UIResponderStandardEditActions](../uikit/uiresponderstandardeditactions.md)
- [UIStateRestoring](../uikit/uistaterestoring.md)
- [UITraitChangeObservable](../uikit/uitraitchangeobservable-67e94.md)
- [UITraitEnvironment](../uikit/uitraitenvironment.md)
- [UIUserActivityRestoring](../uikit/uiuseractivityrestoring.md)

## See Also

- [Displaying the app extensions available to your app](displaying-the-app-extensions-available-to-your-app.md)
  Show the app extensions available to your app, so that people can approve, enable, or disable them.
- [class EXAppExtensionBrowserViewController](exappextensionbrowserviewcontroller.md)
  A view controller that displays an interface to enable or disable the host app’s extensions.


---

*[View on Apple Developer](https://developer.apple.com/documentation/extensionkit/exhostviewcontroller)*