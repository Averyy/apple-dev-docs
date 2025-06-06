# kSecAttrSyncViewHint

**Framework**: Security  
**Kind**: var

A key with a value that’s a string that provides a sync view hint.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
let kSecAttrSyncViewHint: CFString
```

#### Discussion

The corresponding value is of type [`CFString`](https://developer.apple.com/documentation/CoreFoundation/CFString), and is included as part of the primary key of an item. It can be used to help distinguish Sync Views when defining their queries.


---

*[View on Apple Developer](https://developer.apple.com/documentation/security/ksecattrsyncviewhint)*