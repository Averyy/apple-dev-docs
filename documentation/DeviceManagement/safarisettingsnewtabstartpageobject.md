# SafariSettingsNewTabStartPageObject

**Framework**: Device Management  
**Kind**: dictionary

Sets the start page for new tabs in Safari.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- macOS 26.0+
- visionOS 26.0+

## Declaration

```swift
object SafariSettingsNewTabStartPageObject
```

## Properties

- `ExtensionIdentifier` (string): The composed identifier of the extension that provides the start page. The required format is “Identifier (TeamIdentifier)”, for example “com.example.app (ABCD1234)”. Required when setting `PageType` to `Extension`.
- `HomepageURL` (string): The URL of the homepage which needs to start with `https://` or `http://`. Required when setting `PageType` to `Home`.
- `PageType` (string) *(required)*: Sets the start page type in Safari: - `Start` - Safari uses the default start page. Safari disables the Homepage.
- `Home` - Safari uses the page specified by `HomepageURL`, and Safari also sets that as the Homepage.
- `Extension` - Safari uses the page specified by the Safari extension whose identifier is `ExtensionIdentifier`. Safari disables the Homepage.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/safarisettingsnewtabstartpageobject)*