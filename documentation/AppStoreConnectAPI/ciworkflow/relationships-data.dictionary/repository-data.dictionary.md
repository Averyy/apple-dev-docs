# CiWorkflow.Relationships.Repository

**Framework**: App Store Connect API  
**Kind**: dictionary  
**Role**: Object

The data and links that describe the relationship between the Workflows and the Repositories resources.

**Availability**:
- App Store Connect API 1.5+

## Declaration

```
object CiWorkflow.Relationships.Repository
```

## Topics

### Objects
- [object CiWorkflow.Relationships.Repository.Data](./repository-data.dictionary/data-data.dictionary.md)
  The type and ID of a related Repositories resource.

## Properties

- `data` (CiWorkflow.Relationships.Repository.Data): The ID and type of the related Repositories resource.
- `links` (RelationshipLinks): The navigational links that include the self-link.

## See Also

### Objects
- [object CiWorkflow.Relationships.MacOsVersion](./macosversion-data.dictionary.md)
  The data and links that describe the relationship between the Workflows and the macOS Versions resources.
- [object CiWorkflow.Relationships.Product](./product-data.dictionary.md)
  The data and links that describe the relationship between the Workflows and the Products resources.
- [object CiWorkflow.Relationships.XcodeVersion](./xcodeversion-data.dictionary.md)
  The data and links that describe the relationship between the Workflows and the Xcode Versions resources.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/ciworkflow/relationships-data.dictionary/repository-data.dictionary)*