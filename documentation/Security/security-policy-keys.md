# Security Policy Keys

**Framework**: Security

Use these dictionary keys to get and set policy properties.

#### Overview

Use these keys with calls to the [`SecPolicyCopyProperties(_:)`](secpolicycopyproperties(_:).md) and [`SecPolicySetProperties`](secpolicysetproperties.md) functions.

## Topics

### Constants
- [let kSecPolicyOid: CFString](ksecpolicyoid.md)
  The object identifier that defines the policy type (`CFStringRef`). All policies have a value for this key.
- [let kSecPolicyName: CFString](ksecpolicyname.md)
  A name (`CFStringRef`) that the certificate must match to satisfy this policy. For SSL/TLS, this specifies the server name which must match the common name of the certificate. For S/MIME, this specifies the RFC 822 email address.
- [let kSecPolicyClient: CFString](ksecpolicyclient.md)
  If true, indicates this policy should be evaluated against the client certificate. If false, the policy is evaluated against the certificate for the server. Default is false.
- [let kSecPolicyRevocationFlags: CFString](ksecpolicyrevocationflags.md)
- [let kSecPolicyTeamIdentifier: CFString](ksecpolicyteamidentifier.md)
- [let kSecPolicyKU_DigitalSignature: CFString](ksecpolicyku_digitalsignature.md)
  If true, the certificate’s key usage must allow it to be used for signing.
- [let kSecPolicyKU_NonRepudiation: CFString](ksecpolicyku_nonrepudiation.md)
  If true, the certificate’s key usage must allow it to be used for non-repudiation.
- [let kSecPolicyKU_KeyEncipherment: CFString](ksecpolicyku_keyencipherment.md)
  If true, the certificate’s key usage must allow it to be used for key encryption.
- [let kSecPolicyKU_DataEncipherment: CFString](ksecpolicyku_dataencipherment.md)
  If true, the certificate’s key usage must allow it to be used for data encryption.
- [let kSecPolicyKU_KeyAgreement: CFString](ksecpolicyku_keyagreement.md)
  If true, the certificate’s key usage must allow it to be used for key agreement.
- [let kSecPolicyKU_KeyCertSign: CFString](ksecpolicyku_keycertsign.md)
  If true, the certificate’s key usage must allow it to be used for signing certificates.
- [let kSecPolicyKU_CRLSign: CFString](ksecpolicyku_crlsign.md)
  If true, the certificate’s key usage must allow it to be used for signing certificate revocation lists (CRLs).
- [let kSecPolicyKU_EncipherOnly: CFString](ksecpolicyku_encipheronly.md)
  If true, the certificate’s key usage must allow it to be used  for encryption.
- [let kSecPolicyKU_DecipherOnly: CFString](ksecpolicyku_decipheronly.md)
  If true, the certificate’s key usage must allow it to be used  for decryption.


---

*[View on Apple Developer](https://developer.apple.com/documentation/security/security-policy-keys)*