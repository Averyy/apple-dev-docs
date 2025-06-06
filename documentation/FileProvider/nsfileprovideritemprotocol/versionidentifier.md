# versionIdentifier

**Framework**: File Provider  
**Kind**: property

A data value used to determine when the item changes.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- visionOS 1.0+

## Declaration

```swift
optional var versionIdentifier: Data? { get }
```

#### Discussion

This property contains a data object that can uniquely identify each version of the item; for example, the hash of a document’s contents.

Version identifiers are limited to 1000 bytes.

## See Also

- [var itemVersion: NSFileProviderItemVersion](nsfileprovideritemprotocol/itemversion.md)
  A version object that tracks changes to an item.
- [var isMostRecentVersionDownloaded: Bool](nsfileprovideritemprotocol/ismostrecentversiondownloaded.md)
  A Boolean value that indicates whether the item is the most recent version downloaded from the server.


---

*[View on Apple Developer](https://developer.apple.com/documentation/fileprovider/nsfileprovideritemprotocol/versionidentifier)*