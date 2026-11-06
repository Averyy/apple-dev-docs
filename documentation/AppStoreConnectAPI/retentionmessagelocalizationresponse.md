# RetentionMessageLocalizationResponse

**Framework**: App Store Connect API  
**Kind**: dictionary  
**Role**: Object

The response body for endpoints that create, read, or modify a single retention message localization.

**Availability**:
- App Store Connect API 4.6+

## Declaration

```
object RetentionMessageLocalizationResponse
```

## Properties

- `data` (RetentionMessageLocalization) *(required)*: The resource data.
- `included` ([RetentionMessageVersion]): The requested relationship data.
- `links` (DocumentLinks) *(required)*: Navigational links that include the self-link.

## See Also

### Objects and types
- [object RetentionMessageLocalization](./retentionmessagelocalization.md)
  The header and body text of a retention message version for a single locale.
- [object RetentionMessageLocalizationCreateRequest](./retentionmessagelocalizationcreaterequest.md)
  The request body you use to create a retention message localization.
- [object RetentionMessageLocalizationUpdateRequest](./retentionmessagelocalizationupdaterequest.md)
  The request body you use to update a retention message localization.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/retentionmessagelocalizationresponse)*