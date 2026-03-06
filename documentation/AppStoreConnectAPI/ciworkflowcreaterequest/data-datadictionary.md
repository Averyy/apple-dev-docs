# CiWorkflowCreateRequest.Data

**Framework**: App Store Connect API  
**Kind**: dictionary

The data element of the request you use to create a new Xcode Cloud workflow.

**Availability**:
- App Store Connect API 1.5+

## Declaration

```swift
object CiWorkflowCreateRequest.Data
```

## Topics

### Objects
- [object CiWorkflowCreateRequest.Data.Attributes](ciworkflowcreaterequest/data-data.dictionary/attributes-data.dictionary.md)
  The attributes you set that describe the new Xcode Cloud workflow resource.
- [object CiWorkflowCreateRequest.Data.Relationships](ciworkflowcreaterequest/data-data.dictionary/relationships-data.dictionary.md)
  The relationships to other resources that you can set with this request.

## Properties

- `attributes` (CiWorkflowCreateRequest.Data.Attributes) *(required)*: The attributes that describe the request that creates a Workflows resource.
- `relationships` (CiWorkflowCreateRequest.Data.Relationships) *(required)*: The types and IDs of the related data to update.
- `type` (string) *(required)*: The resource type.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/ciworkflowcreaterequest/data-data.dictionary)*