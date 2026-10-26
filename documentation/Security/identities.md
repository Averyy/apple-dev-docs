# Identities

**Framework**: Security  
**Role**: API Collection

Combine certificates and cryptographic keys into identities.

#### Overview

An identity consists of a private key packaged with the certificate that contains and vouches for the corresponding public key. You use the certificate, key, and trust services API to create an identity from a private key and its certificate, or to import an identity from a password-protected PKCS #12 file. You then use the API to extract the key and certificate from the identity. You can also use the keychain services API to store the identity to or retrieve it from a keychain, much as you would the certificate or key by itself.

## Topics

### Essentials
- [Creating an Identity](./creating-an-identity.md)
  Create an identity from a certificate and private key.
- [Storing an Identity in the Keychain](./storing-an-identity-in-the-keychain.md)
  Securely store an identity in the keychain.
- [func SecIdentityCreateWithCertificate(CFTypeRef?, SecCertificate, UnsafeMutablePointer<SecIdentity?>) -> OSStatus](./secidentitycreatewithcertificate%28_,_,_%29.md)
  Creates a new identity for a certificate and its associated private key.
- [class SecIdentity](./secidentity.md)
  An abstract Core Foundation-type object representing an identity.
- [func SecIdentityGetTypeID() -> CFTypeID](./secidentitygettypeid%28%29.md)
  Returns the unique identifier of the opaque type to which an identity object belongs.
### Identity Import
- [Importing an Identity](./importing-an-identity.md)
  Learn how to import an identity from file.
- [func SecPKCS12Import(CFData, CFDictionary, UnsafeMutablePointer<CFArray?>) -> OSStatus](./secpkcs12import%28_,_,_%29.md)
  Returns the identities and certificates in a PKCS #12-formatted blob.
- [Keychain Import and Export Options](./keychain-import-and-export-options.md)
  Use these constants when you pass dictionary-based arguments to import and export functions.
- [PKCS #12 Import Item Keys](./pkcs-12-import-item-keys.md)
  Recognized the dictionary keys returned by an import operation.
### Identity Components
- [Parsing an Identity](./parsing-an-identity.md)
  Extract the private key and certificate from an identity.
- [func SecIdentityCopyCertificate(SecIdentity, UnsafeMutablePointer<SecCertificate?>) -> OSStatus](./secidentitycopycertificate%28_,_%29.md)
  Retrieves a certificate associated with an identity.
- [func SecIdentityCopyPrivateKey(SecIdentity, UnsafeMutablePointer<SecKey?>) -> OSStatus](./secidentitycopyprivatekey%28_,_%29.md)
  Retrieves the private key associated with an identity.
### System Identities
- [func SecIdentityCopySystemIdentity(CFString, UnsafeMutablePointer<SecIdentity?>, UnsafeMutablePointer<CFString?>?) -> OSStatus](./secidentitycopysystemidentity%28_,_,_%29.md)
  Obtains the system identity associated with a specified domain.
- [func SecIdentitySetSystemIdentity(CFString, SecIdentity?) -> OSStatus](./secidentitysetsystemidentity%28_,_%29.md)
  Assigns the system identity to be associated with a specified domain.
- [System Identity Domains](./system-identity-domains.md)
  Set or obtain a system identity for domains.
### Identity Naming
- [func SecIdentitySetPreferred(SecIdentity?, CFString, CFArray?) -> OSStatus](./secidentitysetpreferred%28_,_,_%29.md)
  Sets the identity that should be preferred for the specified name and key use.
- [func SecIdentityCopyPreferred(CFString, CFArray?, CFArray?) -> SecIdentity?](./secidentitycopypreferred%28_,_,_%29.md)
  Retrieves the preferred identity for the specified name and key use.
- [SecIdentityCopyPreference](./secidentitycopypreference.md)
  Returns the preferred identity for the specified name and key use.
- [SecIdentitySetPreference](./secidentitysetpreference.md)
  Sets the preferred identity for the specified name and key use.
### Identity Search
- [class SecIdentitySearch](./secidentitysearch.md)
  Contains information about an identity search.
- [SecIdentitySearchCopyNext](./secidentitysearchcopynext.md)
  Finds the next identity matching specified search criteria
- [SecIdentitySearchCreate](./secidentitysearchcreate.md)
  Creates a search object for finding identities.
- [SecIdentitySearchGetTypeID](./secidentitysearchgettypeid.md)
  Returns the unique identifier of the opaque type to which a `SecIdentitySearch` object belongs.
### Creating an Identity for Local Network TLS
- [Creating an Identity for Local Network TLS](../Network/creating-an-identity-for-local-network-tls.md)
  Learn how to create and use a digital identity in your application for local network TLS.
### Legacy Symbols
- [OpaqueSecIdentityRef](./opaquesecidentityref.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/security/identities)*