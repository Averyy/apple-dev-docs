# kSecReturnAttributes

**Framework**: Security  
**Kind**: var  
**Role**: Global Variable

A key whose value is a Boolean indicating whether or not to return item attributes.

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
let kSecReturnAttributes: CFString
```

```c
extern CFStringRef const kSecReturnAttributes;
```

## Discussion

The corresponding value is of type [`CFBoolean`](../CoreFoundation/cfboolean.md). A value of [`kCFBooleanTrue`](../CoreFoundation/kcfbooleantrue.md) indicates that a dictionary of the (unencrypted) attributes of an item should be returned in the form of a [`CFDictionary`](../CoreFoundation/cfdictionary.md) using the keys and values defined in [Item attribute keys and values](./item-attribute-keys-and-values.md).


---

*[View on Apple Developer](https://developer.apple.com/documentation/security/ksecreturnattributes)*