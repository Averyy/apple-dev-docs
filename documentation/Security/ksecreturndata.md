# kSecReturnData

**Framework**: Security  
**Kind**: var

A key whose value is a Boolean that indicates whether or not to return item data.

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
let kSecReturnData: CFString
```

## Mentions

- [Searching for keychain items](searching-for-keychain-items.md)

#### Discussion

The corresponding value is of type [`CFBoolean`](https://developer.apple.com/documentation/CoreFoundation/CFBoolean). A value of [`kCFBooleanTrue`](https://developer.apple.com/documentation/CoreFoundation/kCFBooleanTrue) indicates that the function needs to return the item’s data as a [`CFData`](https://developer.apple.com/documentation/CoreFoundation/CFData) object.

For keys and password items, data is secret (encrypted) and might require the user to enter a password for access. For key items, the resulting data has the same format as the return value of the function [`SecKeyCopyExternalRepresentation(_:_:)`](seckeycopyexternalrepresentation(_:_:).md). However, the key data might not be extractable (for example, if it’s protected by the Secure Enclave), so prefer to use [`SecKeyCopyExternalRepresentation(_:_:)`](seckeycopyexternalrepresentation(_:_:).md) for keys and check the `error` parameter if it returns `nil`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/security/ksecreturndata)*