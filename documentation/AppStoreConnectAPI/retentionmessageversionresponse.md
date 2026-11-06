# RetentionMessageVersionResponse

**Framework**: App Store Connect API  
**Kind**: dictionary  
**Role**: Object

The response body for endpoints that create or read a single retention message version.

**Availability**:
- App Store Connect API 4.6+

## Declaration

```
object RetentionMessageVersionResponse
```

## Properties

- `data` (RetentionMessageVersion) *(required)*: The resource data.
- `included` ([*]): The requested relationship data.

  **Allowed Types**: `AppAssetLibraryPlacement`, `RetentionMessageLocalization`, `RetentionMessage`
- `links` (DocumentLinks) *(required)*: Navigational links that include the self-link.

## See Also

### Objects and types
- [object RetentionMessageVersion](./retentionmessageversion.md)
  A version of a retention message’s content that you submit to App Review.
- [object RetentionMessageVersionCreateRequest](./retentionmessageversioncreaterequest.md)
  The request body you use to create a retention message version.
- [object RetentionMessageLocalizationsResponse](./retentionmessagelocalizationsresponse.md)
  The response body for endpoints that list retention message localizations.
- [object RetentionMessageVersionLocalizationsLinkagesResponse](./retentionmessageversionlocalizationslinkagesresponse.md)
  A response containing the resource identifiers of localizations for a retention message version.
- [object RetentionMessageVersionPlacementLinkageResponse](./retentionmessageversionplacementlinkageresponse.md)
  A response containing the resource identifier of the image placement for a retention message version.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/retentionmessageversionresponse)*