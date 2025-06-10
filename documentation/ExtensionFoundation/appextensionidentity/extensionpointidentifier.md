# extensionPointIdentifier

**Framework**: ExtensionFoundation  
**Kind**: property

A unique identifier for the extension point this extension targets.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst 26.0+ (Beta)
- macOS 13.0+
- tvOS 26.0+ (Beta)
- visionOS 1.1+
- watchOS 26.0+ (Beta)

## Declaration

```swift
var extensionPointIdentifier: String { get }
```

## See Also

- [var bundleIdentifier: String](appextensionidentity/bundleidentifier.md)
  The bundle identifier for the extension.
- [var localizedName: String](appextensionidentity/localizedname.md)
  A localized, human-readable name for the extension.
- [AppExtensionIdentity.Identities](appextensionidentity/identities.md)
  An asynchronous sequence that returns the enabled extensions that match provided constraints.


---

*[View on Apple Developer](https://developer.apple.com/documentation/extensionfoundation/appextensionidentity/extensionpointidentifier)*