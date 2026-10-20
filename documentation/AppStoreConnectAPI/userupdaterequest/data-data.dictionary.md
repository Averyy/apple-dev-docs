# UserUpdateRequest.Data

**Framework**: App Store Connect API  
**Kind**: dictionary

The data element of the request body.

**Availability**:
- App Store Connect API 1.0+

## Declaration

```swift
object UserUpdateRequest.Data
```

## Topics

### Objects
- [object UserUpdateRequest.Data.Attributes](userupdaterequest/data-data.dictionary/attributes-data.dictionary.md)
  Attributes whose values you’re changing as part of the update request.
- [object UserUpdateRequest.Data.Relationships](userupdaterequest/data-data.dictionary/relationships-data.dictionary.md)
  The data and links that describe the relationship between the resources.

## Properties

- `attributes` (UserUpdateRequest.Data.Attributes): The resource’s attributes.
- `id` (string) *(required)*: The opaque resource ID that uniquely identifies the resource.
- `relationships` (UserUpdateRequest.Data.Relationships): The types and IDs of the related data to update.
- `type` (string) *(required)*: The resource type.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/userupdaterequest/data-data.dictionary)*