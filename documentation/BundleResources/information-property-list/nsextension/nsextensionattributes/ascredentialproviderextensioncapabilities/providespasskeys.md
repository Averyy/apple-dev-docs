# ProvidesPasskeys

**Framework**: Bundle Resources  
**Kind**: typealias  
**Role**: Property List Key

A Boolean value that indicates whether your credential provider extension provides passkeys.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- macOS 14.0+

## Details

- **Name**: `ProvidesPasskeys`
- **Type**: boolean



**Default**: `NO`

#### Discussion

The operating system includes your extension’s passkeys in AutoFill and sign in sheets if this value is `true`.

## See Also

### Providing credentials
- [SupportsConditionalPasskeyRegistration](../../../supportsconditionalpasskeyregistration.md)
  Indicates that the credential provider supports automatic passkey upgrades.
- [ProvidesPasswords](./providespasswords.md)
  A Boolean value that indicates whether your credential provider extension provides passwords.
- [ProvidesOneTimeCodes](../../../providesonetimecodes.md)
  Allows this credential provider to show up in one-time-code text fields, to allowing filling time-based verification codes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/bundleresources/information-property-list/nsextension/nsextensionattributes/ascredentialproviderextensioncapabilities/providespasskeys)*