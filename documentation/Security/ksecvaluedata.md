# kSecValueData

**Framework**: Security  
**Kind**: var

A key whose value is the item’s data.

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
let kSecValueData: CFString
```

## Mentions

- [Searching for keychain items](searching-for-keychain-items.md)
- [Updating and deleting keychain items](updating-and-deleting-keychain-items.md)

#### Discussion

The corresponding value is of type [`CFData`](https://developer.apple.com/documentation/CoreFoundation/CFData).  For keys and password items, the data is secret (encrypted) and may require the user to enter a password for access.


---

*[View on Apple Developer](https://developer.apple.com/documentation/security/ksecvaluedata)*