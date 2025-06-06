# kSecValueRef

**Framework**: Security  
**Kind**: var

A key whose value is a reference to the item.

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
let kSecValueRef: CFString
```

#### Discussion

The corresponding value, depending on the item class requested, is of type [`SecKeychainItem`](seckeychainitem.md), [`SecKey`](seckey.md), [`SecCertificate`](seccertificate.md), or [`SecIdentity`](secidentity.md).


---

*[View on Apple Developer](https://developer.apple.com/documentation/security/ksecvalueref)*