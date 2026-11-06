# RetentionMessageLocalization

**Framework**: App Store Connect API  
**Kind**: dictionary  
**Role**: Object

The header and body text of a retention message version for a single locale.

**Availability**:
- App Store Connect API 4.6+

## Declaration

```
object RetentionMessageLocalization
```

## Topics

### Objects
- [object RetentionMessageLocalization.Attributes](./retentionmessagelocalization/attributes-data.dictionary.md)
  Attributes that describe a retention message localization resource.
- [object RetentionMessageLocalization.Relationships](./retentionmessagelocalization/relationships-data.dictionary.md)
  The relationships you include in the request and those on which you can operate.

## Properties

- `type` (string) *(required)*: The resource type.

  **Allowed Values**: `retentionMessageLocalizations`
- `id` (string) *(required)*: An opaque resource ID that uniquely identifies the resource.
- `attributes` (RetentionMessageLocalization.Attributes): The resource’s attributes.
- `relationships` (RetentionMessageLocalization.Relationships): Navigational links to related data and included resource types and IDs.
- `links` (ResourceLinks): Navigational links that include the self-link.

## See Also

### Objects and types
- [object RetentionMessageLocalizationCreateRequest](./retentionmessagelocalizationcreaterequest.md)
  The request body you use to create a retention message localization.
- [object RetentionMessageLocalizationUpdateRequest](./retentionmessagelocalizationupdaterequest.md)
  The request body you use to update a retention message localization.
- [object RetentionMessageLocalizationResponse](./retentionmessagelocalizationresponse.md)
  The response body for endpoints that create, read, or modify a single retention message localization.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/retentionmessagelocalization)*