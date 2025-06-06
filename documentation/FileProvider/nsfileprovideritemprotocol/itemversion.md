# itemVersion

**Framework**: File Provider  
**Kind**: property

A version object that tracks changes to an item.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- macOS 11.0+
- visionOS 1.0+

## Declaration

```swift
optional var itemVersion: NSFileProviderItemVersion { get }
```

#### Discussion

The version object lets you track changes to an item’s content and metadata separately. Updating the version also invalidates the thumbnail cache. For more information, see [`NSFileProviderItemVersion`](nsfileprovideritemversion.md).

## See Also

- [var versionIdentifier: Data?](nsfileprovideritemprotocol/versionidentifier.md)
  A data value used to determine when the item changes.
- [var isMostRecentVersionDownloaded: Bool](nsfileprovideritemprotocol/ismostrecentversiondownloaded.md)
  A Boolean value that indicates whether the item is the most recent version downloaded from the server.


---

*[View on Apple Developer](https://developer.apple.com/documentation/fileprovider/nsfileprovideritemprotocol/itemversion)*