# Configuring the runtime behavior of your app intents

**Framework**: App Intents

Configure your app intents to run from your app in the foreground or background, or from an app extension in the background.

#### Overview

Most app intents run quietly in the background and deliver results back to the system, but some app intents need to bring your app to the foreground to complete their action. An app intent that plays a video, shows search results, or displays content in your app’s interface needs your app to be in the foreground to show the content. You might also define custom app intents that update your app’s interface or perform actions that require your app to be visible.

Because the system runs app intents, it’s responsible for bringing your app to the foreground when needed. Certain factors automatically affect whether an app intent runs in the foreground or background, such as the app intent’s type or where it runs. After that, the system relies on your code to specify the behavior you prefer. The system also relies on your code to direct foreground app intents to specific scenes of your app, which you might do to configure your views before the app becomes visible.

##### Place App Intent Code in the Correct Bundle

The placement of your app intent code affects whether the system is able to run your app in the foreground. When assembling your project, you can place your app intent–related code in your app bundle, in an App Intents extension, or in a shared framework that you include in both your app and app extension. Each location imposes specific restrictions on how the code runs:

- **App bundle**: Code in your app bundle can run in either the foreground or background.
- **App extensions**: Code in an App Intents extension or Widget extension runs only in the background.
- **Shared framework**: Code in a shared framework inherits the runtime behavior of where it’s included.

> **Note**: If you want to distribute app intents in a Swift Package, configure the package as a shareable binary framework. For more information, see [`Distributing binary frameworks as Swift packages`](https://developer.apple.com/documentation/xcode/distributing-binary-frameworks-as-swift-packages).

If an app intent can run in the foreground, its code needs to live in your app bundle or in a shared framework your app includes. At compile time, the compiler places metadata in each bundle about the app intents, app entities, and entity queries it contains. At runtime, the system uses this metadata to determine whether it can run the code from the app or app extension. When it actually needs to run an app intent or other code, it chooses a bundle based on various factors. For example, the system prefers to run a background app intent from your app extension, but might run it from your app if the app is already running.

If you place your app intent code in a shared framework, you need to take additional steps before the system can run that code from your app or app extension. At build time, the compiler places the metadata from your framework’s code in the framework’s bundle, not in the app or app extension’s bundle. As a result, the system doesn’t automatically know about the code in your framework, but you can fix that problem using an app intents package.

An app intents package is a custom type that adopts the [`AppIntentsPackage`](appintentspackage.md) protocol. The type itself requires little or no code, but its presence in a shared framework acts as a signpost for where to find your framework’s code. The following code shows how to define a type with this protocol in your shared framework.

```swift
struct MySharedFrameworkPackage: AppIntentsPackage { }
```

In your app or app extension, you use the same [`AppIntentsPackage`](appintentspackage.md) protocol to tell the system which shared frameworks you consider to be part of the bundle. In your code, define a custom type that adopts the [`AppIntentsPackage`](appintentspackage.md) protocol and implements the optional [`includedPackages`](appintentspackage/includedpackages.md) property. List the package type from your framework as one of the values of the property to associate its metadata with your app or app extension. The following example shows an implementation of this type in an app that includes the package from the shared framework in the previous example:

```swift
struct MyAppPackage: AppIntentsPackage {
    static var includedPackages: [any AppIntentsPackage.Type] {
        [MySharedFrameworkPackage.self]
    }
}
```

If you distribute app intent code among multiple shared frameworks, you can use the [`includedPackages`](appintentspackage/includedpackages.md) property in your framework’s package to inherit app intent code from other frameworks. This inheritance works the same way as for your app or app extension.

> **Note**: If you include the same shared framework in your app and app extension, you can restrict where an app intent runs using its [`allowedExecutionTargets`](appintent/allowedexecutiontargets.md) property. Implement this property in your app intent type to run it from your app, App Intents extension, Widget extension, or a combination of those bundles.

##### Choose the Preferred Runtime Modes for Your App Intent

When it’s time to run an app intent, the system consults the app intent’s [`supportedModes`](appintent/supportedmodes.md) property to determine whether to run it in the foreground or background. In addition to running either in the foreground or background, you can use this property to add nuanced runtime behaviors to your app intent. For example, you can tell the system you want the app intent to run in the background initially but transition your app to the foreground at some point later. If you don’t assign a value to this property, the system applies a default behavior based on various factors, but which typically results in your app intent running in the background.

The information in your app intent’s [`supportedModes`](appintent/supportedmodes.md) property is only a suggestion to the system. The location of your app intent code, the type of your app intent, and current system conditions also influence the system’s choice. In some cases, these other factors override the modes you specified:

- An app intent in your App Intents extension always runs in the background.
- For WidgetKit controls in a Widget extension, the system runs the control’s app intent from the extension in the background.
- The [`OpenIntent`](openintent.md), [`ShowInAppSearchResultsIntent`](showinappsearchresultsintent.md), [`PlayVideoIntent`](playvideointent.md), [`StartWorkoutIntent`](startworkoutintent.md), or [`LiveActivityIntent`](liveactivityintent.md) protocols automatically configure the [`supportedModes`](appintent/supportedmodes.md) property to run the app intent in the foreground.
- If your app is currently in the foreground, and your app intent is in both your app and App Intents extension, the system runs your app intent in the app regardless of the configured modes.

You can determine the system’s choice for running the app intent from the [`systemContext`](appintent/systemcontext.md) property. If your code is running in the background, you can also use this information to determine if running in the foreground is possible. If foreground transitions aren’t available, don’t call methods that initiate such a transition. For example, the system reports an error if you call the app intent’s [`continueInForeground(_:alwaysConfirm:)`](appintent/continueinforeground(_:alwaysconfirm:).md) method from an app extension. The following example shows code you might add to your [`perform()`](appintent/perform().md) method to determine if your app intent is currently running in the background and is able to transition to the foreground:

```swift
if systemContext.currentMode == .background {
   if systemContext.currentMode.canContinueInForeground {
      try await continueInForeground()
   } else {
      // The current conditions don't allow the app intent to continue in the foreground,
      // so it needs to continue in the background.
   }
}
```

##### Update Your Apps Interface Using Your App Intent

One of the main reasons to run an app intent in the foreground is to show something from your app’s interface. For example, an app intent that adopts the [`ShowInAppSearchResultsIntent`](showinappsearchresultsintent.md) protocol runs a search query and displays the results, and one that adopts the [`PlayVideoIntent`](playvideointent.md) protocol shows the app’s video playback interface. To make the required changes to your app’s interface, you need to write code to update your app’s views. However, you have several options for how to make the actual changes:

- **Leverage your app’s existing universal link support.** An [`OpenIntent`](openintent.md) type can use your app’s existing universal link support to open the specified item. Add the [`URLRepresentableIntent`](urlrepresentableintent.md) protocol to your app intent type, or configure your type with an entity that supports the [`URLRepresentableEntity`](urlrepresentableentity.md) protocol. For information about how to add universal links to your app, see [`Allowing apps and websites to link to your content`](https://developer.apple.com/documentation/xcode/allowing-apps-and-websites-to-link-to-your-content).
- **Send the app intent to one of your scenes.** When your app intent supports the [`TargetContentProvidingIntent`](targetcontentprovidingintent.md) or [`UISceneAppIntent`](uisceneappintent.md) protocol, the system directs the app intent to one of your app’s scenes. Use your scene code to configure its views using the contents of the app intent before your app moves to the foreground. For more information, see [`Directing app intents to your app’s scenes`](directing-app-intents-to-your-apps-scenes.md).
- **Configure your app’s interface from your app intent.** You can change views directly from your app intent’s [`perform()`](appintent/perform().md) method if you know what changes to make. The system runs this method after bringing your app to the foreground, so animate any changes you make for a smoother transition. Make all interface-related changes from your app’s main thread using a [`MainActor`](https://developer.apple.com/documentation/swift/mainactor) type or other approach.

## See Also

- [Creating your first app intent](creating-your-first-app-intent.md)
  Create your first app intent that makes your app available in system experiences like Spotlight or the Shortcuts app.
- [Accelerating app interactions with App Intents](acceleratingappinteractionswithappintents.md)
  Enable people to use your app’s features quickly through Siri, Spotlight, and Shortcuts.
- [Soup Chef with App Intents: Migrating custom intents](../sirikit/soup-chef-with-app-intents-migrating-custom-intents.md)
  Integrating App Intents to provide your appʼs actions to Siri and Shortcuts.
- [protocol AppIntent](appintent.md)
  An interface you use to express app-specific actions and make them available to the rest of the system.
- [App intent types](app-intent-types.md)
  Build your intents from types that define common behaviors such as opening or deleting items, playing or recording media, and more.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/configuring-the-runtime-behavior-of-your-app-intents)*