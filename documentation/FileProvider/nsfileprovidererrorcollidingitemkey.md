# NSFileProviderErrorCollidingItemKey

**Framework**: File Provider  
**Kind**: var  
**Role**: Global Variable

The key for accessing the existing item from a filename collision error’s user info dictionary.

**Availability**:
- iOS 8.0+ - Deprecated in 13.0
- iPadOS 8.0+ - Deprecated in 13.0
- Mac Catalyst 8.0+ - Deprecated in 13.0
- visionOS 1.0+ - Deprecated in 1.0

> **Deprecated**: Use [`NSFileProviderErrorItemKey`](./nsfileprovidererroritemkey.md) instead.

## Declaration

```swift
let NSFileProviderErrorCollidingItemKey: String
```

```c
extern NSErrorUserInfoKey const NSFileProviderErrorCollidingItemKey;
```

## See Also

### Errors
- [struct NSFileProviderError](./nsfileprovidererror.md)
  A structure that contains information about File Provider extension errors.
- [NSFileProviderError.Code](./nsfileprovidererror/code.md)
  The error codes for the File Provider extension.
- [let NSFileProviderErrorDomain: String](./nsfileprovidererrordomain.md)
  The error domain for the File Provider extension.
- [let NSFileProviderErrorItemKey: String](./nsfileprovidererroritemkey.md)
  The key for accessing information about sync-related errors.
- [let NSFileProviderErrorNonExistentItemIdentifierKey: String](./nsfileprovidererrornonexistentitemidentifierkey.md)
  The key for accessing the specified item’s identifier when the item doesn’t exist.


---

*[View on Apple Developer](https://developer.apple.com/documentation/fileprovider/nsfileprovidererrorcollidingitemkey)*