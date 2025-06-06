# NSFileProviderErrorItemKey

**Framework**: File Provider  
**Kind**: var

The key for accessing information about sync-related errors.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- macOS 10.15+
- visionOS 1.0+

## Declaration

```swift
let NSFileProviderErrorItemKey: String
```

#### Discussion

If a specific item caused the error, the system sets the [`NSFileProviderErrorItemKey`](nsfileprovidererroritemkey.md) key to the item’s identifier, and it sets the [`NSUnderlyingErrorKey`](https://developer.apple.com/documentation/Foundation/NSUnderlyingErrorKey) key to the error encountered by the item.

## See Also

- [struct NSFileProviderError](nsfileprovidererror.md)
  A structure that contains information about File Provider extension errors.
- [NSFileProviderError.Code](nsfileprovidererror/code.md)
  The error codes for the File Provider extension.
- [let NSFileProviderErrorDomain: String](nsfileprovidererrordomain.md)
  The error domain for the File Provider extension.
- [let NSFileProviderErrorNonExistentItemIdentifierKey: String](nsfileprovidererrornonexistentitemidentifierkey.md)
  The key for accessing the specified item’s identifier when the item doesn’t exist.
- [let NSFileProviderErrorCollidingItemKey: String](nsfileprovidererrorcollidingitemkey.md)
  The key for accessing the existing item from a filename collision error’s user info dictionary.


---

*[View on Apple Developer](https://developer.apple.com/documentation/fileprovider/nsfileprovidererroritemkey)*