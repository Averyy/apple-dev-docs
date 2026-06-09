# AppPreviewSet

**Framework**: App Store Connect API  
**Kind**: dictionary

The data structure that represent an App Preview Sets resource.

**Availability**:
- App Store Connect API 1.2+

## Declaration

```swift
object AppPreviewSet
```

## Topics

### Objects
- [object AppPreviewSet.Attributes](apppreviewset/attributes-data.dictionary.md)
  Attributes that describe an App Preview Sets resource.
- [object AppPreviewSet.Relationships](apppreviewset/relationships-data.dictionary.md)
  The relationships you include in the request and those on which you can operate.

## Properties

- `attributes` (AppPreviewSet.Attributes)
- `id` (string) *(required)*
- `links` (ResourceLinks)
- `relationships` (AppPreviewSet.Relationships)
- `type` (string) *(required)*

## See Also

- [object AppPreviewSetCreateRequest](apppreviewsetcreaterequest.md)
  The request body you use to create an App Preview Set.
- [object AppPreviewSetResponse](apppreviewsetresponse.md)
  The response body for endpoints that create or read a set of app preview videos for a display size.
- [object AppPreviewSetsResponse](apppreviewsetsresponse.md)
  The response body for endpoints that list app preview sets for an App Store version localization.
- [object AppPreviewSetAppPreviewsLinkagesRequest](apppreviewsetapppreviewslinkagesrequest.md)
  A request body you use to reorder the app previews in a preview set.
- [object AppPreviewSetAppPreviewsLinkagesResponse](apppreviewsetapppreviewslinkagesresponse.md)
  A response body that contains a list of related resource IDs.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/apppreviewset)*