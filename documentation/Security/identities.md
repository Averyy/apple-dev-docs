# Identities

**Framework**: Security

Combine certificates and cryptographic keys into identities.

#### Overview

An identity consists of a private key packaged with the certificate that contains and vouches for the corresponding public key. You use the certificate, key, and trust services API to create an identity from a private key and its certificate, or to import an identity from a password-protected PKCS #12 file. You then use the API to extract the key and certificate from the identity. You can also use the keychain services API to store the identity to or retrieve it from a keychain, much as you would the certificate or key by itself.

## Topics

### Essentials
- [Creating an Identity](creating-an-identity.md)
  Create an identity from a certificate and private key.
- [Storing an Identity in the Keychain](storing-an-identity-in-the-keychain.md)
  Securely store an identity in the keychain.
- [func SecIdentityCreateWithCertificate(CFTypeRef?, SecCertificate, UnsafeMutablePointer<SecIdentity?>) -> OSStatus](secidentitycreatewithcertificate(_:_:_:).md)
  Creates a new identity for a certificate and its associated private key.
- [class SecIdentity](secidentity.md)
  An abstract Core Foundation-type object representing an identity.
- [func SecIdentityGetTypeID() -> CFTypeID](secidentitygettypeid().md)
  Returns the unique identifier of the opaque type to which an identity object belongs.
### Identity Import
- [Importing an Identity](importing-an-identity.md)
  Learn how to import an identity from file.
- [func SecPKCS12Import(CFData, CFDictionary, UnsafeMutablePointer<CFArray?>) -> OSStatus](secpkcs12import(_:_:_:).md)
  Returns the identities and certificates in a PKCS #12-formatted blob.
- [Keychain Import and Export Options](keychain-import-and-export-options.md)
  Use these constants when you pass dictionary-based arguments to import and export functions.
- [PKCS #12 Import Item Keys](pkcs-12-import-item-keys.md)
  Recognized the dictionary keys returned by an import operation.
### Identity Components
- [Parsing an Identity](parsing-an-identity.md)
  Extract the private key and certificate from an identity.
- [func SecIdentityCopyCertificate(SecIdentity, UnsafeMutablePointer<SecCertificate?>) -> OSStatus](secidentitycopycertificate(_:_:).md)
  Retrieves a certificate associated with an identity.
- [func SecIdentityCopyPrivateKey(SecIdentity, UnsafeMutablePointer<SecKey?>) -> OSStatus](secidentitycopyprivatekey(_:_:).md)
  Retrieves the private key associated with an identity.
### System Identities
- [func SecIdentityCopySystemIdentity(CFString, UnsafeMutablePointer<SecIdentity?>, UnsafeMutablePointer<CFString?>?) -> OSStatus](secidentitycopysystemidentity(_:_:_:).md)
  Obtains the system identity associated with a specified domain.
- [func SecIdentitySetSystemIdentity(CFString, SecIdentity?) -> OSStatus](secidentitysetsystemidentity(_:_:).md)
  Assigns the system identity to be associated with a specified domain.
- [System Identity Domains](system-identity-domains.md)
  Set or obtain a system identity for domains.
### Identity Naming
- [func SecIdentitySetPreferred(SecIdentity?, CFString, CFArray?) -> OSStatus](secidentitysetpreferred(_:_:_:).md)
  Sets the identity that should be preferred for the specified name and key use.
- [func SecIdentityCopyPreferred(CFString, CFArray?, CFArray?) -> SecIdentity?](secidentitycopypreferred(_:_:_:).md)
  Retrieves the preferred identity for the specified name and key use.
### Identity Search
- [class SecIdentitySearch](secidentitysearch.md)
  Contains information about an identity search.
### Creating an Identity for Local Network TLS
- [Creating an Identity for Local Network TLS](../Network/creating-an-identity-for-local-network-tls.md)
  Learn how to create and use a digital identity in your application for local network TLS.


---

*[View on Apple Developer](https://developer.apple.com/documentation/security/identities)*