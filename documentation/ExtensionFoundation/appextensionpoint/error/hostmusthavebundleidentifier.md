# AppExtensionPoint.Error.hostMustHaveBundleIdentifier

**Framework**: ExtensionFoundation  
**Kind**: case

An error that indicates the host app is missing its bundle identifier.

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
case hostMustHaveBundleIdentifier
```

## See Also

- [AppExtensionPoint.Error.hostMustBeApplicationOrAppExtension](appextensionpoint/error/hostmustbeapplicationorappextension.md)
  An error that indicates the definition of an extension point in an unsupported target.
- [AppExtensionPoint.Error.hostMustDefineAppExtensionPoint(_:)](appextensionpoint/error/hostmustdefineappextensionpoint(_:).md)
  An error that indicates an attempt to define an extension point outside an app.
- [AppExtensionPoint.Error.invalidAppExtensionPoint](appextensionpoint/error/invalidappextensionpoint.md)
  An error that indicates an attempt to bind to an unknown extension point.
- [AppExtensionPoint.Error.unspecifiedAppExtensionPointName](appextensionpoint/error/unspecifiedappextensionpointname.md)
  An error that indicates the specified extension point is unknown.


---

*[View on Apple Developer](https://developer.apple.com/documentation/extensionfoundation/appextensionpoint/error/hostmusthavebundleidentifier)*