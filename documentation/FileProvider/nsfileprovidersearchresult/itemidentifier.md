# itemIdentifier

**Framework**: File Provider  
**Kind**: property  
**Required**: Yes

The identifier for this search result.

**Availability**:
- macOS 26.0+

## Declaration

```swift
var itemIdentifier: NSFileProviderItemIdentifier { get }
```

#### Discussion

Choose an identifier that’s usable with API calls from the [`NSFileProviderReplicatedExtension`](nsfileproviderreplicatedextension.md) protocol.

## See Also

- [struct NSFileProviderItemIdentifier](nsfileprovideritemidentifier.md)
  A unique identifier for an item managed by the File Provider extension.
- [var filename: String](nsfileprovidersearchresult/filename.md)
  The result’s file name.


---

*[View on Apple Developer](https://developer.apple.com/documentation/fileprovider/nsfileprovidersearchresult/itemidentifier)*