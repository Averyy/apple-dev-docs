# ExtensionKit

**Framework**: ExtensionKit  
**Kind**: module

Create executable bundles to extend the functionality of other apps by presenting a user interface.

**Availability**:
- iOS 16.1+
- iPadOS 16.1+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.0+
- visionOS 1.0+
- watchOS 10.0+

#### Overview

Extensions are executable code bundles, in one app that perform functions in a second,  app. Host apps declare  that control the kinds of functionality its extensions can implement. Extensions allow iOS and Mac apps to include code that runs inside system apps. For example, [`Messages`](https://developer.apple.com/documentation/Messages) provides extension points so apps can create [`Messages`](https://developer.apple.com/documentation/Messages). Messages automatically finds extension bundles that target its extension points and makes them available in its app drawer. A Mac app can also declare its own extension points so that other apps can extend the Mac app’s functionality.

Prior to macOS 13, apps use [`NSExtension`](https://developer.apple.com/documentation/BundleResources/Information-Property-List/NSExtension) property lists to declare and configure extensions. ExtensionKit supports this approach, but also adds the ability to configure extensions and extension points entirely in Swift code.

Extensions come in two basic forms: UI and non-UI.

An iMessage app, which can include sophisticated user interfaces — even entire games — is an example of a UI extension. [`SiriKit`](https://developer.apple.com/documentation/SiriKit) app intents, which gives people the ability to interact with your app using Siri, is an example of a non-UI extension.

Use ExtensionKit, in combination with [`ExtensionFoundation`](https://developer.apple.com/documentation/ExtensionFoundation), to create extensions and extension points for UI extensions. To create extensions with no user interface, use [`ExtensionFoundation`](https://developer.apple.com/documentation/ExtensionFoundation).

## Topics

### UI App Extensions
- [protocol AppExtensionScene](appextensionscene.md)
  A protocol that defines the user interface for an application extension.
- [struct AppExtensionSceneConfiguration](appextensionsceneconfiguration.md)
  An object that holds configuration options for an extension scene.
- [struct AppExtensionSceneBuilder](appextensionscenebuilder.md)
  A custom parameter attribute that constructs extension scenes from closures.
- [struct PrimitiveAppExtensionScene](primitiveappextensionscene.md)
  A primitive you use to compose specialized app extension points.
### Host Apps
- [class EXHostViewController](exhostviewcontroller.md)
  A view controller that hosts remote views provided by an extension.
- [class EXAppExtensionBrowserViewController](exappextensionbrowserviewcontroller.md)
  A view controller that allows users to enable and disable extensions.


---

*[View on Apple Developer](https://developer.apple.com/documentation/ExtensionKit)*