# CiWorkflow.Relationships

**Framework**: App Store Connect API  
**Kind**: dictionary  
**Role**: Object

The relationships of the Workflows resource you included in the request and those on which you can operate.

**Availability**:
- App Store Connect API 1.5+

## Declaration

```
object CiWorkflow.Relationships
```

## Topics

### Objects
- [object CiWorkflow.Relationships.MacOsVersion](./relationships-data.dictionary/macosversion-data.dictionary.md)
  The data and links that describe the relationship between the Workflows and the macOS Versions resources.
- [object CiWorkflow.Relationships.Product](./relationships-data.dictionary/product-data.dictionary.md)
  The data and links that describe the relationship between the Workflows and the Products resources.
- [object CiWorkflow.Relationships.Repository](./relationships-data.dictionary/repository-data.dictionary.md)
  The data and links that describe the relationship between the Workflows and the Repositories resources.
- [object CiWorkflow.Relationships.XcodeVersion](./relationships-data.dictionary/xcodeversion-data.dictionary.md)
  The data and links that describe the relationship between the Workflows and the Xcode Versions resources.
### Dictionaries
- [object CiWorkflow.Relationships.BuildRuns](./relationships-data.dictionary/buildruns-data.dictionary.md)

## Properties

- `product` (CiWorkflow.Relationships.Product): The related Products resource.
- `repository` (CiWorkflow.Relationships.Repository): The workflow’s related Git repository.
- `xcodeVersion` (CiWorkflow.Relationships.XcodeVersion): The related Xcode Versions resource.
- `macOsVersion` (CiWorkflow.Relationships.MacOsVersion): The related macOS Versions resource.
- `buildRuns` (CiWorkflow.Relationships.BuildRuns)

## See Also

### Objects
- [object CiWorkflow.Attributes](./attributes-data.dictionary.md)
  The attributes that describe a Workflows resource.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/ciworkflow/relationships-data.dictionary)*