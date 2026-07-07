# SafariExtensionSettingsExtensionDictionaryObject

**Framework**: Device Management  
**Kind**: dictionary

The dictionary that defines the settings for a managed extension. Each key represents a specific managed extension, or you can specify a single “*” character to match any extension.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- visionOS 26.0+

## Declaration

```swift
object SafariExtensionSettingsExtensionDictionaryObject
```

## Properties

- `AllowedDomains` ([string]): Controls the domains and sub-domains the extension can access. The device ignores this key when the extension identifier is a single “*” character.
- `DeniedDomains` ([string]): Controls the domains and sub-domains the extension isn’t allowed to access. The device uses this key when the extension identifier is a composed identifier or a single “*” character.
- `PrivateBrowsing` (string): Controls whether an extension is allowed in Private Browsing. The device uses this key when the extension identifier is a composed identifier or a single “*” character. - `Allowed` - The user is allowed to turn the extension on or off in Private Browsing.
- `AlwaysOn` - The extension will always be on in Private Browsing if the extension is on outside of Private Browsing.
- `AlwaysOff` - The extension will never be on in Private Browsing.
- `State` (string): Controls whether an extension is allowed. The device uses this key when the extension identifier is a composed identifier or a single “*” character. - `Allowed` - The user is allowed to turn the extension on or off.
- `AlwaysOn` - The extension will always be on.
- `AlwaysOff` - The extension will always be off.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/safariextensionsettingsextensiondictionaryobject)*