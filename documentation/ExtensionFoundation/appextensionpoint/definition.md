# AppExtensionPoint.Definition

**Framework**: ExtensionFoundation  
**Kind**: struct  
**Role**: Structure

A property wrapper that a host app uses to declare the extension points it supports.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- tvOS 26.0+
- visionOS 1.1+
- watchOS 26.0+

## Declaration

```swift
@resultBuilder
struct Definition
```

## Mentions

- [Adding support for app extensions to your app](../adding-support-for-app-extensions-to-your-app.md)

## Overview

Apply this property wrapper to variables that define your host app’s custom extension points. In the property that follows the definition, specify the name of your extension point and any additional attributes. The following example defines an extension point that runs app extensions with enhanced security:

```
extension AppExtensionPoint {
    @Definition
    static var MySecureFeature : AppExtensionPoint {
        Name(“MySecureFeature”)
        UserInterface(false)
        EnhancedSecurity(true)
    }
}
```

To ensure the system discovers your app’s extension points, add a user-defined build setting to your app target in Xcode. Set the build setting name to `EX_ENABLE_EXTENSION_POINT_GENERATION` and configure it with a value of `YES`. When this setting is present, the compiler adds an `.appext` file to your app’s bundle and places your definitions in it.

## Topics

### Wrapping the type
- [static func buildBlock<each T>(AppExtensionPoint.Name, repeat each T) -> AppExtensionPoint](./definition/buildblock%28_,_%29.md)

## See Also

### Declaring an extension point
- [AppExtensionPoint.Name](./name.md)
  A type that defines the name of an extension point.
- [AppExtensionPoint.UserInterface](./userinterface.md)
  A type with that indicates whether the extension point displays UI from an app extension.
- [AppExtensionPoint.EnhancedSecurity](./enhancedsecurity.md)
  A type that indicates whether an extension point requires extra security.
- [AppExtensionPoint.Scope](./scope.md)
  A type that regulates which app extensions may access an extension point.
- [AppExtensionPoint.Attribute](./attribute.md)
  An interface that marks a type as an extension point attribute.


---

*[View on Apple Developer](https://developer.apple.com/documentation/extensionfoundation/appextensionpoint/definition)*