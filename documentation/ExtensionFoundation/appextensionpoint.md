# AppExtensionPoint

**Framework**: ExtensionFoundation  
**Kind**: struct

A type representing an extension point

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst 26.0+ (Beta)
- macOS 26.0+ (Beta)
- tvOS 26.0+ (Beta)
- visionOS 1.1+
- watchOS 26.0+ (Beta)

## Declaration

```swift
struct AppExtensionPoint
```

#### Overview

Use this to define extension points, bind to them and get available `AppExtensionIdentity` objects representing hostable extensions.

## Topics

### Classes
- [AppExtensionPoint.Monitor](appextensionpoint/monitor.md)
  An object that monitors the app extension points you add to it
### Protocols
- [AppExtensionPoint.Attribute](appextensionpoint/attribute.md)
  Marks the type as an extension point attribute
### Structures
- [AppExtensionPoint.Bind](appextensionpoint/bind.md)
  Marks the property as a binding to an extension point
- [AppExtensionPoint.Definition](appextensionpoint/definition.md)
  Marks the property as an extension point definition
- [AppExtensionPoint.EnhancedSecurity](appextensionpoint/enhancedsecurity.md)
  Specifies that the extension bound to this extension point must be launched in enhanced security mode
- [AppExtensionPoint.Identifier](appextensionpoint/identifier.md)
  Specifies the extension point identifier.
- [AppExtensionPoint.Name](appextensionpoint/name.md)
  Specifies the name of the extension point.
- [AppExtensionPoint.Scope](appextensionpoint/scope.md)
  Specifies the extension point scope.
- [AppExtensionPoint.UserInterface](appextensionpoint/userinterface.md)
  Specifies that the extension point supports user interface
### Initializers
- [init(identifier: StaticString) throws](appextensionpoint/init(identifier:).md)
### Enumerations
- [AppExtensionPoint.Error](appextensionpoint/error.md)

## Relationships

### Conforms To
- [Copyable](../Swift/Copyable.md)
- [Equatable](../Swift/Equatable.md)
- [ExtensionPointDefining](extensionpointdefining.md)
- [Hashable](../Swift/Hashable.md)
- [Identifiable](../Swift/Identifiable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/extensionfoundation/appextensionpoint)*