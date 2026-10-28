# kSecMatchDiacriticInsensitive

**Framework**: Security  
**Kind**: var  
**Role**: Global Variable

A key whose value is a Boolean indicating whether diacritic-insensitive matching is performed.

**Availability**:
- macOS 10.7+

## Declaration

```swift
let kSecMatchDiacriticInsensitive: CFString
```

```c
extern CFStringRef const kSecMatchDiacriticInsensitive;
```

## Discussion

The corresponding value is of type [`CFBoolean`](../CoreFoundation/cfboolean.md). If this value is [`kCFBooleanFalse`](../CoreFoundation/kcfbooleanfalse.md), or if this attribute is not provided, then diacritic-sensitive string matching is performed.


---

*[View on Apple Developer](https://developer.apple.com/documentation/security/ksecmatchdiacriticinsensitive)*