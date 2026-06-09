# PrivacyPreferencesPolicyControl.Services.Identity

**Framework**: Device Management  
**Kind**: dictionary

A dictionary listing apps and the privacy policy to apply to them.

**Availability**:
- macOS 10.14+

## Declaration

```swift
object PrivacyPreferencesPolicyControl.Services.Identity
```

## Properties

- `AEReceiverCodeRequirement` (string): The code requirement for the receiving binary. This code requirement is required for AppleEvents service; not valid for other services. Deprecated: macOS 27+
- `AEReceiverIdentifier` (string): The identifier of the process receiving an AppleEvent sent by the Identifier process. This identifier is required for AppleEvents service; not valid for other services. Deprecated: macOS 27+
- `AEReceiverIdentifierType` (string): The type of AEReceiverIdentifier value, either `bundleID` or `path`. This setting is required for AppleEvents service; not valid for other services. Deprecated: macOS 27+
- `Allowed` (boolean): If `true`, access is granted; otherwise, the process doesn’t have access. The user isn’t prompted and can’t change this value. > **Note**:  Every payload needs to include either `Authorization` or `Allowed`, but not both. Deprecated: macOS 27+
- `Authorization` (string): The `Authorization` key is an optional replacement for the `Allowed` key, which has one of the following possible values: - `Allow`: Equivalent to a `true` value for the `Allowed` key
- `Deny`: Equivalent to a `false` value for the `Allowed` key
- `AllowStandardUserToSetSystemService`: Allows a standard (non-admin) user to configure the permissions for the specified app in the Privacy preferences for services that otherwise require admin authorization; only valid for the `ListenEvent` and `ScreenCapture` services > **Note**:  Every payload needs to include either `Authorization` or `Allowed`, but not both. Available: macOS 11+
Deprecated: macOS 27+
- `CodeRequirement` (string) *(required)*: Obtained via the command `codesign -display -r -`. Deprecated: macOS 27+
- `Comment` (string): Not used. Deprecated: macOS 27+
- `Identifier` (string) *(required)*: The bundle ID or installation path of the binary. > **Note**:  This value is case-sensitive. Deprecated: macOS 27+
- `IdentifierType` (string) *(required)*: The type of identifier value. Application bundles must be identified by bundle ID. Nonbundled binaries must be identified by installation path. Helper tools embedded within an application bundle automatically inherit the permissions of their enclosing app bundle. Deprecated: macOS 27+
- `StaticCode` (boolean): If `true`, statically validate the code requirement. Used only if the process invalidates its dynamic code signature. Deprecated: macOS 27+


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/privacypreferencespolicycontrol/services-data.dictionary/identity)*