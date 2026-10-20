# kSecReturnPersistentRef

**Framework**: Security  
**Kind**: var  
**Role**: Global Variable

A key whose value is a Boolean indicating whether or not to return a persistent reference to an item.

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
let kSecReturnPersistentRef: CFString
```

```c
extern CFStringRef const kSecReturnPersistentRef;
```

#### Discussion

The corresponding value is of type [`CFBoolean`](../CoreFoundation/cfboolean.md). A value of [`kCFBooleanTrue`](../CoreFoundation/kcfbooleantrue.md) indicates that a persistent reference to an item should be returned as a [`CFData`](../CoreFoundation/cfdata.md) object. Unlike normal references, a persistent reference may be stored on disk or passed between processes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/security/ksecreturnpersistentref)*