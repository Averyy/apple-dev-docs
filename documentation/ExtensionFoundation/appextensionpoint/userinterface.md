# AppExtensionPoint.UserInterface

**Framework**: ExtensionFoundation  
**Kind**: struct  
**Role**: Structure

A type with that indicates whether the extension point displays UI from an app extension.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- visionOS 1.1+

## Declaration

```swift
struct UserInterface
```

## Overview

Add a `UserInterface` type in an extension point definition and initialize it with a Boolean value. Specify `true` if your extension point supports custom UI or `false` if it doesn’t.

## Topics

### Creating a user-interface attribute
- [init(Bool)](./userinterface/init%28_%29.md)
  Initializes the type with the specified Boolean value.
### Getting the value
- [let value: Bool](./userinterface/value.md)

## Relationships

### Conforms To
- [AppExtensionPoint.Attribute](./attribute.md)

## See Also

### Declaring an extension point
- [AppExtensionPoint.Definition](./definition.md)
  A property wrapper that a host app uses to declare the extension points it supports.
- [AppExtensionPoint.Name](./name.md)
  A type that defines the name of an extension point.
- [AppExtensionPoint.EnhancedSecurity](./enhancedsecurity.md)
  A type that indicates whether an extension point requires extra security.
- [AppExtensionPoint.Scope](./scope.md)
  A type that regulates which app extensions may access an extension point.
- [AppExtensionPoint.Attribute](./attribute.md)
  An interface that marks a type as an extension point attribute.


---

*[View on Apple Developer](https://developer.apple.com/documentation/extensionfoundation/appextensionpoint/userinterface)*