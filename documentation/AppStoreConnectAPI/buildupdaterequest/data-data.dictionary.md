# BuildUpdateRequest.Data

**Framework**: App Store Connect API  
**Kind**: dictionary

The data element of the request body.

**Availability**:
- App Store Connect API 1.0+

## Declaration

```swift
object BuildUpdateRequest.Data
```

## Topics

### Objects
- [object BuildUpdateRequest.Data.Attributes](buildupdaterequest/data-data.dictionary/attributes-data.dictionary.md)
  Attributes whose values you’re changing as part of the update request.
- [object BuildUpdateRequest.Data.Relationships](buildupdaterequest/data-data.dictionary/relationships-data.dictionary.md)
  The data and links that describe the relationship between the resources.

## Properties

- `attributes` (BuildUpdateRequest.Data.Attributes): The resource’s attributes.
- `id` (string) *(required)*: The opaque resource ID that uniquely identifies the resource.
- `relationships` (BuildUpdateRequest.Data.Relationships): Navigational links to related data and included resource types and IDs.
- `type` (string) *(required)*: The resource type.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/buildupdaterequest/data-data.dictionary)*