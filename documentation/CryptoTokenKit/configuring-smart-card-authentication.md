# Configuring Smart Card Authentication

**Framework**: Cryptotokenkit

Set preferences for smart card authentication operations, including those on managed devices.

#### Overview

When you use the CryptoTokenKit framework to manage hardware tokens as two-factor authentication devices, as [`Authenticating Users with a Cryptographic Token`](authenticating-users-with-a-cryptographic-token.md) describes, the authentication process is subject to certain configuration options.

##### Set Smart Card Preferences

Configure smart card authentication preferences by setting values in the `com.apple.security.smartcard` preferences domain. For each setting, the framework first tries to read from mobile device management (MDM) settings. Next, it looks at systemwide preferences. Finally, it falls back on default values for any remaining unspecificed values.

> **Note**:  The framework ignores individual user preferences.

The framework looks for and responds to the following preference keys:

The values for `checkCertificateTrust:`

- `0` — Trust every certificate. Although this setting is the default, it’s suitable only for users with self-signed certificates. Corporate systems must typically use a more secure setting.
- `1` — Test that certificates are within their validity period and that the system trusts the issuer.
- `2` — Test that the certificates are within the validity period, test that the system trusts the issuer, and test against a soft revocation check. A soft revocation check means that as long as the certificate revocation check doesn’t explicitly reject the certificate, it remains valid. When the system can’t complete a check, the certificate remains valid.
- `3` — Test that the certificates are within the validity period, test that the system trusts the issuer, and test against a hard revocation check. Unless a certificate revocation check explicitly validates the certificate, it’s considered invalid.

## See Also

- [Authenticating Users with a Cryptographic Token](authenticating-users-with-a-cryptographic-token.md)
  Grant access to user accounts and the keychain by creating a smart card app extension.
- [class TKSmartCardTokenDriver](tksmartcardtokendriver.md)
  The driver that acts as an entry point for smart card app extensions.
- [class TKSmartCardToken](tksmartcardtoken.md)
  A representation of a smart card based cryptographic token.
- [class TKSmartCardTokenSession](tksmartcardtokensession.md)
  A token session that is based on a smart card token.


---

*[View on Apple Developer](https://developer.apple.com/documentation/CryptoTokenKit/configuring-smart-card-authentication)*