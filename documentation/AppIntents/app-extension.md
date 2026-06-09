# App extension

**Framework**: App Intents

Deliver app intents in an app extension or other package that lives outside your app’s code.

#### Overview

Create an app extension to run your custom app intents when your app isn’t running. To make it easier to share your intent code between your app and app extension, you can also place that code in a Swift package and import it into each target.

## Topics

### App extensions
- [protocol AppIntentsExtension](appintentsextension.md)
  An interface for managing an extension’s configuration.
### App intents in packages
- [protocol AppIntentsPackage](appintentspackage.md)
  A type that describes app intent definitions that aren’t part of an app bundle and their dependencies.

## See Also

- [App intents](app-intents.md)
  Make your app’s custom actions available to the system by using app intent types.
- [App entities](app-entities.md)
  Make your app’s core types and data concepts available to the system using app entity types.
- [App enums](app-enums.md)
  Make your app’s enumerations and predefined values available to the system by using app enum types.
- [Common data types](common-data-types.md)
  Use framework-defined types for common parameter and result data types such as contacts, files, currencies, and more.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/app-extension)*