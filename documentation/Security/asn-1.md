# ASN.1

**Framework**: Security  
**Role**: API Collection

Encode and decode Distinguished Encoding Rules (DER) and Basic Encoding Rules (BER) data streams.

#### Overview

You use an ASN.1 coder to encode and decode both DER and BER data streams based on templates that you supply, which in turn are based upon ASN.1 specifications. You must import this API explicitly:

**Swift**:

```swift
import Security.SecAsn1Coder
import Security.SecAsn1Templates
```

**Objective-C**:

```objc
#import <Security/SecAsn1Coder.h>
#import <Security/SecAsn1Templates.h>
```

## Topics

### Encoding
- [typealias SecAsn1Item](./secasn1item.md)
  A structure holding DER encoded data.
- [struct SecAsn1Template_struct](./secasn1template_struct.md)
  A structure that defines one element of a BER or DER encoding.
- [struct SecAsn1Template_struct](./secasn1template_struct.md)
  A structure that defines one element of a BER or DER encoding.
- [typealias SecAsn1TemplateChooser](./secasn1templatechooser.md)
  Dynamically provides the sub-template to use during encode or decode.
- [typealias SecAsn1TemplateChooserPtr](./secasn1templatechooserptr.md)
  A pointer to the template chooser function.
- [Type Tags](./type-tags.md)
  Recognize BER and DER values for ASN.1 identifier octets.
- [SecAsn1EncodeItem](./secasn1encodeitem.md)
  Encodes data in DER format.
- [Generic Templates](./generic-templates.md)
  Use templates for each of the simple types.
### OID Comparison
- [typealias SecAsn1Oid](./secasn1oid.md)
  An object identifier.
- [SecAsn1OidCompare](./secasn1oidcompare.md)
  Compares two decoded object identifiers.
### Public Key Info
- [struct SecAsn1AlgId](./secasn1algid.md)
  A structure identifying an ASN.1 algorithm by its OID, and its corresponding parameters.
- [struct SecAsn1PubKeyInfo](./secasn1pubkeyinfo.md)
  A structure containing a public key and its associated algorithm.
### Coder Creation
- [SecAsn1CoderCreate](./secasn1codercreate.md)
  Creates an ASN.1 coder object.
- [SecAsn1CoderRelease](./secasn1coderrelease.md)
  Destroys an ASN.1 coder object and releases all of its memory.
- [SecAsn1CoderRef](./secasn1coderref.md)
  An object that represents an ASN.1 coder.
### Decoding
- [SecAsn1Decode](./secasn1decode.md)
  Decodes untyped DER data.
- [SecAsn1DecodeData](./secasn1decodedata.md)
  Decodes an ASN.1 item in DER format.
### Memory Management
- [SecAsn1Malloc](./secasn1malloc.md)
  Allocates memory in the coder object’s memory pool.
- [SecAsn1AllocItem](./secasn1allocitem.md)
  Allocates memory for an item’s data field in the coder object’s memory pool.
- [SecAsn1AllocCopy](./secasn1alloccopy.md)
  Allocates memory for an item’s data field in the coder object’s memory pool and copies in a block of data.
- [SecAsn1AllocCopyItem](./secasn1alloccopyitem.md)
  Allocates memory for an item’s data field in the coder object’s memory pool and copies in a block of data from another item.


---

*[View on Apple Developer](https://developer.apple.com/documentation/security/asn-1)*