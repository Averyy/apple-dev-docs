# isMostRecentVersionDownloaded

**Framework**: File Provider  
**Kind**: property  
**Role**: Instance Property

A Boolean value that indicates whether the item is the most recent version downloaded from the server.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 11.0+
- macOS 11.0+
- visionOS 1.0+

## Declaration

```swift
optional var isMostRecentVersionDownloaded: Bool { get }
```

```objc
@property (nonatomic, readonly, getter=isMostRecentVersionDownloaded) BOOL mostRecentVersionDownloaded;
```

## See Also

### Tracking Versions
- [var itemVersion: NSFileProviderItemVersion](./itemversion.md)
  A version object that tracks changes to an item.
- [var versionIdentifier: Data?](./versionidentifier.md)
  A data value used to determine when the item changes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/fileprovider/nsfileprovideritemprotocol/ismostrecentversiondownloaded)*