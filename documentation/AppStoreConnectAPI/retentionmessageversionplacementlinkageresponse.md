# RetentionMessageVersionPlacementLinkageResponse

**Framework**: App Store Connect API  
**Kind**: dictionary  
**Role**: Object

A response containing the resource identifier of the image placement for a retention message version.

**Availability**:
- App Store Connect API 4.6+

## Declaration

```
object RetentionMessageVersionPlacementLinkageResponse
```

## Topics

### Objects
- [object RetentionMessageVersionPlacementLinkageResponse.Data](./retentionmessageversionplacementlinkageresponse/data-data.dictionary.md)
  The type and ID of a related resource.

## Properties

- `data` (RetentionMessageVersionPlacementLinkageResponse.Data) *(required)*: The object type and ID of the related resource.
- `links` (DocumentLinks) *(required)*: Navigational links that include the self-link.

## See Also

### Objects and types
- [object RetentionMessageVersion](./retentionmessageversion.md)
  A version of a retention message’s content that you submit to App Review.
- [object RetentionMessageVersionCreateRequest](./retentionmessageversioncreaterequest.md)
  The request body you use to create a retention message version.
- [object RetentionMessageVersionResponse](./retentionmessageversionresponse.md)
  The response body for endpoints that create or read a single retention message version.
- [object RetentionMessageLocalizationsResponse](./retentionmessagelocalizationsresponse.md)
  The response body for endpoints that list retention message localizations.
- [object RetentionMessageVersionLocalizationsLinkagesResponse](./retentionmessageversionlocalizationslinkagesresponse.md)
  A response containing the resource identifiers of localizations for a retention message version.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/retentionmessageversionplacementlinkageresponse)*