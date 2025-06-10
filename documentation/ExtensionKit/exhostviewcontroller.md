# EXHostViewController

**Framework**: ExtensionKit  
**Kind**: class

A view controller that hosts remote views provided by an extension.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst 26.0+ (Beta)
- macOS 13.0+

## Declaration

```swift
@MainActor
class EXHostViewController
```

## Topics

### Configuring the View Controller
- [var configuration: EXHostViewController.Configuration?](exhostviewcontroller/configuration-swift.property.md)
  The view controller’s configuration.
- [EXHostViewController.Configuration](exhostviewcontroller/configuration-swift.struct.md)
  An object that holds configuration options for a host view controller.
- [var placeholderView: UIView](exhostviewcontroller/placeholderview.md)
  A view that’s used when the view controller has no content to display.
### Connecting to the Extension
- [func makeXPCConnection() throws -> NSXPCConnection](exhostviewcontroller/makexpcconnection.md)
  Attempts to connect to the extension over XPC.
- [var delegate: (any EXHostViewControllerDelegate)?](exhostviewcontroller/delegate.md)
  The connection delegate.
- [protocol EXHostViewControllerDelegate](exhostviewcontrollerdelegate.md)
  The delegate for a hosted view controller.

## Relationships

### Inherits From
- [NSViewController](../AppKit/NSViewController.md)
- [UIViewController](../UIKit/UIViewController.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSCoding](../Foundation/NSCoding.md)
- [NSEditor](../AppKit/NSEditor.md)
- [NSExtensionRequestHandling](../Foundation/NSExtensionRequestHandling.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [NSSeguePerforming](../AppKit/NSSeguePerforming.md)
- [NSStandardKeyBindingResponding](../AppKit/NSStandardKeyBindingResponding.md)
- [NSTouchBarProvider](../AppKit/NSTouchBarProvider.md)
- [NSUserActivityRestoring](../AppKit/NSUserActivityRestoring.md)
- [NSUserInterfaceItemIdentification](../AppKit/NSUserInterfaceItemIdentification.md)
- [UIActivityItemsConfigurationProviding](../UIKit/UIActivityItemsConfigurationProviding.md)
- [UIAppearanceContainer](../UIKit/UIAppearanceContainer.md)
- [UIContentContainer](../UIKit/UIContentContainer.md)
- [UIFocusEnvironment](../UIKit/UIFocusEnvironment.md)
- [UIPasteConfigurationSupporting](../UIKit/UIPasteConfigurationSupporting.md)
- [UIResponderStandardEditActions](../UIKit/UIResponderStandardEditActions.md)
- [UIStateRestoring](../UIKit/UIStateRestoring.md)
- [UITraitChangeObservable](../UIKit/UITraitChangeObservable-67e94.md)
- [UITraitEnvironment](../UIKit/UITraitEnvironment.md)
- [UIUserActivityRestoring](../UIKit/UIUserActivityRestoring.md)

## See Also

- [class EXAppExtensionBrowserViewController](exappextensionbrowserviewcontroller.md)
  A view controller that allows users to enable and disable extensions.


---

*[View on Apple Developer](https://developer.apple.com/documentation/extensionkit/exhostviewcontroller)*