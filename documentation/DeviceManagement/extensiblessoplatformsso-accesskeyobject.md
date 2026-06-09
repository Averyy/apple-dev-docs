# ExtensibleSSOPlatformSSO_AccessKeyObject

**Framework**: Device Management  
**Kind**: dictionary

Settings for Access Key authentication.

**Availability**:
- macOS 27.0+ (Beta)

## Declaration

```swift
object ExtensibleSSOPlatformSSO_AccessKeyObject
```

## Properties

- `AllowExpressMode` (boolean): If `true`, the system uses the access key in express mode, and doesn’t require authentication before use.
- `ReaderGroupIdentifier` (string): The reader group identifier for use with the `AccessKey`. The value needs to match the configured access key. Required if `UserCreation.AuthenticationMethods` contains `AccessKey`.
- `ReaderIssuerCertificateAssetReference` (string): The identifier of an asset declaration that contains the certificate for the issuer certificate of the `Terminal` identity of the access key. Other specifications refer to the key as the “Reader CA Public Key”. The key must be an elliptic curve key. Required if `UserCreation.AuthenticationMethods` includes `AccessKey`. The issuer of the Terminal identity of the access key needs to match this certificate, otherwise the device fails the authentication.
- `TerminalIdentityAssetReference` (string): The identifier of an asset declaration that contains the identity to use as the Terminal identity of the Access Key. The Access Key needs to trust the identity. Required if `UserCreation.AuthenticationMethods` includes `AccessKey`.

## See Also

- [object ExtensibleSSOPlatformSSO_AccountObject](extensiblessoplatformsso_accountobject.md)
  Account display and profile settings.
- [object ExtensibleSSOPlatformSSO_AuthorizationObject](extensiblessoplatformsso_authorizationobject.md)
  Settings for authorization prompts and group management.
- [object ExtensibleSSOPlatformSSO_PoliciesObject](extensiblessoplatformsso_policiesobject.md)
  Policies for login, unlock, and FileVault behavior.
- [object ExtensibleSSOPlatformSSO_UserCreationObject](extensiblessoplatformsso_usercreationobject.md)
  Settings for creating new users via Platform SSO.
- [object ExtensibleSSOPlatformSSO_WebAuthenticationObject](extensiblessoplatformsso_webauthenticationobject.md)
  Settings for web authentication behavior.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/extensiblessoplatformsso_accesskeyobject)*