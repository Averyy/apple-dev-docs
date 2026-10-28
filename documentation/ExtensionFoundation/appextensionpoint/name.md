# AppExtensionPoint.Name

**Framework**: ExtensionFoundation  
**Kind**: struct  
**Role**: Structure

A type that defines the name of an extension point.

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
struct Name
```

## Mentions

- [Adding support for app extensions to your app](../adding-support-for-app-extensions-to-your-app.md)

## Overview

Add this type to each extension point definition you create in your host app. Provide a unique string for each of your app’s extension points. App extensions that want to bind to the extension point include this name in their binding.

## Topics

### Creating a name attribute
- [init(StaticString)](./name/init%28_%29.md)
  Initializes the name type with the specified string.

## See Also

### Declaring an extension point
- [AppExtensionPoint.Definition](./definition.md)
  A property wrapper that a host app uses to declare the extension points it supports.
- [AppExtensionPoint.UserInterface](./userinterface.md)
  A type with that indicates whether the extension point displays UI from an app extension.
- [AppExtensionPoint.EnhancedSecurity](./enhancedsecurity.md)
  A type that indicates whether an extension point requires extra security.
- [AppExtensionPoint.Scope](./scope.md)
  A type that regulates which app extensions may access an extension point.
- [AppExtensionPoint.Attribute](./attribute.md)
  An interface that marks a type as an extension point attribute.


---

*[View on Apple Developer](https://developer.apple.com/documentation/extensionfoundation/appextensionpoint/name)*