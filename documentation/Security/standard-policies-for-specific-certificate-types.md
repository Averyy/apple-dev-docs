# Standard Policies for Specific Certificate Types

**Framework**: Security

Use special OIDs to cause a certificate to be evaluated based on security policies specific to a given type of certificate.

## Topics

### Constants
- [let kSecPolicyAppleX509Basic: CFString](ksecpolicyapplex509basic.md)
  Basic X509-style certificate evaluation.
- [let kSecPolicyAppleSSL: CFString](ksecpolicyapplessl.md)
  Basic X509 plus host name verification per RFC 2818.
- [let kSecPolicyAppleSMIME: CFString](ksecpolicyapplesmime.md)
  Basic X509 plus email address verification and `KeyUsage` enforcement per RFC 2632.
- [let kSecPolicyAppleEAP: CFString](ksecpolicyappleeap.md)
  Extensible Authentication Protocol. Functionally identical to SSL policy. A separate OID is provided to facilitate per-policy, per-certificate trust settings using the `SecTrust` mechanism.
- [let kSecPolicyAppleIPsec: CFString](ksecpolicyappleipsec.md)
  Policy for use in IPsec communication. Functionally identical to SSL policy. A separate OID is provided to facilitate per-policy, per-certificate trust settings using the `SecTrust` mechanism.
- [let kSecPolicyApplePKINITClient: CFString](ksecpolicyapplepkinitclient.md)
  Kerberos Pkinit client certificate validation.
- [let kSecPolicyApplePKINITServer: CFString](ksecpolicyapplepkinitserver.md)
  Kerberos Pkinit server certificate validation.
- [let kSecPolicyAppleCodeSigning: CFString](ksecpolicyapplecodesigning.md)
  Policy for use in evaluating Apple code signing certificates.
- [let kSecPolicyMacAppStoreReceipt: CFString](ksecpolicymacappstorereceipt.md)
  Policy for use in evaluating Mac App Store receipts.
- [let kSecPolicyAppleIDValidation: CFString](ksecpolicyappleidvalidation.md)
  Policy for use in evaluating Apple ID certificates.
- [let kSecPolicyAppleTimeStamping: CFString](ksecpolicyappletimestamping.md)
  Policy that causes evaluation of the validity of the time stamp on a signature. This can be used to allow verification that a certificate was valid at the time that something was signed with that certificate even if the certificate is no longer valid.
- [let kSecPolicyApplePassbookSigning: CFString](ksecpolicyapplepassbooksigning.md)
- [let kSecPolicyApplePayIssuerEncryption: CFString](ksecpolicyapplepayissuerencryption.md)
- [let kSecPolicyAppleRevocation: CFString](ksecpolicyapplerevocation.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/security/standard-policies-for-specific-certificate-types)*