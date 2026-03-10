# Intent infrastructure

**Framework**: App Intents

Provide supplemental context for your intents, and create infrastructure to make app intents reusable across your apps.

#### Overview

The App Intents framework describes actions and content to the system for integration with Siri, the Shortcuts app, Spotlight, and more. Since your app intent code doesn’t exist in isolation, the framework also includes API to write infrastructure code. If your app intent requires access to shared dependencies to perform its functionality, use [`AppDependencyManager`](appdependencymanager.md) and [`AppDependency`](appdependency.md) to share dependencies across your intents, promote code reuse, and increase testability.

To take code reuse one step further and reuse intents across a suite of apps, consider creating a library of app intents with [`AppIntentsPackage`](appintentspackage.md). An advanced way to modularize code is creating an app intents extension with [`AppIntentsExtension`](appintentsextension.md). `AppIntentsExtension` serves as the registration mechanism for your app intents, and allows the system to discover and perform intents without launching your app.

In addition to providing API that helps you structure your app intent code base, the framework also provides you with information that allows you to adapt the behavior of your app intent for each invocation. For example, an intent might change its behavior depending on whether Siri, the Action button, widgets, or the Shortcuts app triggered the intent. To adapt your intent’s behavior, use [`IntentSystemContext`](intentsystemcontext.md) to access information about the environment at runtime.

For gracefully retiring older intents, [`IntentDeprecation`](intentdeprecation.md) helps you phase out deprecated functionality while guiding people to your newer alternatives, ensuring a smooth transition for their workflows.

## Topics

### Code reuse
- [class AppDependencyManager](appdependencymanager.md)
  An object that manages the registration and initialization of an app intent’s dependencies.
- [class AppDependency](appdependency.md)
  A property wrapper that resolves a registered dependency at runtime.
- [protocol AppIntentsExtension](appintentsextension.md)
  An interface for managing an extension’s configuration.
- [protocol AppIntentsPackage](appintentspackage.md)
  A type that describes app intent definitions that aren’t part of an app bundle and their dependencies.
### Supplementary content
- [struct IntentSystemContext](intentsystemcontext.md)
  Information that the system makes available to an app intent while it performs its action.
- [struct IntentDeprecation](intentdeprecation.md)

## See Also

- [Accelerating app interactions with App Intents](acceleratingappinteractionswithappintents.md)
  Enable people to use your app’s features quickly through Siri, Spotlight, and Shortcuts.
- [Creating your first app intent](creating-your-first-app-intent.md)
  Create your first app intent that makes your app available in system experiences like Spotlight or the Shortcuts app.
- [App intents](app-intents.md)
  Define the custom actions your app exposes to the system using specialized intents.
- [App intent domains](app-intent-domains.md)
  Make your app’s actions and content available to Siri and Apple Intelligence with assistant schemas.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/intent-infrastructure)*