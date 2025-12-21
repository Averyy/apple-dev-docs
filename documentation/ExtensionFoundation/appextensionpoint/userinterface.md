# AppExtensionPoint.UserInterface

**Framework**: ExtensionFoundation  
**Kind**: struct

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

#### Overview

Add a `UserInterface` type in an extension point definition and initialize it with a Boolean value. Specify `true` if your extension point supports custom UI or `false` if it doesn’t.

## Topics

### Creating a user-interface attribute
- [init(Bool)](appextensionpoint/userinterface/init(_:).md)
  Initializes the type with the specified Boolean value.
### Getting the value
- [let value: Bool](appextensionpoint/userinterface/value.md)

## Relationships

### Conforms To
- [AppExtensionPoint.Attribute](appextensionpoint/attribute.md)

## See Also

- [AppExtensionPoint.Definition](appextensionpoint/definition.md)
  A property wrapper that a host app uses to declare the extension points it supports.
- [AppExtensionPoint.Name](appextensionpoint/name.md)
  A type that defines the name of an extension point.
- [AppExtensionPoint.EnhancedSecurity](appextensionpoint/enhancedsecurity.md)
  A type that indicates whether an extension point requires extra security.
- [AppExtensionPoint.Scope](appextensionpoint/scope.md)
  A type that regulates which app extensions may access an extension point.
- [AppExtensionPoint.Attribute](appextensionpoint/attribute.md)
  An interface that marks a type as an extension point attribute.


---

*[View on Apple Developer](https://developer.apple.com/documentation/extensionfoundation/appextensionpoint/userinterface)*