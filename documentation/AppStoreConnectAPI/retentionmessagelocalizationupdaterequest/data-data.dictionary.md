# RetentionMessageLocalizationUpdateRequest.Data

**Framework**: App Store Connect API  
**Kind**: dictionary  
**Role**: Object

The data element of the request body.

**Availability**:
- App Store Connect API 4.6+

## Declaration

```
object RetentionMessageLocalizationUpdateRequest.Data
```

## Topics

### Objects
- [object RetentionMessageLocalizationUpdateRequest.Data.Attributes](./data-data.dictionary/attributes-data.dictionary.md)
  Attributes whose values you’re changing as part of the update request.

## Properties

- `type` (string) *(required)*: The resource type.

  **Allowed Values**: `retentionMessageLocalizations`
- `id` (string) *(required)*: An opaque resource ID that uniquely identifies the resource.
- `attributes` (RetentionMessageLocalizationUpdateRequest.Data.Attributes): The resource’s attributes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/retentionmessagelocalizationupdaterequest/data-data.dictionary)*