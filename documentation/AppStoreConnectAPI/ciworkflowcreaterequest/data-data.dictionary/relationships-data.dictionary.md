# CiWorkflowCreateRequest.Data.Relationships

**Framework**: App Store Connect API  
**Kind**: dictionary  
**Role**: Object

The relationships to other resources that you can set with this request.

**Availability**:
- App Store Connect API 1.5+

## Declaration

```
object CiWorkflowCreateRequest.Data.Relationships
```

## Topics

### Objects
- [object CiWorkflowCreateRequest.Data.Relationships.MacOsVersion](./relationships-data.dictionary/macosversion-data.dictionary.md)
  The relationship to the macOS Versions resource you set with the request that creates a Workflows resource.
- [object CiWorkflowCreateRequest.Data.Relationships.Product](./relationships-data.dictionary/product-data.dictionary.md)
  The relationship to the Products resource you set with the request that creates a Workflows resource.
- [object CiWorkflowCreateRequest.Data.Relationships.Repository](./relationships-data.dictionary/repository-data.dictionary.md)
  The relationship to the Repositories Versions resource you set with the request that creates a Workflows resource.
- [object CiWorkflowCreateRequest.Data.Relationships.XcodeVersion](./relationships-data.dictionary/xcodeversion-data.dictionary.md)
  The relationship to the Xcode Versions resource you set with the request that creates a Workflows resource.

## Properties

- `product` (CiWorkflowCreateRequest.Data.Relationships.Product) *(required)*: The related Products resource.
- `repository` (CiWorkflowCreateRequest.Data.Relationships.Repository) *(required)*: The related Repositories resource.
- `xcodeVersion` (CiWorkflowCreateRequest.Data.Relationships.XcodeVersion) *(required)*: The related Xcode Versions resource.
- `macOsVersion` (CiWorkflowCreateRequest.Data.Relationships.MacOsVersion) *(required)*: The related macOS Versions resource.

## See Also

### Objects
- [object CiWorkflowCreateRequest.Data.Attributes](./attributes-data.dictionary.md)
  The attributes you set that describe the new Xcode Cloud workflow resource.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/ciworkflowcreaterequest/data-data.dictionary/relationships-data.dictionary)*