# AppTagTerritoriesLinkagesResponse

**Framework**: App Store Connect API  
**Kind**: dictionary

A response containing the resource identifiers of territories associated with an app tag.

**Availability**:
- App Store Connect API 4.1+

## Declaration

```swift
object AppTagTerritoriesLinkagesResponse
```

## Topics

### Dictionaries
- [object AppTagTerritoriesLinkagesResponse.Data](apptagterritorieslinkagesresponse/data-data.dictionary.md)
  The resource linkage data identifying a territory associated with an app tag.

## Properties

- `data` ([AppTagTerritoriesLinkagesResponse.Data]) *(required)*
- `links` (PagedDocumentLinks) *(required)*
- `meta` (PagingInformation)

## See Also

- [object AppAppTagsLinkagesResponse](appapptagslinkagesresponse.md)
  A response containing the resource identifiers of tags associated with an app.
- [object AppTag](apptag.md)
  A label used to categorize an app for internal organization or to control which App Store territories feature it.
- [object AppTagResponse](apptagresponse.md)
  A response containing a single app tag.
- [object AppTagsResponse](apptagsresponse.md)
  A response containing a list of tags associated with apps.
- [object AppTagUpdateRequest](apptagupdaterequest.md)
  The request body you use to update an app tag update request.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/apptagterritorieslinkagesresponse)*