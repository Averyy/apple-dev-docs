# NSFileProviderSearchResult

**Framework**: File Provider  
**Kind**: protocol

A protocol that defines properties of a search result.

**Availability**:
- macOS 26.0+

## Declaration

```swift
protocol NSFileProviderSearchResult
```

## Topics

### Identifying the item
- [var itemIdentifier: NSFileProviderItemIdentifier](nsfileprovidersearchresult/itemidentifier.md)
  The identifier for this search result.
- [struct NSFileProviderItemIdentifier](nsfileprovideritemidentifier.md)
  A unique identifier for an item managed by the File Provider extension.
- [var filename: String](nsfileprovidersearchresult/filename.md)
  The result’s file name.
### Accessing file metadata
- [var creationDate: Date?](nsfileprovidersearchresult/creationdate.md)
  The result file’s creation date.
- [var contentModificationDate: Date?](nsfileprovidersearchresult/contentmodificationdate.md)
  The result file’s content modification date.
- [var lastUsedDate: Date?](nsfileprovidersearchresult/lastuseddate.md)
  The result file’s last-used date.
- [var contentType: UTType](nsfileprovidersearchresult/contenttype.md)
  The result file’s content type.
- [var documentSize: NSNumber?](nsfileprovidersearchresult/documentsize.md)
  The result file’s size.

## See Also

- [func didEnumerate([any NSFileProviderSearchResult])](nsfileprovidersearchenumerationobserver/didenumerate(_:).md)
  Delivers an array of search results to the observer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/fileprovider/nsfileprovidersearchresult)*