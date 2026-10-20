# kSecAttrIsInvisible

**Framework**: Security  
**Kind**: var  
**Role**: Global Variable

A key with a value that’s a Boolean indicating the item’s visibility.

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
let kSecAttrIsInvisible: CFString
```

```c
extern CFStringRef const kSecAttrIsInvisible;
```

#### Discussion

The corresponding value is of type [`CFBoolean`](../CoreFoundation/cfboolean.md) and is [`kCFBooleanTrue`](../CoreFoundation/kcfbooleantrue.md) if the item is invisible (that is, should not be displayed).


---

*[View on Apple Developer](https://developer.apple.com/documentation/security/ksecattrisinvisible)*