# AppInfoUpdateRequest.Data

**Framework**: App Store Connect API  
**Kind**: dictionary

The data element of the request body.

**Availability**:
- App Store Connect API 1.2+

## Declaration

```swift
object AppInfoUpdateRequest.Data
```

## Topics

### Objects
- [object AppInfoUpdateRequest.Data.Relationships](appinfoupdaterequest/data-data.dictionary/relationships-data.dictionary.md)
  The data and links that describe the relationship between the resources.

## Properties

- `id` (string) *(required)*: An opaque resource ID that uniquely identifies the resource.
- `relationships` (AppInfoUpdateRequest.Data.Relationships): Navigational links to related data and included resource types and IDs.
- `type` (string) *(required)*: The resource type.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/appinfoupdaterequest/data-data.dictionary)*