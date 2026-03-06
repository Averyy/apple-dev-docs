# PagedDocumentLinks

**Framework**: App Store Connect API  
**Kind**: dictionary

Links related to the response document, including paging links.

**Availability**:
- App Store Connect API 1.0+

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
  Self-links to requested resources.
- [object DocumentLinks](documentlinks.md)
  Self-links to documents that can contain information for one or more resources.
- [object RelationshipLinks](relationshiplinks.md)
  Links related to the response document, including self links.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/pageddocumentlinks)*