# kSecMatchDiacriticInsensitive

**Framework**: Security  
**Kind**: var

A key whose value is a Boolean indicating whether diacritic-insensitive matching is performed.

**Availability**:
- macOS 10.7+

## Declaration

```swift
let kSecMatchDiacriticInsensitive: CFString
```

#### Discussion

The corresponding value is of type [`CFBoolean`](https://developer.apple.com/documentation/CoreFoundation/CFBoolean). If this value is [`kCFBooleanFalse`](https://developer.apple.com/documentation/CoreFoundation/kCFBooleanFalse), or if this attribute is not provided, then diacritic-sensitive string matching is performed.


---

*[View on Apple Developer](https://developer.apple.com/documentation/security/ksecmatchdiacriticinsensitive)*