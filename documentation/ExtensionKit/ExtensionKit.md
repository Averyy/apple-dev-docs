# ExtensionKit

**Framework**: ExtensionKit  
**Kind**: module

Make custom UI from an app extension available in a host app, and manage the list of enabled and disabled app extensions.

**Availability**:
- iOS 16.1+
- iPadOS 16.1+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.0+
- visionOS 1.0+
- watchOS 10.0+

## Mentions

- [Including extension-based UI in your interface](including-extension-based-ui-in-your-interface.md)
- [Displaying the app extensions available to your app](displaying-the-app-extensions-available-to-your-app.md)

#### Overview

An app extension is a code bundle that extends the capabilities of the system, or the capabilities of another app. At the system level, app extensions give you a way to add your custom capabilities to system features. For example, [`Creating a widget extension`](https://developer.apple.com/documentation/WidgetKit/Creating-a-Widget-Extension) display your app’s content in specific locations like the iOS Home Screen and Lock screen. System features typically provide a custom workflow for building the associated app extension, but still use this framework to implement support for those features.

If your app supports the incorporation of content from custom app extensions, adopt this framework and the [`ExtensionFoundation`](https://developer.apple.com/documentation/ExtensionFoundation) framework to support that capability. Adopt `ExtensionKit` in your app extensions and use it to define the views you want to display. In a host app, use this framework to present the interfaces that app extensions provide. This framework also provides a view controller to show enabled and disabled app extensions from your app’s interface.

## Topics

### Essentials
- [Including extension-based UI in your interface](including-extension-based-ui-in-your-interface.md)
  Build app extensions that provide a custom UI, and host those views in your app’s interface.
### UI definition
- [protocol AppExtensionScene](appextensionscene.md)
  An interface you use to provide a specific scene from your app extension’s UI.
- [struct PrimitiveAppExtensionScene](primitiveappextensionscene.md)
  A type you use to deliver the contents of your app-extension-based UI.
- [struct AppExtensionSceneBuilder](appextensionscenebuilder.md)
  A custom parameter attribute that constructs extension scenes from closures.
### App extension configuration
- [struct AppExtensionSceneConfiguration](appextensionsceneconfiguration.md)
  An object you use to configure an app extension that provides a custom UI.
### Host app presentation
- [Displaying the app extensions available to your app](displaying-the-app-extensions-available-to-your-app.md)
  Show the app extensions available to your app, so that people can approve, enable, or disable them.
- [class EXHostViewController](exhostviewcontroller.md)
  A view controller that hosts remote views provided by an app extension.
- [class EXAppExtensionBrowserViewController](exappextensionbrowserviewcontroller.md)
  A view controller that displays an interface to enable or disable the host app’s extensions.


---

*[View on Apple Developer](https://developer.apple.com/documentation/ExtensionKit)*