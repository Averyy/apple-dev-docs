# kSecAttrAccessible

**Framework**: Security  
**Kind**: var

A key with a value that indicates when the keychain item is accessible.

**Availability**:
- iOS 4.0+
- iPadOS 4.0+
- Mac Catalyst 13.1+
- macOS 10.9+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
let kSecAttrAccessible: CFString
```

## Mentions

- [Restricting keychain item accessibility](restricting-keychain-item-accessibility.md)

#### Discussion

The corresponding value, one of those found in [`Accessibility Values`](item-attribute-keys-and-values#Accessibility-Values.md), indicates when your app needs access to the data in a keychain item. Choose the most restrictive option that meets your app’s needs so that the system can protect that item to the greatest extent possible. For more information, see [`Restricting keychain item accessibility`](restricting-keychain-item-accessibility.md).

> ❗ **Important**:  You can use this attribute for macOS keychain items only if you also set a value of `true` for the [`kSecUseDataProtectionKeychain`](ksecusedataprotectionkeychain.md) key, the [`kSecAttrSynchronizable`](ksecattrsynchronizable.md) key, or both. For any item marked as synchronizable, the value for the [`kSecAttrAccessible`](ksecattraccessible.md) key may only be one whose name does not end with `ThisDeviceOnly`, as those cannot sync to another device.

 You can use this attribute for macOS keychain items only if you also set a value of `true` for the [`kSecUseDataProtectionKeychain`](ksecusedataprotectionkeychain.md) key, the [`kSecAttrSynchronizable`](ksecattrsynchronizable.md) key, or both. For any item marked as synchronizable, the value for the [`kSecAttrAccessible`](ksecattraccessible.md) key may only be one whose name does not end with `ThisDeviceOnly`, as those cannot sync to another device.

> **Note**:  The app  provide the contents of the keychain item ([`kSecValueData`](ksecvaluedata.md)) when changing this attribute in iOS 4 and earlier.

 The app  provide the contents of the keychain item ([`kSecValueData`](ksecvaluedata.md)) when changing this attribute in iOS 4 and earlier.


---

*[View on Apple Developer](https://developer.apple.com/documentation/security/ksecattraccessible)*