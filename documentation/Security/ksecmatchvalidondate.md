# kSecMatchValidOnDate

**Framework**: Security  
**Kind**: var

A key whose value indicates the validity date.

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
let kSecMatchValidOnDate: CFString
```

#### Discussion

The corresponding value is of type [`CFDate`](https://developer.apple.com/documentation/CoreFoundation/CFDate). If provided, returned keys, certificates or identities are limited to those that are valid for the given date. Pass a value of [`kCFNull`](https://developer.apple.com/documentation/CoreFoundation/kCFNull) to indicate the current date.


---

*[View on Apple Developer](https://developer.apple.com/documentation/security/ksecmatchvalidondate)*