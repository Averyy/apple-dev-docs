# kSecMatchCaseInsensitive

**Framework**: Security  
**Kind**: var  
**Role**: Global Variable

A key whose value is a Boolean indicating whether case-insensitive matching is performed.

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
let kSecMatchCaseInsensitive: CFString
```

```c
extern CFStringRef const kSecMatchCaseInsensitive;
```

#### Discussion

The corresponding value is of type [`CFBoolean`](../CoreFoundation/cfboolean.md). If this value is [`kCFBooleanFalse`](../CoreFoundation/kcfbooleanfalse.md), or if this attribute is not provided, then case-sensitive string matching is performed.


---

*[View on Apple Developer](https://developer.apple.com/documentation/security/ksecmatchcaseinsensitive)*