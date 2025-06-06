# ProvidesPasskeys

**Framework**: Bundle Resources  
**Kind**: typealias

A Boolean value that indicates whether your credential provider extension provides passkeys.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- macOS 14.0+

#### Discussion

The operating system includes your extension’s passkeys in AutoFill and sign in sheets if this value is `true`.

## See Also

- [SupportsConditionalPasskeyRegistration](information-property-list/supportsconditionalpasskeyregistration.md)
  Indicates that the credential provider supports automatic passkey upgrades.
- [ProvidesPasswords](information-property-list/nsextension/nsextensionattributes/ascredentialproviderextensioncapabilities/providespasswords.md)
  A Boolean value that indicates whether your credential provider extension provides passwords.
- [ProvidesOneTimeCodes](information-property-list/providesonetimecodes.md)
  Allows this credential provider to show up in one-time-code text fields, to allowing filling time-based verification codes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/bundleresources/information-property-list/nsextension/nsextensionattributes/ascredentialproviderextensioncapabilities/providespasskeys)*