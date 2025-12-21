# AppExtensionPoint.Error.unspecifiedAppExtensionPointName

**Framework**: ExtensionFoundation  
**Kind**: case

An error that indicates the specified extension point is unknown.

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
case unspecifiedAppExtensionPointName
```

#### Discussion

Make sure the extension point name you specified matches one of the host app’s defined extension points.

## See Also

- [AppExtensionPoint.Error.hostMustBeApplicationOrAppExtension](appextensionpoint/error/hostmustbeapplicationorappextension.md)
  An error that indicates the definition of an extension point in an unsupported target.
- [AppExtensionPoint.Error.hostMustDefineAppExtensionPoint(_:)](appextensionpoint/error/hostmustdefineappextensionpoint(_:).md)
  An error that indicates an attempt to define an extension point outside an app.
- [AppExtensionPoint.Error.hostMustHaveBundleIdentifier](appextensionpoint/error/hostmusthavebundleidentifier.md)
  An error that indicates the host app is missing its bundle identifier.
- [AppExtensionPoint.Error.invalidAppExtensionPoint](appextensionpoint/error/invalidappextensionpoint.md)
  An error that indicates an attempt to bind to an unknown extension point.


---

*[View on Apple Developer](https://developer.apple.com/documentation/extensionfoundation/appextensionpoint/error/unspecifiedappextensionpointname)*