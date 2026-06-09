# AppTagsResponse

**Framework**: App Store Connect API  
**Kind**: dictionary

A response containing a list of tags associated with apps.

**Availability**:
- App Store Connect API 4.1+

## Declaration

```swift
object AppTagsResponse
```

## Properties

- `data` ([AppTag]) *(required)*
- `included` ([Territory])
- `links` (PagedDocumentLinks) *(required)*
- `meta` (PagingInformation)

## See Also

- [object AppAppTagsLinkagesResponse](appapptagslinkagesresponse.md)
  A response containing the resource identifiers of tags associated with an app.
- [object AppTag](apptag.md)
  A label used to categorize an app for internal organization or to control which App Store territories feature it.
- [object AppTagResponse](apptagresponse.md)
  A response containing a single app tag.
- [object AppTagTerritoriesLinkagesResponse](apptagterritorieslinkagesresponse.md)
  A response containing the resource identifiers of territories associated with an app tag.
- [object AppTagUpdateRequest](apptagupdaterequest.md)
  The request body you use to update an app tag update request.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/apptagsresponse)*