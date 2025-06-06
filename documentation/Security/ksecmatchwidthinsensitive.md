# kSecMatchWidthInsensitive

**Framework**: Security  
**Kind**: var

A key whose value is a Boolean indicating whether width-insensitive matching is performed.

**Availability**:
- macOS 10.7+

## Declaration

```swift
let kSecMatchWidthInsensitive: CFString
```

#### Discussion

The corresponding value is of type [`CFBoolean`](https://developer.apple.com/documentation/CoreFoundation/CFBoolean). If this value is [`kCFBooleanFalse`](https://developer.apple.com/documentation/CoreFoundation/kCFBooleanFalse), or if this attribute is not provided, then width-sensitive string matching is performed (for example, the ASCII character `a` does not match the UTF-8 full-width letter `a` (`U+FF41`).


---

*[View on Apple Developer](https://developer.apple.com/documentation/security/ksecmatchwidthinsensitive)*