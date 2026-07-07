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
- visionOS ?+
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


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/appintentspackage)*