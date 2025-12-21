# AppExtensionPoint.Error.hostMustDefineAppExtensionPoint(_:)

**Framework**: ExtensionFoundation  
**Kind**: case

An error that indicates an attempt to define an extension point outside an app.

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
case hostMustDefineAppExtensionPoint(String)
```

## See Also

- [AppExtensionPoint.Error.hostMustBeApplicationOrAppExtension](appextensionpoint/error/hostmustbeapplicationorappextension.md)
  An error that indicates the definition of an extension point in an unsupported target.
- [AppExtensionPoint.Error.hostMustHaveBundleIdentifier](appextensionpoint/error/hostmusthavebundleidentifier.md)
  An error that indicates the host app is missing its bundle identifier.
- [AppExtensionPoint.Error.invalidAppExtensionPoint](appextensionpoint/error/invalidappextensionpoint.md)
  An error that indicates an attempt to bind to an unknown extension point.
- [AppExtensionPoint.Error.unspecifiedAppExtensionPointName](appextensionpoint/error/unspecifiedappextensionpointname.md)
  An error that indicates the specified extension point is unknown.


---

*[View on Apple Developer](https://developer.apple.com/documentation/extensionfoundation/appextensionpoint/error/hostmustdefineappextensionpoint(_:))*