# kSecMatchSubjectEndsWith

**Framework**: Security  
**Kind**: var  
**Role**: Global Variable

A key whose value is a string to match against the end of a certificate or identity’s subject.

**Availability**:
- macOS 10.7+

## Declaration

```swift
let kSecMatchSubjectEndsWith: CFString
```

```c
extern CFStringRef const kSecMatchSubjectEndsWith;
```

## Discussion

The corresponding value is of type [`CFString`](../CoreFoundation/cfstring.md). If provided, returned certificates or identities are limited to those whose subject ends with this string.


---

*[View on Apple Developer](https://developer.apple.com/documentation/security/ksecmatchsubjectendswith)*