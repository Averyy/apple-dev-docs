# ASCredentialProviderExtensionCapabilities

**Framework**: Bundle Resources  
**Kind**: dictionary  
**Role**: Property List Key

The credential types supported by a credential provider extension, and whether it presents a user interface.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+

## Details

- **Name**: `ASCredentialProviderExtensionCapabilities`
- **Type**: dictionary

## Topics

### Providing credentials
- [ProvidesPasskeys](./ascredentialproviderextensioncapabilities/providespasskeys.md)
  A Boolean value that indicates whether your credential provider extension provides passkeys.
- [SupportsConditionalPasskeyRegistration](../../supportsconditionalpasskeyregistration.md)
  Indicates that the credential provider supports automatic passkey upgrades.
- [ProvidesPasswords](./ascredentialproviderextensioncapabilities/providespasswords.md)
  A Boolean value that indicates whether your credential provider extension provides passwords.
- [ProvidesOneTimeCodes](../../providesonetimecodes.md)
  Allows this credential provider to show up in one-time-code text fields, to allowing filling time-based verification codes.
### Providing text to AutoFill
- [ProvidesTextToInsert](../../providestexttoinsert.md)
  Allows this credential provider to show up in the system AutoFill context menu, so that it can fill text in any text field.
### Configuring credential providers
- [ShowsConfigurationUI](./ascredentialproviderextensioncapabilities/showsconfigurationui.md)
  A Boolean value that indicates whether your extension presents a user interface when someone enables it in Passwords settings.


---

*[View on Apple Developer](https://developer.apple.com/documentation/bundleresources/information-property-list/nsextension/nsextensionattributes/ascredentialproviderextensioncapabilities)*