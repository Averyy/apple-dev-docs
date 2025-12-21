# bundleIdentifier

**Framework**: ExtensionFoundation  
**Kind**: property

The bundle identifier of the app extension.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 13.0+
- tvOS 26.0+
- visionOS 1.1+
- watchOS 26.0+

## Declaration

```swift
var bundleIdentifier: String { get }
```

#### Discussion

During development, an app extension creator assigns a value to this string that incorporates the creator’s company name and the extension name. Bundle identifier strings use reverse-DNS notation.

## See Also

- [var extensionPointIdentifier: String](appextensionidentity/extensionpointidentifier.md)
  The extension point of your host app that the app extension supports.
- [var localizedName: String](appextensionidentity/localizedname.md)
  The localized, human-readable name of the app extension.


---

*[View on Apple Developer](https://developer.apple.com/documentation/extensionfoundation/appextensionidentity/bundleidentifier)*