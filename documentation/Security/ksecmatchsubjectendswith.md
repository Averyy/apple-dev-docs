# kSecMatchSubjectEndsWith

**Framework**: Security  
**Kind**: var

A key whose value is a string to match against the end of a certificate or identity’s subject.

**Availability**:
- macOS 10.7+

## Declaration

```swift
let kSecMatchSubjectEndsWith: CFString
```

#### Discussion

The corresponding value is of type [`CFString`](https://developer.apple.com/documentation/CoreFoundation/CFString). If provided, returned certificates or identities are limited to those whose subject ends with this string.


---

*[View on Apple Developer](https://developer.apple.com/documentation/security/ksecmatchsubjectendswith)*