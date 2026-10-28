# itemIdentifier

**Framework**: File Provider  
**Kind**: property  
**Role**: Instance Property  
**Required**: Yes

The identifier for this search result.

**Availability**:
- macOS 26.0+

## Declaration

```swift
var itemIdentifier: NSFileProviderItemIdentifier { get }
```

```objc
@property (nonatomic, copy, readonly) NSFileProviderItemIdentifier itemIdentifier;
```

## Discussion

Choose an identifier that’s usable with API calls from the [`NSFileProviderReplicatedExtension`](../nsfileproviderreplicatedextension.md) protocol.

## See Also

### Identifying the item
- [struct NSFileProviderItemIdentifier](../nsfileprovideritemidentifier.md)
  A unique identifier for an item managed by the File Provider extension.
- [var filename: String](./filename.md)
  The result’s file name.


---

*[View on Apple Developer](https://developer.apple.com/documentation/fileprovider/nsfileprovidersearchresult/itemidentifier)*