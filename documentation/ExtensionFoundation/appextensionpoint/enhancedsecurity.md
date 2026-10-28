# AppExtensionPoint.EnhancedSecurity

**Framework**: ExtensionFoundation  
**Kind**: struct  
**Role**: Structure

A type that indicates whether an extension point requires extra security.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+

## Declaration

```swift
struct EnhancedSecurity
```

## Mentions

- [Building an app extension to support a host app](../building-an-app-extension-to-support-a-host-app.md)

## Overview

Add the `EnhancedSecurity` type to your extension point definition to indicate its security requirements. Initialize the type with a value of `true` if you require app extensions to run in a highly restrictive sandbox, or `false` if you don’t. For more information about configuring the sandbox environment, see [Enabling enhanced security for your app](../../Xcode/enabling-enhanced-security-for-your-app.md).

## Topics

### Creating a security attribute
- [init(Bool)](./enhancedsecurity/init%28_%29.md)
  Initializes the type with the specified Boolean value.

## Relationships

### Conforms To
- [AppExtensionPoint.Attribute](./attribute.md)

## See Also

### Declaring an extension point
- [AppExtensionPoint.Definition](./definition.md)
  A property wrapper that a host app uses to declare the extension points it supports.
- [AppExtensionPoint.Name](./name.md)
  A type that defines the name of an extension point.
- [AppExtensionPoint.UserInterface](./userinterface.md)
  A type with that indicates whether the extension point displays UI from an app extension.
- [AppExtensionPoint.Scope](./scope.md)
  A type that regulates which app extensions may access an extension point.
- [AppExtensionPoint.Attribute](./attribute.md)
  An interface that marks a type as an extension point attribute.


---

*[View on Apple Developer](https://developer.apple.com/documentation/extensionfoundation/appextensionpoint/enhancedsecurity)*