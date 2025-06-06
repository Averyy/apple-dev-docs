# kSecReturnRef

**Framework**: Security  
**Kind**: var

A key whose value is a Boolean indicating whether or not to return a reference to an item.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- macOS 10.6+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
let kSecReturnRef: CFString
```

## Mentions

- [Storing a Certificate in the Keychain](storing-a-certificate-in-the-keychain.md)

#### Discussion

The corresponding value is of type [`CFBoolean`](https://developer.apple.com/documentation/CoreFoundation/CFBoolean). A value of [`kCFBooleanTrue`](https://developer.apple.com/documentation/CoreFoundation/kCFBooleanTrue) indicates that a reference should be returned. Depending on the item class requested, the returned references may be of type [`SecKeychainItem`](seckeychainitem.md), [`SecKey`](seckey.md), [`SecCertificate`](seccertificate.md), [`SecIdentity`](secidentity.md), or [`CFData`](https://developer.apple.com/documentation/CoreFoundation/CFData).


---

*[View on Apple Developer](https://developer.apple.com/documentation/security/ksecreturnref)*