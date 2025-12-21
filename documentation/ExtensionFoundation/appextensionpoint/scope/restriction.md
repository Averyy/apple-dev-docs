# AppExtensionPoint.Scope.Restriction

**Framework**: ExtensionFoundation  
**Kind**: enum

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
- [AppExtensionPoint.Scope.Restriction.none](appextensionpoint/scope/restriction/none.md)
  A value that allows app extensions in any app to bind to the host app.
- [AppExtensionPoint.Scope.Restriction.application](appextensionpoint/scope/restriction/application.md)
  A value that requires an app extension to reside inside the same app to which it’s binding.

## Relationships

### Conforms To
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)

## See Also

- [init(restriction: AppExtensionPoint.Scope.Restriction)](appextensionpoint/scope/init(restriction:).md)
  Initializes the scope type with the specified restriction value.


---

*[View on Apple Developer](https://developer.apple.com/documentation/extensionfoundation/appextensionpoint/scope/restriction)*