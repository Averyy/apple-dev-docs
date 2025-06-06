# kSecReturnPersistentRef

**Framework**: Security  
**Kind**: var

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

#### Discussion

The corresponding value is of type [`CFBoolean`](https://developer.apple.com/documentation/CoreFoundation/CFBoolean). A value of [`kCFBooleanTrue`](https://developer.apple.com/documentation/CoreFoundation/kCFBooleanTrue) indicates that a persistent reference to an item should be returned as a [`CFData`](https://developer.apple.com/documentation/CoreFoundation/CFData) object. Unlike normal references, a persistent reference may be stored on disk or passed between processes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/security/ksecreturnpersistentref)*