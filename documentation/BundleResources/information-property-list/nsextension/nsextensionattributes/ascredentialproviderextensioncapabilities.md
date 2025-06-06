# ASCredentialProviderExtensionCapabilities

**Framework**: Bundle Resources  
**Kind**: dictionary

The credential types supported by a credential provider extension, and whether it presents a user interface.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+

## Topics

### Providing credentials
- [ProvidesPasskeys](information-property-list/nsextension/nsextensionattributes/ascredentialproviderextensioncapabilities/providespasskeys.md)
  A Boolean value that indicates whether your credential provider extension provides passkeys.
- [SupportsConditionalPasskeyRegistration](information-property-list/supportsconditionalpasskeyregistration.md)
  Indicates that the credential provider supports automatic passkey upgrades.
- [ProvidesPasswords](information-property-list/nsextension/nsextensionattributes/ascredentialproviderextensioncapabilities/providespasswords.md)
  A Boolean value that indicates whether your credential provider extension provides passwords.
- [ProvidesOneTimeCodes](information-property-list/providesonetimecodes.md)
  Allows this credential provider to show up in one-time-code text fields, to allowing filling time-based verification codes.
### Providing text to AutoFill
- [ProvidesTextToInsert](information-property-list/providestexttoinsert.md)
  Allows this credential provider to show up in the system AutoFill context menu, so that it can fill text in any text field.
### Configuring credential providers
- [ShowsConfigurationUI](information-property-list/nsextension/nsextensionattributes/ascredentialproviderextensioncapabilities/showsconfigurationui.md)
  A Boolean value that indicates whether your extension presents a user interface when someone enables it in Passwords settings.


---

*[View on Apple Developer](https://developer.apple.com/documentation/bundleresources/information-property-list/nsextension/nsextensionattributes/ascredentialproviderextensioncapabilities)*