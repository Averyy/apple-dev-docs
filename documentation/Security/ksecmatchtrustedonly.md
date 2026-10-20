# kSecMatchTrustedOnly

**Framework**: Security  
**Kind**: var  
**Role**: Global Variable

A key whose value is a Boolean indicating whether untrusted certificates should be returned.

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
let kSecMatchTrustedOnly: CFString
```

```c
extern CFStringRef const kSecMatchTrustedOnly;
```

#### Discussion

The corresponding value is of type [`CFBoolean`](../CoreFoundation/cfboolean.md). If this attribute is provided with a value of [`kCFBooleanTrue`](../CoreFoundation/kcfbooleantrue.md), only certificates that can be verified back to a trusted anchor are returned. If this value is [`kCFBooleanFalse`](../CoreFoundation/kcfbooleanfalse.md) or the attribute is not provided, then both trusted and untrusted certificates may be returned.


---

*[View on Apple Developer](https://developer.apple.com/documentation/security/ksecmatchtrustedonly)*