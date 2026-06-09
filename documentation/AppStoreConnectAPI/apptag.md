# AppTag

**Framework**: App Store Connect API  
**Kind**: dictionary

A label used to categorize an app for internal organization or to control which App Store territories feature it.

**Availability**:
- App Store Connect API 4.1+

## Declaration

```swift
object AppTag
```

## Topics

### Dictionaries
- [object AppTag.Attributes](apptag/attributes-data.dictionary.md)
  Attributes that describe an app tag resource.
- [object AppTag.Relationships](apptag/relationships-data.dictionary.md)
  The relationships you include in the request and those on which you can operate.

## Properties

- `attributes` (AppTag.Attributes)
- `id` (string) *(required)*
- `links` (ResourceLinks)
- `relationships` (AppTag.Relationships)
- `type` (string) *(required)*

## See Also

- [object AppAppTagsLinkagesResponse](appapptagslinkagesresponse.md)
  A response containing the resource identifiers of tags associated with an app.
- [object AppTagResponse](apptagresponse.md)
  A response containing a single app tag.
- [object AppTagsResponse](apptagsresponse.md)
  A response containing a list of tags associated with apps.
- [object AppTagTerritoriesLinkagesResponse](apptagterritorieslinkagesresponse.md)
  A response containing the resource identifiers of territories associated with an app tag.
- [object AppTagUpdateRequest](apptagupdaterequest.md)
  The request body you use to update an app tag update request.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/apptag)*