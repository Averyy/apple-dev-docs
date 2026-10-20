# versionIdentifier

**Framework**: File Provider  
**Kind**: property  
**Role**: Instance Property

A data value used to determine when the item changes.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 11.0+
- visionOS 1.0+

## Declaration

```swift
optional var versionIdentifier: Data? { get }
```

```objc
@property (nonatomic, strong, readonly, nullable) NSData * versionIdentifier;
```

#### Discussion

This property contains a data object that can uniquely identify each version of the item; for example, the hash of a document’s contents.

Version identifiers are limited to 1000 bytes.

## See Also

### Tracking Versions
- [var itemVersion: NSFileProviderItemVersion](./itemversion.md)
  A version object that tracks changes to an item.
- [var isMostRecentVersionDownloaded: Bool](./ismostrecentversiondownloaded.md)
  A Boolean value that indicates whether the item is the most recent version downloaded from the server.


---

*[View on Apple Developer](https://developer.apple.com/documentation/fileprovider/nsfileprovideritemprotocol/versionidentifier)*