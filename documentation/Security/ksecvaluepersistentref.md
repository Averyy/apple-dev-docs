# kSecValuePersistentRef

**Framework**: Security  
**Kind**: var

A key whose value is a persistent reference to the item.

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
let kSecValuePersistentRef: CFString
```

#### Discussion

The corresponding value is of type [`CFData`](https://developer.apple.com/documentation/CoreFoundation/CFData). The bytes in this object can be stored by the caller and used on a subsequent invocation of the application (or even a different application) to retrieve the item referenced by it.


---

*[View on Apple Developer](https://developer.apple.com/documentation/security/ksecvaluepersistentref)*