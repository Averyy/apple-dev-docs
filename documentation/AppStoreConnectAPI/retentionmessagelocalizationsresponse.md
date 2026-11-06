# RetentionMessageLocalizationsResponse

**Framework**: App Store Connect API  
**Kind**: dictionary  
**Role**: Object

The response body for endpoints that list retention message localizations.

**Availability**:
- App Store Connect API 4.6+

## Declaration

```
object RetentionMessageLocalizationsResponse
```

## Properties

- `data` ([RetentionMessageLocalization]) *(required)*: The resource data.
- `included` ([RetentionMessageVersion]): The requested relationship data.
- `links` (PagedDocumentLinks) *(required)*: Navigational links that include the self-link.
- `meta` (PagingInformation): Paging information.

## See Also

### Objects and types
- [object RetentionMessageVersion](./retentionmessageversion.md)
  A version of a retention message’s content that you submit to App Review.
- [object RetentionMessageVersionCreateRequest](./retentionmessageversioncreaterequest.md)
  The request body you use to create a retention message version.
- [object RetentionMessageVersionResponse](./retentionmessageversionresponse.md)
  The response body for endpoints that create or read a single retention message version.
- [object RetentionMessageVersionLocalizationsLinkagesResponse](./retentionmessageversionlocalizationslinkagesresponse.md)
  A response containing the resource identifiers of localizations for a retention message version.
- [object RetentionMessageVersionPlacementLinkageResponse](./retentionmessageversionplacementlinkageresponse.md)
  A response containing the resource identifier of the image placement for a retention message version.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/retentionmessagelocalizationsresponse)*