# Keychain Item Attribute Constants For Keys

**Framework**: Security

Specifies the attributes for a key item in a keychain.

#### Overview

For attributes for items other than keys, see [`SecItemAttr`](secitemattr.md).

## Topics

### Constants
- [var kSecKeyKeyClass: Int32](kseckeykeyclass.md)
  Type uint32 (`CSSM_KEYCLASS`); value is one of `CSSM_KEYCLASS_PUBLIC_KEY`, `CSSM_KEYCLASS_PRIVATE_KEY` or `CSSM_KEYCLASS_SESSION_KEY`.
- [var kSecKeyPrintName: Int32](kseckeyprintname.md)
  Type blob; human readable name of the key. Same as `kSecLabelItemAttr` for typical keychain items.
- [var kSecKeyAlias: Int32](kseckeyalias.md)
  Type blob; currently unused.
- [var kSecKeyPermanent: Int32](kseckeypermanent.md)
  Type uint32; value is nonzero. This key is permanent (stored in some keychain) and is always `1`.
- [var kSecKeyPrivate: Int32](kseckeyprivate.md)
  Type uint32; value is nonzero. This key is protected by a user login, a password, or both.
- [var kSecKeyModifiable: Int32](kseckeymodifiable.md)
  Type uint32; value is nonzero. Attributes of this key can be modified.
- [var kSecKeyLabel: Int32](kseckeylabel.md)
- [var kSecKeyApplicationTag: Int32](kseckeyapplicationtag.md)
  Type blob; currently unused.
- [var kSecKeyKeyCreator: Int32](kseckeykeycreator.md)
  Type data. The data points to a `CSSM_GUID` structure representing the module ID of the CSP owning this key.
- [var kSecKeyKeyType: Int32](kseckeykeytype.md)
  Type uint32; value is a CSSM algorithm (`CSSM_ALGORITHMS`) representing the algorithm associated with this key.
- [var kSecKeyKeySizeInBits: Int32](kseckeykeysizeinbits.md)
  Type uint32; value is the number of bits in this key.
- [var kSecKeyEffectiveKeySize: Int32](kseckeyeffectivekeysize.md)
  Type uint32; value is the effective number of bits in this key.  For example, a DES key has a key size in bits (`kSecKeyKeySizeInBits`) of 64 but a value for `kSecKeyEffectiveKeySize` of 56.
- [var kSecKeyStartDate: Int32](kseckeystartdate.md)
  Type `CSSM_DATE`.  Earliest date at which this key may be used.  If the value is all zeros or not present, no restriction applies.
- [var kSecKeyEndDate: Int32](kseckeyenddate.md)
  Type `CSSM_DATE`.  Latest date at which this key may be used.  If the value is all zeros or not present, no restriction applies.
- [var kSecKeySensitive: Int32](kseckeysensitive.md)
  Type uint32; value is nonzero. This key cannot be wrapped with `CSSM_ALGID_NONE`.
- [var kSecKeyAlwaysSensitive: Int32](kseckeyalwayssensitive.md)
  Type uint32; value is nonzero. This key has always been marked sensitive.
- [var kSecKeyExtractable: Int32](kseckeyextractable.md)
  Type uint32; value is nonzero. This key can be wrapped.
- [var kSecKeyNeverExtractable: Int32](kseckeyneverextractable.md)
  Type uint32; value is nonzero. This key was never marked extractable.
- [var kSecKeyEncrypt: Int32](kseckeyencrypt.md)
  Type uint32; value is nonzero. This key can be used in an encrypt operation.
- [var kSecKeyDecrypt: Int32](kseckeydecrypt.md)
  Type uint32; value is nonzero. This key can be used in a decrypt operation.
- [var kSecKeyDerive: Int32](kseckeyderive.md)
  Type uint32; value is nonzero. This key can be used in a key derivation operation.
- [var kSecKeySign: Int32](kseckeysign.md)
  Type uint32, value is nonzero. This key can be used in a sign operation.
- [var kSecKeyVerify: Int32](kseckeyverify.md)
  Type uint32, value is nonzero. This key can be used in a verify operation.
- [var kSecKeySignRecover: Int32](kseckeysignrecover.md)
  Type uint32.
- [var kSecKeyVerifyRecover: Int32](kseckeyverifyrecover.md)
  Type uint32. This key can unwrap other keys.
- [var kSecKeyWrap: Int32](kseckeywrap.md)
  Type uint32; value is nonzero. This key can wrap other keys.
- [var kSecKeyUnwrap: Int32](kseckeyunwrap.md)
  Type uint32; value is nonzero. This key can unwrap other keys.


---

*[View on Apple Developer](https://developer.apple.com/documentation/security/keychain-item-attribute-constants-for-keys)*