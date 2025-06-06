# AppIntentsPackage

**Framework**: App Intents  
**Kind**: protocol

A type that describes app intent definitions that aren’t part of an app bundle and their dependencies.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- tvOS 17.0+
- visionOS 1.0+
- watchOS 10.0+

## Declaration

```swift
protocol AppIntentsPackage
```

#### Overview

By default, your app intents are part of your application bundle. However, you may want to reuse app intents across apps or app extensions; for example, by bundling them with a framework you use across apps or Xcode targets.

To make app intent declarations available with your framework, it needs to define its own app intents package type as shown in the following example:

```swift
struct MyFrameworkPackage: AppIntentsPackage { }
```

To use the framework’s app intents in your app, define an app intents package in your app that depends on the framework’s app intents package; for example:

```swift
struct MyAppPackage: AppIntentsPackage {
   static var includedPackages: [any AppIntentsPackage.Type] {
       [MyFrameworkPackage.self]
   }
}
```

The app intents package `MyFrameworkPackage` in the example above doesn’t depend on another framework and its app intents. However, any app intents package can include a dependency on one or more other app intents packages. For example, the `MyAppPackage` could include the `MyFrameworkPackage` which itself could include another framework’s `OtherFrameworkPackage`.

## Topics

### Type Properties
- [static var includedPackages: [any AppIntentsPackage.Type]](appintentspackage/includedpackages.md)

## See Also

- [struct IntentDescription](intentdescription.md)
  The human-readable description and metadata for an app intent.
- [struct IntentDialog](intentdialog.md)
  The text you want the system to display, or speak, when requesting a value, asking for disambiguation, or confirming an action.
- [struct IntentDeprecation](intentdeprecation.md)
- [class IntentProjection](intentprojection.md)
  Projections for an app intent that returns non-optional values for parameters.
- [struct IntentSystemContext](intentsystemcontext.md)
  Information that the system makes available to an app intent while it performs its action.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/appintentspackage)*