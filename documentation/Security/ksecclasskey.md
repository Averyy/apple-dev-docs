# kSecClassKey

**Framework**: Security  
**Kind**: var

The value that indicates a cryptographic key item.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- macOS 10.7+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
let kSecClassKey: CFString
```

## Mentions

- [Storing Keys in the Keychain](storing-keys-in-the-keychain.md)

#### Discussion

The following keychain item attributes form the composite primary key of a cryptographic key item:

- [`kSecAttrAccessGroup`](ksecattraccessgroup.md) (on macOS, this key only applies if you set [`kSecUseDataProtectionKeychain`](ksecusedataprotectionkeychain.md) or [`kSecAttrSynchronizable`](ksecattrsynchronizable.md) to [`true`](https://developer.apple.com/documentation/swift/true))
- [`kSecAttrApplicationLabel`](ksecattrapplicationlabel.md)
- [`kSecAttrApplicationTag`](ksecattrapplicationtag.md)
- [`kSecAttrEffectiveKeySize`](ksecattreffectivekeysize.md)
- [`kSecAttrKeyClass`](ksecattrkeyclass.md)
- [`kSecAttrKeySizeInBits`](ksecattrkeysizeinbits.md)
- [`kSecAttrKeyType`](ksecattrkeytype.md)
- [`kSecAttrSynchronizable`](ksecattrsynchronizable.md) (on iOS 14 and newer, iOS 11 newer, and watchOS 7 and newer)

Calls to [`SecItemAdd(_:_:)`](secitemadd(_:_:).md) that add a cryptographic key item with the same values for all of these attributes as an existing item result in [`errSecDuplicateItem`](errsecduplicateitem.md).

The following keychain item attributes apply to a cryptographic key item, and don’t form part of its composite primary key:

- [`kSecAttrAccess`](ksecattraccess.md) (macOS only)
- [`kSecAttrAccessible`](ksecattraccessible.md) (on macOS, this key only applies if you set [`kSecUseDataProtectionKeychain`](ksecusedataprotectionkeychain.md) or [`kSecAttrSynchronizable`](ksecattrsynchronizable.md) to [`true`](https://developer.apple.com/documentation/swift/true))
- [`kSecAttrLabel`](ksecattrlabel.md)
- [`kSecAttrIsPermanent`](ksecattrispermanent.md)
- [`kSecAttrPRF`](ksecattrprf.md)
- [`kSecAttrSalt`](ksecattrsalt.md)
- [`kSecAttrRounds`](ksecattrrounds.md)
- [`kSecAttrCanEncrypt`](ksecattrcanencrypt.md)
- [`kSecAttrCanDecrypt`](ksecattrcandecrypt.md)
- [`kSecAttrCanDerive`](ksecattrcanderive.md)
- [`kSecAttrCanSign`](ksecattrcansign.md)
- [`kSecAttrCanVerify`](ksecattrcanverify.md)
- [`kSecAttrCanWrap`](ksecattrcanwrap.md)
- [`kSecAttrCanUnwrap`](ksecattrcanunwrap.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/security/ksecclasskey)*