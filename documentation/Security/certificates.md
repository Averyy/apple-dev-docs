# Certificates

**Framework**: Security

Manage digital certificates.

#### Overview

A digital certificate is a collection of data used to securely distribute the public half of a public/private key pair. Figure 1 shows the parts of a typical X.509 certificate that make this possible. Along with structural information, the certificate contains name and contact information for both its issuer and its owner (or subject), plus the owner’s public key. A date range indicates when the certificate is valid. Certificate extensions provide additional information and conditions, like acceptable uses for the public key. When assembling the certificate, to vouch for its integrity, the issuer digitally signs it using the issuer’s own identity (private key and certificate).

![Diagram showing the components of an X.509 certificate, including the version and serial number, the subject and issuer, the validity dates, the public key, the signature, and the extensions.](https://docs-assets.developer.apple.com/published/76dd13909e46b298fd2d4de9bca4f6a0/media-2904073%402x.png)

To evaluate a certificate, you first verify its signature using the specified algorithm and the issuer’s public key, which you obtain from the issuer’s publicly available certificate. A valid signature confirms that the certificate under evaluation, known as the leaf certificate, is unaltered. But in order to trust this result, you must also trust the issuer’s certificate. You use a similar procedure to test this certificate, and the one that guarantees that certificate, and the next, and so on in a chain back to a trusted root authority whose certificate, known as the anchor, which you trust implicitly. The public key included in the leaf certificate is then considered trustworthy. You can be assured that it has come unaltered from the certificate’s owner who controls the corresponding private key. This allows you to securely use the public key to engage in asymmetric cryptography with the certificate’s owner.

For more details about how certificates work, read [`Digital Certificates`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/Security/Conceptual/cryptoservices/CryptographyConcepts/CryptographyConcepts.html#//apple_ref/doc/uid/TP40011172-CH8-CHDBIGCE) in [`Cryptographic Services Guide`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/Security/Conceptual/cryptoservices/Introduction/Introduction.html#//apple_ref/doc/uid/TP40011172).

## Topics

### Essentials
- [Getting a Certificate](getting-a-certificate.md)
  Obtain a certificate from an identity, from DER-encoded data, or from the keychain.
- [Storing a Certificate in the Keychain](storing-a-certificate-in-the-keychain.md)
  Store a certificate in the keychain for safekeeping.
- [class SecCertificate](seccertificate.md)
  An abstract Core Foundation-type object representing an X.509 certificate.
- [func SecCertificateGetTypeID() -> CFTypeID](seccertificategettypeid().md)
  Returns the unique identifier of the opaque type to which a certificate object belongs.
### Import and Export
- [Storing a DER-Encoded X.509 Certificate](storing-a-der-encoded-x-509-certificate.md)
  Import and export a certificate from a file.
- [func SecCertificateCreateWithData(CFAllocator?, CFData) -> SecCertificate?](seccertificatecreatewithdata(_:_:).md)
  Creates a certificate object from a DER representation of a certificate.
- [func SecCertificateCopyData(SecCertificate) -> CFData](seccertificatecopydata(_:).md)
  Returns a DER representation of a certificate given a certificate object.
### Certificate Components
- [Examining a Certificate](examining-a-certificate.md)
  Learn how to retrieve properties from a certificate.
- [func SecCertificateCopySubjectSummary(SecCertificate) -> CFString?](seccertificatecopysubjectsummary(_:).md)
  Returns a human-readable summary of a certificate.
- [func SecCertificateCopyCommonName(SecCertificate, UnsafeMutablePointer<CFString?>) -> OSStatus](seccertificatecopycommonname(_:_:).md)
  Retrieves the common name of the subject of a certificate.
- [func SecCertificateCopyEmailAddresses(SecCertificate, UnsafeMutablePointer<CFArray?>) -> OSStatus](seccertificatecopyemailaddresses(_:_:).md)
  Retrieves the email addresses for the subject of a certificate.
- [func SecCertificateCopyNormalizedIssuerSequence(SecCertificate) -> CFData?](seccertificatecopynormalizedissuersequence(_:).md)
  Retrieves the normalized issuer sequence from a certificate.
- [func SecCertificateCopyNormalizedSubjectSequence(SecCertificate) -> CFData?](seccertificatecopynormalizedsubjectsequence(_:).md)
  Retrieves the normalized subject sequence from a certificate.
- [func SecCertificateCopySerialNumberData(SecCertificate, UnsafeMutablePointer<Unmanaged<CFError>?>?) -> CFData?](seccertificatecopyserialnumberdata(_:_:).md)
  Returns the certificate’s serial number.
- [func SecCertificateCopyKey(SecCertificate) -> SecKey?](seccertificatecopykey(_:).md)
  Retrieves the public key for a given certificate.
- [func SecCertificateCopyShortDescription(CFAllocator?, SecCertificate, UnsafeMutablePointer<Unmanaged<CFError>?>?) -> CFString?](seccertificatecopyshortdescription(_:_:_:).md)
  Returns a copy of the short description of a certificate.
- [func SecCertificateCopyLongDescription(CFAllocator?, SecCertificate, UnsafeMutablePointer<Unmanaged<CFError>?>?) -> CFString?](seccertificatecopylongdescription(_:_:_:).md)
  Returns a copy of the long description of a certificate.
### Detailed Certificate Information
- [Getting Certificate Values](getting-certificate-values.md)
  Obtain all the values associated with a certificate.
- [func SecCertificateCopyValues(SecCertificate, CFArray?, UnsafeMutablePointer<Unmanaged<CFError>?>?) -> CFDictionary?](seccertificatecopyvalues(_:_:_:).md)
  Creates a dictionary that represents a certificate’s contents.
- [Certificate OIDs](certificate-oids.md)
  Use OIDs as keys in the dictionary representing certificate values.
- [Certificate Property Keys](certificate-property-keys.md)
  Recognize the dictionary keys that taken together define a certificate property.
- [Certificate Property Type Values](certificate-property-type-values.md)
  Recognize the possible certificate property types.
- [Certificate Item Attribute Constants](certificate-item-attribute-constants.md)
  Use these four character values to indicate certificate item attributes.
### Certificate Names
- [func SecCertificateSetPreferred(SecCertificate?, CFString, CFArray?) -> OSStatus](seccertificatesetpreferred(_:_:_:).md)
  Sets the certificate that should be preferred for the specified name and key use.
- [func SecCertificateCopyPreferred(CFString, CFArray?) -> SecCertificate?](seccertificatecopypreferred(_:_:).md)
  Returns the preferred certificate for the specified name and key usage.
### Legacy Symbols
- [func SecCertificateAddToKeychain(SecCertificate, SecKeychain?) -> OSStatus](seccertificateaddtokeychain(_:_:).md)
  Adds a certificate to a keychain.
- [func SecCertificateCopyNormalizedIssuerContent(SecCertificate, UnsafeMutablePointer<Unmanaged<CFError>?>?) -> CFData?](seccertificatecopynormalizedissuercontent(_:_:).md)
  Returns a normalized copy of the distinguished name (DN) of the issuer of a certificate.
- [func SecCertificateCopyNormalizedSubjectContent(SecCertificate, UnsafeMutablePointer<Unmanaged<CFError>?>?) -> CFData?](seccertificatecopynormalizedsubjectcontent(_:_:).md)
  Returns a normalized copy of the distinguished name (DN) of the subject of a certificate.
- [func SecCertificateCopySerialNumber(SecCertificate) -> CFData?](seccertificatecopyserialnumber(_:_:).md)
  Returns a copy of a certificate’s serial number.
- [func SecCertificateCopyPublicKey(SecCertificate) -> SecKey?](seccertificatecopypublickey(_:_:).md)
  Retrieves the public key from a certificate.


---

*[View on Apple Developer](https://developer.apple.com/documentation/security/certificates)*