# kSecAttrCreationDate

**Framework**: Security  
**Kind**: var  
**Role**: Global Variable

A key with a value that indicates the item’s creation date.

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
let kSecAttrCreationDate: CFString
```

```c
extern CFStringRef const kSecAttrCreationDate;
```

## Discussion

The corresponding value is of type [`CFDate`](../CoreFoundation/cfdate.md) and represents the date the item was created. Read only.


---

*[View on Apple Developer](https://developer.apple.com/documentation/security/ksecattrcreationdate)*