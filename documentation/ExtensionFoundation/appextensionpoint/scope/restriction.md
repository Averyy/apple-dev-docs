# AppExtensionPoint.Scope.Restriction

**Framework**: ExtensionFoundation  
**Kind**: enum  
**Role**: Enumeration

A type that indicates which app extensions may bind to a host app.

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
enum Restriction
```

## Topics

### Getting the restriction types
- [AppExtensionPoint.Scope.Restriction.none](./restriction/none.md)
  A value that allows app extensions in any app to bind to the host app.
- [AppExtensionPoint.Scope.Restriction.application](./restriction/application.md)
  A value that requires an app extension to reside inside the same app to which it’s binding.

## Relationships

### Conforms To
- [Equatable](../../../Swift/equatable.md)
- [Hashable](../../../Swift/hashable.md)

## See Also

### Creating a scope attribute
- [init(restriction: AppExtensionPoint.Scope.Restriction)](./init%28restriction%29.md)
  Initializes the scope type with the specified restriction value.


---

*[View on Apple Developer](https://developer.apple.com/documentation/extensionfoundation/appextensionpoint/scope/restriction)*