# RetentionMessageVersion

**Framework**: App Store Connect API  
**Kind**: dictionary  
**Role**: Object

A version of a retention message’s content that you submit to App Review.

**Availability**:
- App Store Connect API 4.6+

## Declaration

```
object RetentionMessageVersion
```

## Topics

### Objects
- [object RetentionMessageVersion.Attributes](./retentionmessageversion/attributes-data.dictionary.md)
  Attributes that describe a retention message version resource.
- [object RetentionMessageVersion.Relationships](./retentionmessageversion/relationships-data.dictionary.md)
  The relationships you include in the request and those on which you can operate.

## Properties

- `type` (string) *(required)*: The resource type.

  **Allowed Values**: `retentionMessageVersions`
- `id` (string) *(required)*: An opaque resource ID that uniquely identifies the resource.
- `attributes` (RetentionMessageVersion.Attributes): The resource’s attributes.
- `relationships` (RetentionMessageVersion.Relationships): Navigational links to related data and included resource types and IDs.
- `links` (ResourceLinks): Navigational links that include the self-link.

## See Also

### Objects and types
- [object RetentionMessageVersionCreateRequest](./retentionmessageversioncreaterequest.md)
  The request body you use to create a retention message version.
- [object RetentionMessageVersionResponse](./retentionmessageversionresponse.md)
  The response body for endpoints that create or read a single retention message version.
- [object RetentionMessageLocalizationsResponse](./retentionmessagelocalizationsresponse.md)
  The response body for endpoints that list retention message localizations.
- [object RetentionMessageVersionLocalizationsLinkagesResponse](./retentionmessageversionlocalizationslinkagesresponse.md)
  A response containing the resource identifiers of localizations for a retention message version.
- [object RetentionMessageVersionPlacementLinkageResponse](./retentionmessageversionplacementlinkageresponse.md)
  A response containing the resource identifier of the image placement for a retention message version.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/retentionmessageversion)*