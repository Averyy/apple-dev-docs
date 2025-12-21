# init(restriction:)

**Framework**: ExtensionFoundation  
**Kind**: init

Initializes the scope type with the specified restriction value.

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
init(restriction: AppExtensionPoint.Scope.Restriction = .application)
```

## Parameters

- `restriction`: The binding restriction for app extensions. If you don’t specify a   value, only app extensions inside the host app may bind to it.

## See Also

- [AppExtensionPoint.Scope.Restriction](appextensionpoint/scope/restriction.md)
  A type that indicates which app extensions may bind to a host app.


---

*[View on Apple Developer](https://developer.apple.com/documentation/extensionfoundation/appextensionpoint/scope/init(restriction:))*