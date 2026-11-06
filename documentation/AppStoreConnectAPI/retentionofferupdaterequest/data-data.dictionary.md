# RetentionOfferUpdateRequest.Data

**Framework**: App Store Connect API  
**Kind**: dictionary  
**Role**: Object

The data element of the request body.

**Availability**:
- App Store Connect API 4.6+

## Declaration

```
object RetentionOfferUpdateRequest.Data
```

## Topics

### Objects
- [object RetentionOfferUpdateRequest.Data.Attributes](./data-data.dictionary/attributes-data.dictionary.md)
  Attributes whose values you’re changing as part of the update request.

## Properties

- `type` (string) *(required)*: The resource type.

  **Allowed Values**: `retentionOffers`
- `id` (string) *(required)*: An opaque resource ID that uniquely identifies the resource.
- `attributes` (RetentionOfferUpdateRequest.Data.Attributes): The resource’s attributes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/retentionofferupdaterequest/data-data.dictionary)*