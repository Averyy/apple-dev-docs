# extensionPointIdentifier

**Framework**: ExtensionFoundation  
**Kind**: property

The extension point of your host app that the app extension supports.

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
var extensionPointIdentifier: String { get }
```

#### Discussion

This property contains the identifier for one of the host app’s extension points. Extension points represent the extensible features of the host app.

## See Also

- [var bundleIdentifier: String](appextensionidentity/bundleidentifier.md)
  The bundle identifier of the app extension.
- [var localizedName: String](appextensionidentity/localizedname.md)
  The localized, human-readable name of the app extension.


---

*[View on Apple Developer](https://developer.apple.com/documentation/extensionfoundation/appextensionidentity/extensionpointidentifier)*