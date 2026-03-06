# CiBuildRunCreateRequest.Data

**Framework**: App Store Connect API  
**Kind**: dictionary

The data element of the request you use to start a new Xcode Cloud build.

**Availability**:
- App Store Connect API 1.5+

## Declaration

```swift
object CiBuildRunCreateRequest.Data
```

## Topics

### Objects
- [object CiBuildRunCreateRequest.Data.Attributes](cibuildruncreaterequest/data-data.dictionary/attributes-data.dictionary.md)
  The attributes you set that describe the new Build Runs resource.
- [object CiBuildRunCreateRequest.Data.Relationships](cibuildruncreaterequest/data-data.dictionary/relationships-data.dictionary.md)
  The relationships to other resources that you can set with this request.

## Properties

- `attributes` (CiBuildRunCreateRequest.Data.Attributes): The attributes that describe the request that creates a Build Runs resource.
- `relationships` (CiBuildRunCreateRequest.Data.Relationships): The types and IDs of the related data to update.
- `type` (string) *(required)*: The resource type.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/cibuildruncreaterequest/data-data.dictionary)*