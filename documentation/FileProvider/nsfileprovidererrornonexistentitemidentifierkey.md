# NSFileProviderErrorNonExistentItemIdentifierKey

**Framework**: File Provider  
**Kind**: var

The key for accessing the specified item’s identifier when the item doesn’t exist.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- macOS 11.0+
- visionOS 1.0+

## Declaration

```swift
let NSFileProviderErrorNonExistentItemIdentifierKey: String
```

#### Discussion

Use this key to access the item’s identifier from a [`noSuchItem`](nsfileprovidererror/nosuchitem.md) error’s [`userInfo`](https://developer.apple.com/documentation/Foundation/NSError/userInfo) dictionary.

## See Also

- [struct NSFileProviderError](nsfileprovidererror.md)
  A structure that contains information about File Provider extension errors.
- [NSFileProviderError.Code](nsfileprovidererror/code.md)
  The error codes for the File Provider extension.
- [let NSFileProviderErrorDomain: String](nsfileprovidererrordomain.md)
  The error domain for the File Provider extension.
- [let NSFileProviderErrorItemKey: String](nsfileprovidererroritemkey.md)
  The key for accessing information about sync-related errors.
- [let NSFileProviderErrorCollidingItemKey: String](nsfileprovidererrorcollidingitemkey.md)
  The key for accessing the existing item from a filename collision error’s user info dictionary.


---

*[View on Apple Developer](https://developer.apple.com/documentation/fileprovider/nsfileprovidererrornonexistentitemidentifierkey)*