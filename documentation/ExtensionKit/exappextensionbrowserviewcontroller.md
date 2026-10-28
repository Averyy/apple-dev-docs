# EXAppExtensionBrowserViewController

**Framework**: ExtensionKit  
**Kind**: class  
**Role**: Class

A view controller that displays an interface to enable or disable the host app’s extensions.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 13.0+

## Declaration

```swift
class EXAppExtensionBrowserViewController
```

## Mentions

- [Displaying the app extensions available to your app](./displaying-the-app-extensions-available-to-your-app.md)

## Overview

When your host app supports app extensions, use this view controller to give people a way to enable or disable those extensions. When you present this view controller, the system displays an out-of-process UI with a list of all app extensions that support your app’s extension points. Someone using your app can use the presented interface to enable or disable extensions selectively. App extensions you include inside your host app’s bundle are enabled by default, but extensions that ship in separate apps are disabled by default.

Present this view controller modally from your app, or embed the view controller as a child in one of your existing view controller interfaces. For example, you might choose to embed the view controller in a tab of your app’s preferences interface.

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

### Host app presentation
- [Displaying the app extensions available to your app](./displaying-the-app-extensions-available-to-your-app.md)
  Show the app extensions available to your app, so that people can approve, enable, or disable them.
- [class EXHostViewController](./exhostviewcontroller.md)
  A view controller that hosts remote views provided by an app extension.


---

*[View on Apple Developer](https://developer.apple.com/documentation/extensionkit/exappextensionbrowserviewcontroller)*