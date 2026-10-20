# CiProduct.Relationships

**Framework**: App Store Connect API  
**Kind**: dictionary  
**Role**: Object

The relationships of the Products resource you included in the request and those on which you can operate.

**Availability**:
- App Store Connect API 1.5+

## Declaration

```
object CiProduct.Relationships
```

## Topics

### Objects
- [object CiProduct.Relationships.App](./relationships-data.dictionary/app-data.dictionary.md)
  The data and links that describe the relationship between the Products and Apps resources.
- [object CiProduct.Relationships.BundleId](./relationships-data.dictionary/bundleid-data.dictionary.md)
  The data and links that describe the relationship between the Products and the Bundle IDs resources.
- [object CiProduct.Relationships.PrimaryRepositories](./relationships-data.dictionary/primaryrepositories-data.dictionary.md)
  The data, links, and paging information that describe the relationship between the Products resource and the Repositories resource that represents the primary repository.
### Dictionaries
- [object CiProduct.Relationships.AdditionalRepositories](./relationships-data.dictionary/additionalrepositories-data.dictionary.md)
- [object CiProduct.Relationships.BuildRuns](./relationships-data.dictionary/buildruns-data.dictionary.md)
- [object CiProduct.Relationships.Workflows](./relationships-data.dictionary/workflows-data.dictionary.md)

## Properties

- `app` (CiProduct.Relationships.App): The related Apps resource.
- `primaryRepositories` (CiProduct.Relationships.PrimaryRepositories): The related primary repository.
- `bundleId` (CiProduct.Relationships.BundleId): The related bundle ID.
- `additionalRepositories` (CiProduct.Relationships.AdditionalRepositories)
- `buildRuns` (CiProduct.Relationships.BuildRuns)
- `workflows` (CiProduct.Relationships.Workflows)

## See Also

### Objects
- [object CiProduct.Attributes](./attributes-data.dictionary.md)
  The attributes that describe a Products resource.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/ciproduct/relationships-data.dictionary)*