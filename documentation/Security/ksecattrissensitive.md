# kSecAttrIsSensitive

**Framework**: Security  
**Kind**: var  
**Role**: Global Variable

A key whose value indicates the item’s sensitivity.

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
let kSecAttrIsSensitive: CFString
```

```c
extern CFStringRef const kSecAttrIsSensitive;
```

#### Discussion

The corresponding value is of type [`CFBoolean`](../CoreFoundation/cfboolean.md). When set to [`kCFBooleanTrue`](../CoreFoundation/kcfbooleantrue.md), the item can only be exported in an encrypted format. Items of class [`kSecClassKey`](./ksecclasskey.md) have this attribute.


---

*[View on Apple Developer](https://developer.apple.com/documentation/security/ksecattrissensitive)*