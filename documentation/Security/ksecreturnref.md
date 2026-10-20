# kSecReturnRef

**Framework**: Security  
**Kind**: var  
**Role**: Global Variable

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

```c
extern CFStringRef const kSecReturnRef;
```

## Mentions

- [Storing a Certificate in the Keychain](./storing-a-certificate-in-the-keychain.md)

#### Discussion

The corresponding value is of type [`CFBoolean`](../CoreFoundation/cfboolean.md). A value of [`kCFBooleanTrue`](../CoreFoundation/kcfbooleantrue.md) indicates that a reference should be returned. Depending on the item class requested, the returned references may be of type [`SecKeychainItem`](./seckeychainitem.md), [`SecKey`](./seckey.md), [`SecCertificate`](./seccertificate.md), [`SecIdentity`](./secidentity.md), or [`CFData`](../CoreFoundation/cfdata.md).


---

*[View on Apple Developer](https://developer.apple.com/documentation/security/ksecreturnref)*