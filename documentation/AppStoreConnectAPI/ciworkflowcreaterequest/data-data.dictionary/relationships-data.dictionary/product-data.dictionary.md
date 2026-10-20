# CiWorkflowCreateRequest.Data.Relationships.Product

**Framework**: App Store Connect API  
**Kind**: dictionary  
**Role**: Object

The relationship to the Products resource you set with the request that creates a Workflows resource.

**Availability**:
- App Store Connect API 1.5+

## Declaration

```
object CiWorkflowCreateRequest.Data.Relationships.Product
```

## Topics

### Objects
- [object CiWorkflowCreateRequest.Data.Relationships.Product.Data](./product-data.dictionary/data-data.dictionary.md)
  The type and ID of the Products resource that you’re relating with the Workflows resource you’re creating.

## Properties

- `data` (CiWorkflowCreateRequest.Data.Relationships.Product.Data) *(required)*: The ID and type of the related Products resource.

## See Also

### Objects
- [object CiWorkflowCreateRequest.Data.Relationships.MacOsVersion](./macosversion-data.dictionary.md)
  The relationship to the macOS Versions resource you set with the request that creates a Workflows resource.
- [object CiWorkflowCreateRequest.Data.Relationships.Repository](./repository-data.dictionary.md)
  The relationship to the Repositories Versions resource you set with the request that creates a Workflows resource.
- [object CiWorkflowCreateRequest.Data.Relationships.XcodeVersion](./xcodeversion-data.dictionary.md)
  The relationship to the Xcode Versions resource you set with the request that creates a Workflows resource.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/ciworkflowcreaterequest/data-data.dictionary/relationships-data.dictionary/product-data.dictionary)*