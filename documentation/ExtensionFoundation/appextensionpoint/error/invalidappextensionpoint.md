# AppExtensionPoint.Error.invalidAppExtensionPoint

**Framework**: ExtensionFoundation  
**Kind**: case  
**Role**: Case

An error that indicates an attempt to bind to an unknown extension point.

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
case invalidAppExtensionPoint
```

## See Also

### Getting the error codes
- [AppExtensionPoint.Error.hostMustBeApplicationOrAppExtension](./hostmustbeapplicationorappextension.md)
  An error that indicates the definition of an extension point in an unsupported target.
- [AppExtensionPoint.Error.hostMustDefineAppExtensionPoint(_:)](./hostmustdefineappextensionpoint%28_%29.md)
  An error that indicates an attempt to define an extension point outside an app.
- [AppExtensionPoint.Error.hostMustHaveBundleIdentifier](./hostmusthavebundleidentifier.md)
  An error that indicates the host app is missing its bundle identifier.
- [AppExtensionPoint.Error.unspecifiedAppExtensionPointName](./unspecifiedappextensionpointname.md)
  An error that indicates the specified extension point is unknown.


---

*[View on Apple Developer](https://developer.apple.com/documentation/extensionfoundation/appextensionpoint/error/invalidappextensionpoint)*