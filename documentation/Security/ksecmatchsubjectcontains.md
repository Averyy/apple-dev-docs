# kSecMatchSubjectContains

**Framework**: Security  
**Kind**: var  
**Role**: Global Variable

A key whose value is a string to look for in a certificate or identity’s subject.

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
let kSecMatchSubjectContains: CFString
```

```c
extern CFStringRef const kSecMatchSubjectContains;
```

## Discussion

The corresponding value is of type [`CFString`](../CoreFoundation/cfstring.md). If provided, returned certificates or identities are limited to those whose subject contains this string.


---

*[View on Apple Developer](https://developer.apple.com/documentation/security/ksecmatchsubjectcontains)*