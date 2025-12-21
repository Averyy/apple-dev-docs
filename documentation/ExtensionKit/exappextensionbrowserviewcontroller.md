# EXAppExtensionBrowserViewController

**Framework**: ExtensionKit  
**Kind**: class

A view controller that displays an interface to enable or disable the host app’s extensions.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 13.0+

## Declaration

```swift
@MainActor
class EXAppExtensionBrowserViewController
```

## Mentions

- [Displaying the app extensions available to your app](displaying-the-app-extensions-available-to-your-app.md)

#### Overview

When your host app supports app extensions, use this view controller to give people a way to enable or disable those extensions. When you present this view controller, the system displays an out-of-process UI with a list of all app extensions that support your app’s extension points. Someone using your app can use the presented interface to enable or disable extensions selectively. App extensions you include inside your host app’s bundle are enabled by default, but extensions that ship in separate apps are disabled by default.

Present this view controller modally from your app, or embed the view controller as a child in one of your existing view controller interfaces. For example, you might choose to embed the view controller in a tab of your app’s preferences interface.

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
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)
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

- [Displaying the app extensions available to your app](displaying-the-app-extensions-available-to-your-app.md)
  Show the app extensions available to your app, so that people can approve, enable, or disable them.
- [class EXHostViewController](exhostviewcontroller.md)
  A view controller that hosts remote views provided by an app extension.


---

*[View on Apple Developer](https://developer.apple.com/documentation/extensionkit/exappextensionbrowserviewcontroller)*