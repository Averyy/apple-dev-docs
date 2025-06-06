# ASN.1

**Framework**: Security

Encode and decode Distinguished Encoding Rules (DER) and Basic Encoding Rules (BER) data streams.

#### Overview

You use an ASN.1 coder to encode and decode both DER and BER data streams based on templates that you supply, which in turn are based upon ASN.1 specifications. You must import this API explicitly:

## Topics

### Encoding
- [typealias SecAsn1Item](secasn1item.md)
  A structure holding DER encoded data.
- [struct SecAsn1Template_struct](secasn1template_struct.md)
  A structure that defines one element of a BER or DER encoding.
- [struct SecAsn1Template_struct](secasn1template_struct.md)
  A structure that defines one element of a BER or DER encoding.
- [typealias SecAsn1TemplateChooser](secasn1templatechooser.md)
  Dynamically provides the sub-template to use during encode or decode.
- [typealias SecAsn1TemplateChooserPtr](secasn1templatechooserptr.md)
  A pointer to the template chooser function.
- [Type Tags](type-tags.md)
  Recognize BER and DER values for ASN.1 identifier octets.
### OID Comparison
- [typealias SecAsn1Oid](secasn1oid.md)
  An object identifier.
### Public Key Info
- [struct SecAsn1AlgId](secasn1algid.md)
  A structure identifying an ASN.1 algorithm by its OID, and its corresponding parameters.
- [struct SecAsn1PubKeyInfo](secasn1pubkeyinfo.md)
  A structure containing a public key and its associated algorithm.


---

*[View on Apple Developer](https://developer.apple.com/documentation/security/asn-1)*