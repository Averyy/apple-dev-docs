# kSecAttrPort

**Framework**: Security  
**Kind**: var  
**Role**: Global Variable

A key whose value indicates the item’s port.

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
let kSecAttrPort: CFString
```

```c
extern CFStringRef const kSecAttrPort;
```

#### Discussion

The corresponding value is of type [`CFNumber`](../CoreFoundation/cfnumber.md) and represents an Internet port number. Items of class [`kSecClassInternetPassword`](./ksecclassinternetpassword.md) have this attribute.


---

*[View on Apple Developer](https://developer.apple.com/documentation/security/ksecattrport)*