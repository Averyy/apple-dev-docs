# Cryptographic Message Syntax Services

**Framework**: Security  
**Role**: API Collection

Cryptographically sign and encrypt S/MIME messages.

#### Overview

When you want to exchange data securely using the Multipurpose Internet Mail Extensions (MIME) protocol, you use the version of the protocol known as S/MIME defined in [RFC 3851](https://tools.ietf.org/html/rfc3851). This allows you to, among other things, ensure data integrity through digital signatures and data confidentiality through encryption. S/MIME in turn relies on the Cryptographic Message Syntax (CMS) protocol defined in [RFC 3852](https://tools.ietf.org/html/rfc3852) to carry out these operations.

Cryptographic message syntax services provides encoder objects that perform encryption using the CMS protocol’s enveloped-data content type and sign using the signed-data content type. When a message is both signed and encrypted, the enveloped data content contains the signed data content. That is, the message is first signed and then the signed content is encrypted.

## Topics

### The Encoder
- [func CMSEncoderCreate(UnsafeMutablePointer<CMSEncoder?>) -> OSStatus](./cmsencodercreate%28_%29.md)
  Creates a CMSEncoder reference.
- [class CMSEncoder](./cmsencoder.md)
  Opaque reference to a CMS encoder object.
- [func CMSEncoderGetTypeID() -> CFTypeID](./cmsencodergettypeid%28%29.md)
  Returns the type identifier for the CMSEncoder opaque type.
### Message Creation
- [func CMSEncoderAddSigners(CMSEncoder, CFTypeRef) -> OSStatus](./cmsencoderaddsigners%28_,_%29.md)
  Specifies signers of the message.
- [func CMSEncoderAddRecipients(CMSEncoder, CFTypeRef) -> OSStatus](./cmsencoderaddrecipients%28_,_%29.md)
  Specifies a message is to be encrypted and specifies the recipients of the message.
- [func CMSEncoderSetHasDetachedContent(CMSEncoder, Bool) -> OSStatus](./cmsencodersethasdetachedcontent%28_,_%29.md)
  Specifies whether the signed data is to be separate from the message.
- [func CMSEncoderSetEncapsulatedContentTypeOID(CMSEncoder, CFTypeRef) -> OSStatus](./cmsencodersetencapsulatedcontenttypeoid%28_,_%29.md)
  Specifies an object identifier for the encapsulated data of a signed message.
- [func CMSEncoderAddSupportingCerts(CMSEncoder, CFTypeRef) -> OSStatus](./cmsencoderaddsupportingcerts%28_,_%29.md)
  Adds certificates to a message.
- [func CMSEncoderAddSignedAttributes(CMSEncoder, CMSSignedAttributes) -> OSStatus](./cmsencoderaddsignedattributes%28_,_%29.md)
  Specifies attributes for a signed message.
- [struct CMSSignedAttributes](./cmssignedattributes.md)
  Optional attributes you can add to a signed message.
- [func CMSEncoderSetCertificateChainMode(CMSEncoder, CMSCertificateChainMode) -> OSStatus](./cmsencodersetcertificatechainmode%28_,_%29.md)
  Specifies which certificates to include in a signed CMS message.
- [enum CMSCertificateChainMode](./cmscertificatechainmode.md)
  Constants that can be set to specify what certificates to include in a signed message.
- [func CMSEncoderSetSignerAlgorithm(CMSEncoder, CFString) -> OSStatus](./cmsencodersetsigneralgorithm%28_,_%29.md)
  Sets the digest algorithm to use for the signer.
### Message Characteristics
- [func CMSEncoderCopySigners(CMSEncoder, UnsafeMutablePointer<CFArray?>) -> OSStatus](./cmsencodercopysigners%28_,_%29.md)
  Obtains the array of signers specified with the `CMSEncoderAddSigners` function.
- [func CMSEncoderCopyRecipients(CMSEncoder, UnsafeMutablePointer<CFArray?>) -> OSStatus](./cmsencodercopyrecipients%28_,_%29.md)
  Obtains the array of recipients specified with the `CMSEncoderAddRecipients` function.
- [func CMSEncoderGetHasDetachedContent(CMSEncoder, UnsafeMutablePointer<DarwinBoolean>) -> OSStatus](./cmsencodergethasdetachedcontent%28_,_%29.md)
  Indicates whether the message is to have detached content.
- [func CMSEncoderCopyEncapsulatedContentType(CMSEncoder, UnsafeMutablePointer<CFData?>) -> OSStatus](./cmsencodercopyencapsulatedcontenttype%28_,_%29.md)
  Obtains the object identifier for the encapsulated data of a signed message.
- [func CMSEncoderCopySupportingCerts(CMSEncoder, UnsafeMutablePointer<CFArray?>) -> OSStatus](./cmsencodercopysupportingcerts%28_,_%29.md)
  Obtains the certificates added to a message with `CMSEncoderAddSupportingCerts`.
- [func CMSEncoderGetCertificateChainMode(CMSEncoder, UnsafeMutablePointer<CMSCertificateChainMode>) -> OSStatus](./cmsencodergetcertificatechainmode%28_,_%29.md)
  Obtains a constant that indicates which certificates are to be included in a signed CMS message.
### Encoding
- [func CMSEncoderUpdateContent(CMSEncoder, UnsafeRawPointer, Int) -> OSStatus](./cmsencoderupdatecontent%28_,_,_%29.md)
  Feeds content bytes into the encoder.
- [func CMSEncoderCopyEncodedContent(CMSEncoder, UnsafeMutablePointer<CFData?>) -> OSStatus](./cmsencodercopyencodedcontent%28_,_%29.md)
  Finishes encoding the message and obtains the encoded result.
- [func CMSEncodeContent(CFTypeRef?, CFTypeRef?, CFTypeRef?, Bool, CMSSignedAttributes, UnsafeRawPointer, Int, UnsafeMutablePointer<CFData?>?) -> OSStatus](./cmsencodecontent%28_,_,_,_,_,_,_,_%29.md)
  Encodes a message and obtains the result in one high-level function call.
### The Decoder
- [func CMSDecoderCreate(UnsafeMutablePointer<CMSDecoder?>) -> OSStatus](./cmsdecodercreate%28_%29.md)
  Creates a CMSDecoder reference.
- [class CMSDecoder](./cmsdecoder.md)
  An opaque reference to a CMS decoder object.
- [func CMSDecoderGetTypeID() -> CFTypeID](./cmsdecodergettypeid%28%29.md)
  Returns the type identifier for the CMSDecoder opaque type.
### Decoding
- [func CMSDecoderUpdateMessage(CMSDecoder, UnsafeRawPointer, Int) -> OSStatus](./cmsdecoderupdatemessage%28_,_,_%29.md)
  Feeds raw bytes of the message to be decoded into the decoder.
- [func CMSDecoderFinalizeMessage(CMSDecoder) -> OSStatus](./cmsdecoderfinalizemessage%28_%29.md)
  Indicates that there is no more data to decode.
- [func CMSDecoderSetDetachedContent(CMSDecoder, CFData) -> OSStatus](./cmsdecodersetdetachedcontent%28_,_%29.md)
  Specifies the message’s detached content, if any.
- [func CMSDecoderCopyDetachedContent(CMSDecoder, UnsafeMutablePointer<CFData?>) -> OSStatus](./cmsdecodercopydetachedcontent%28_,_%29.md)
  Obtains the detached content specified with the `CMSDecoderSetDetachedContent` function.
### Signature Verification
- [func CMSDecoderSetSearchKeychain(CMSDecoder, CFTypeRef) -> OSStatus](./cmsdecodersetsearchkeychain%28_,_%29.md)
  Specifies the keychains to search for intermediate certificates to be used in verifying a signed message’s signer certificates.
- [func CMSDecoderGetNumSigners(CMSDecoder, UnsafeMutablePointer<Int>) -> OSStatus](./cmsdecodergetnumsigners%28_,_%29.md)
  Obtains the number of signers of a message.
- [func CMSDecoderCopySignerEmailAddress(CMSDecoder, Int, UnsafeMutablePointer<CFString?>) -> OSStatus](./cmsdecodercopysigneremailaddress%28_,_,_%29.md)
  Obtains the email address of the specified signer of a CMS message.
- [func CMSDecoderCopySignerCert(CMSDecoder, Int, UnsafeMutablePointer<SecCertificate?>) -> OSStatus](./cmsdecodercopysignercert%28_,_,_%29.md)
  Obtains the certificate of the specified signer of a CMS message.
- [func CMSDecoderCopySignerStatus(CMSDecoder, Int, CFTypeRef, Bool, UnsafeMutablePointer<CMSSignerStatus>?, UnsafeMutablePointer<SecTrust?>?, UnsafeMutablePointer<OSStatus>?) -> OSStatus](./cmsdecodercopysignerstatus%28_,_,_,_,_,_,_%29.md)
  Obtains the status of a CMS message’s signature.
- [enum CMSSignerStatus](./cmssignerstatus.md)
  The constants that indicate the status of the signature and signer information in a signed message.
### Message Content
- [func CMSDecoderIsContentEncrypted(CMSDecoder, UnsafeMutablePointer<DarwinBoolean>) -> OSStatus](./cmsdecoderiscontentencrypted%28_,_%29.md)
  Determines whether a CMS message was encrypted.
- [func CMSDecoderCopyEncapsulatedContentType(CMSDecoder, UnsafeMutablePointer<CFData?>) -> OSStatus](./cmsdecodercopyencapsulatedcontenttype%28_,_%29.md)
  Obtains the object identifier for the encapsulated data of a signed message.
- [func CMSDecoderCopyAllCerts(CMSDecoder, UnsafeMutablePointer<CFArray?>) -> OSStatus](./cmsdecodercopyallcerts%28_,_%29.md)
  Obtains an array of all of the certificates in a message.
- [func CMSDecoderCopyContent(CMSDecoder, UnsafeMutablePointer<CFData?>) -> OSStatus](./cmsdecodercopycontent%28_,_%29.md)
  Obtains the message content, if any.
### Timestamps
- [func CMSDecoderCopySignerSigningTime(CMSDecoder, Int, UnsafeMutablePointer<CFAbsoluteTime>) -> OSStatus](./cmsdecodercopysignersigningtime%28_,_,_%29.md)
  Obtains the signing time of a CMS message, if present.
- [func CMSDecoderCopySignerTimestamp(CMSDecoder, Int, UnsafeMutablePointer<CFAbsoluteTime>) -> OSStatus](./cmsdecodercopysignertimestamp%28_,_,_%29.md)
  Returns the timestamp of a signer of a CMS message, if present.
- [func CMSDecoderCopySignerTimestampCertificates(CMSDecoder, Int, UnsafeMutablePointer<CFArray?>) -> OSStatus](./cmsdecodercopysignertimestampcertificates%28_,_,_%29.md)
  Returns an array containing the certificates from a timestamp response.
- [func CMSDecoderCopySignerTimestampWithPolicy(CMSDecoder, CFTypeRef?, Int, UnsafeMutablePointer<CFAbsoluteTime>) -> OSStatus](./cmsdecodercopysignertimestampwithpolicy%28_,_,_,_%29.md)
  Returns the timestamp of a signer of a CMS message using a given policy, if present.
- [func CMSEncoderCopySignerTimestamp(CMSEncoder, Int, UnsafeMutablePointer<CFAbsoluteTime>) -> OSStatus](./cmsencodercopysignertimestamp%28_,_,_%29.md)
  Returns the timestamp of a signer of a CMS message, if present.
- [func CMSEncoderCopySignerTimestampWithPolicy(CMSEncoder, CFTypeRef?, Int, UnsafeMutablePointer<CFAbsoluteTime>) -> OSStatus](./cmsencodercopysignertimestampwithpolicy%28_,_,_,_%29.md)
  Returns the timestamp of a signer of a CMS message using a particular policy, if present.


---

*[View on Apple Developer](https://developer.apple.com/documentation/security/cryptographic-message-syntax-services)*