# BetaLicenseAgreementUpdateRequest.Data

**Framework**: App Store Connect API  
**Kind**: dictionary  
**Role**: Object

The data element of the request body.

**Availability**:
- App Store Connect API 1.0+

## Declaration

```
object BetaLicenseAgreementUpdateRequest.Data
```

## Topics

### Objects
- [object BetaLicenseAgreementUpdateRequest.Data.Attributes](./data-data.dictionary/attributes-data.dictionary.md)
  Attributes whose values you’re changing as part of the update request.

## Properties

- `attributes` (BetaLicenseAgreementUpdateRequest.Data.Attributes): The resource’s attributes.
- `id` (string) *(required)*: The opaque resource ID that uniquely identifies the resource.
- `type` (string) *(required)*: The resource type.

  **Allowed Values**: `betaLicenseAgreements`


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/betalicenseagreementupdaterequest/data-data.dictionary)*