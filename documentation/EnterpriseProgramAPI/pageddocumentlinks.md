# PagedDocumentLinks

**Framework**: Enterprise Program API  
**Kind**: dictionary

Links related to the response document, including paging links.

## Declaration

```swift
object PagedDocumentLinks
```

#### Discussion

All the response data constitutes multiple *documents.*

## Properties

- `first` (uri-reference): The link to the first page of documents.
- `next` (uri-reference): The link to the next page of documents.
- `self` (uri-reference) *(required)*: The link that produced the current document.

## See Also

- [object PagingInformation](paginginformation.md)
  Paging information for data responses.
- [object ResourceLinks](resourcelinks.md)
- [object DocumentLinks](documentlinks.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/enterpriseprogramapi/pageddocumentlinks)*