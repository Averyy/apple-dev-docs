# kSecReturnData

**Framework**: Security  
**Kind**: var  
**Role**: Global Variable

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

```c
extern CFStringRef const kSecReturnData;
```

## Mentions

- [Searching for keychain items](./searching-for-keychain-items.md)

## Discussion

The corresponding value is of type [`CFBoolean`](../CoreFoundation/cfboolean.md). A value of [`kCFBooleanTrue`](../CoreFoundation/kcfbooleantrue.md) indicates that the function needs to return the item’s data as a [`CFData`](../CoreFoundation/cfdata.md) object.

For keys and password items, data is secret (encrypted) and might require the user to enter a password for access. For key items, the resulting data has the same format as the return value of the function [`SecKeyCopyExternalRepresentation(_:_:)`](./seckeycopyexternalrepresentation%28_,_%29.md). However, the key data might not be extractable (for example, if it’s protected by the Secure Enclave), so prefer to use [`SecKeyCopyExternalRepresentation(_:_:)`](./seckeycopyexternalrepresentation%28_,_%29.md) for keys and check the `error` parameter if it returns `nil`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/security/ksecreturndata)*