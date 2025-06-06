# Transform Attributes

**Framework**: Security

Specify the attributes of a transform.

#### Overview

Use these keys and values when accessing transform attributes by name, such as with the [`SecTransformSetAttribute(_:_:_:_:)`](sectransformsetattribute(_:_:_:_:).md) and [`SecTransformGetAttribute(_:_:)`](sectransformgetattribute(_:_:).md) functions. You can also use some of the values directly in certain function calls, such as when you create a encode transform with the [`SecEncodeTransformCreate(_:_:)`](secencodetransformcreate(_:_:).md) function and give it an `encodeType` parameter to seed the [`kSecEncodeTypeAttribute`](ksecencodetypeattribute.md) attribute.

## Topics

### Encode and Decode Keys
- [let kSecEncodeLineLengthAttribute: CFString](ksecencodelinelengthattribute.md)
  The length of encoded Base32 or Base64 lines.
- [let kSecEncodeTypeAttribute: CFString](ksecencodetypeattribute.md)
  The encoding used by an encode transform.
- [let kSecDecodeTypeAttribute: CFString](ksecdecodetypeattribute.md)
  The encoding used by a decode transform.
- [let kSecCompressionRatio: CFString](kseccompressionratio.md)
  The compression ratio.
### Digest and Encryption Keys
- [let kSecDigestTypeAttribute: CFString](ksecdigesttypeattribute.md)
  The digest algorithm.
- [let kSecDigestLengthAttribute: CFString](ksecdigestlengthattribute.md)
  The digest length.
- [let kSecDigestHMACKeyAttribute: CFString](ksecdigesthmackeyattribute.md)
  The key for HMAC operation.
- [let kSecInputIsAttributeName: CFString](ksecinputisattributename.md)
  The type of input to the transform.
- [let kSecEncryptionMode: CFString](ksecencryptionmode.md)
  The encryption mode.
- [let kSecEncryptKey: CFString](ksecencryptkey.md)
  The encryption key for the transform.
- [let kSecIVKey: CFString](ksecivkey.md)
  The setting for an initialization vector.
- [let kSecPaddingKey: CFString](ksecpaddingkey.md)
  The kind of padding to use.
- [let kSecOAEPEncodingParametersAttributeName: CFString](ksecoaepencodingparametersattributename.md)
  The OAEP encoding parameters.
- [let kSecOAEPMGF1DigestAlgorithmAttributeName: CFString](ksecoaepmgf1digestalgorithmattributename.md)
  The OAEP MGF1 digest algorithm.
- [let kSecOAEPMessageLengthAttributeName: CFString](ksecoaepmessagelengthattributename.md)
  The OAEP message length.
### Transform Keys
- [let kSecTransformInputAttributeName: CFString](ksectransforminputattributename.md)
  The input to a transform.
- [let kSecTransformOutputAttributeName: CFString](ksectransformoutputattributename.md)
  The output of a transform.
- [let kSecTransformDebugAttributeName: CFString](ksectransformdebugattributename.md)
  A write stream that should receive debug data.
- [let kSecKeyAttributeName: CFString](kseckeyattributename.md)
  The cryptographic key associated with a transform.
- [let kSecSignatureAttributeName: CFString](ksecsignatureattributename.md)
  The cryptographic signature associated with a transform.
- [let kSecTransformAbortAttributeName: CFString](ksectransformabortattributename.md)
  The reason for an abort.
- [let kSecTransformTransformName: CFString](ksectransformtransformname.md)
  The name of a transform.
### Encode Types
- [let kSecBase32Encoding: CFString](ksecbase32encoding.md)
  A base 32 encoding.
- [let kSecBase64Encoding: CFString](ksecbase64encoding.md)
  A base 64 encoding.
- [let kSecZLibEncoding: CFString](kseczlibencoding.md)
  A compressed encoding.
### Digest Types
- [let kSecDigestMD2: CFString](ksecdigestmd2.md)
  An MD2 digest.
- [let kSecDigestMD4: CFString](ksecdigestmd4.md)
  An MD4 digest.
- [let kSecDigestMD5: CFString](ksecdigestmd5.md)
  An MD5 digest.
- [let kSecDigestSHA1: CFString](ksecdigestsha1.md)
  An SHA1 digest.
- [let kSecDigestSHA2: CFString](ksecdigestsha2.md)
  An SHA2 digest.
- [let kSecDigestHMACMD5: CFString](ksecdigesthmacmd5.md)
  An HMAC using the MD5 digest algorithm.
- [let kSecDigestHMACSHA1: CFString](ksecdigesthmacsha1.md)
  An HMAC using the SHA1 digest algorithm.
- [let kSecDigestHMACSHA2: CFString](ksecdigesthmacsha2.md)
  An HMAC using one of the SHA2 digest algorithms.
### Line Lengths
- [let kSecLineLength64: CFString](kseclinelength64.md)
  A line length of 64 bytes.
- [let kSecLineLength76: CFString](kseclinelength76.md)
  A line length of 76 bytes.
### Input Types
- [let kSecInputIsDigest: CFString](ksecinputisdigest.md)
  The input is a digest of the original data.
- [let kSecInputIsPlainText: CFString](ksecinputisplaintext.md)
  The input is plain text.
- [let kSecInputIsRaw: CFString](ksecinputisraw.md)
  The input is raw.
### Padding Types
- [let kSecPaddingNoneKey: CFString](ksecpaddingnonekey.md)
  No padding will be used when encrypting or decrypting.
- [let kSecPaddingOAEPKey: CFString](ksecpaddingoaepkey.md)
  PKCS7 padding will be used when encrypting or decrypting.
- [let kSecPaddingPKCS1Key: CFString](ksecpaddingpkcs1key.md)
  PKCS1 padding will be used when encrypting or decrypting.
- [let kSecPaddingPKCS5Key: CFString](ksecpaddingpkcs5key.md)
  PKCS5 padding will be used when encrypting or decrypting.
- [let kSecPaddingPKCS7Key: CFString](ksecpaddingpkcs7key.md)
  PKCS7 padding will be used when encrypting or decrypting.
### Encryption Modes
- [let kSecModeNoneKey: CFString](ksecmodenonekey.md)
  No mode will be used when encrypting or decrypting.
- [let kSecModeCBCKey: CFString](ksecmodecbckey.md)
  CBC mode will be used when encrypting or decrypting.
- [let kSecModeCFBKey: CFString](ksecmodecfbkey.md)
  CFB mode will be used when encrypting or decrypting.
- [let kSecModeECBKey: CFString](ksecmodeecbkey.md)
  ECB mode will be used when encrypting or decrypting.
- [let kSecModeOFBKey: CFString](ksecmodeofbkey.md)
  OFB mode will be used when encrypting or decrypting.


---

*[View on Apple Developer](https://developer.apple.com/documentation/security/transform-attributes)*