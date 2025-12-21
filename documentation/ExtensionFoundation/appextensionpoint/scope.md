# AppExtensionPoint.Scope

**Framework**: ExtensionFoundation  
**Kind**: struct

A type that regulates which app extensions may access an extension point.

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
struct Scope
```

#### Overview

Add a `Scope` type to your extension point definition to restrict the set of app extensions that may bind to the host app. If you don’t include this type in your definition, the default behavior requires app extensions to reside inside the host app. Configure this type with the [`AppExtensionPoint.Scope.Restriction.none`](appextensionpoint/scope/restriction/none.md) option to allow app extensions from outside the host app to connect as well. The following example shows an extension point definition that allows all app extensions to connect, including ones outside the host app:

```None
extension AppExtensionPoint {
    @Definition
    static var MyGlobalFeature : AppExtensionPoint {
        Name(“MyGlobalFeature”)
        UserInterface(false)
        Scope(.none)
    }
}
```

## Topics

### Creating a scope attribute
- [init(restriction: AppExtensionPoint.Scope.Restriction)](appextensionpoint/scope/init(restriction:).md)
  Initializes the scope type with the specified restriction value.
- [AppExtensionPoint.Scope.Restriction](appextensionpoint/scope/restriction.md)
  A type that indicates which app extensions may bind to a host app.

## Relationships

### Conforms To
- [AppExtensionPoint.Attribute](appextensionpoint/attribute.md)

## See Also

- [AppExtensionPoint.Definition](appextensionpoint/definition.md)
  A property wrapper that a host app uses to declare the extension points it supports.
- [AppExtensionPoint.Name](appextensionpoint/name.md)
  A type that defines the name of an extension point.
- [AppExtensionPoint.UserInterface](appextensionpoint/userinterface.md)
  A type with that indicates whether the extension point displays UI from an app extension.
- [AppExtensionPoint.EnhancedSecurity](appextensionpoint/enhancedsecurity.md)
  A type that indicates whether an extension point requires extra security.
- [AppExtensionPoint.Attribute](appextensionpoint/attribute.md)
  An interface that marks a type as an extension point attribute.


---

*[View on Apple Developer](https://developer.apple.com/documentation/extensionfoundation/appextensionpoint/scope)*