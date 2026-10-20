# CiProduct.Relationships.App

**Framework**: App Store Connect API  
**Kind**: dictionary  
**Role**: Object

The data and links that describe the relationship between the Products and Apps resources.

**Availability**:
- App Store Connect API 1.5+

## Declaration

```
object CiProduct.Relationships.App
```

## Topics

### Objects
- [object CiProduct.Relationships.App.Data](./app-data.dictionary/data-data.dictionary.md)
  The type and ID of a related Apps resource.

## Properties

- `data` (CiProduct.Relationships.App.Data): The ID and type of the related Apps resource.
- `links` (RelationshipLinks): The navigational links that include the self-link.

## See Also

### Objects
- [object CiProduct.Relationships.BundleId](./bundleid-data.dictionary.md)
  The data and links that describe the relationship between the Products and the Bundle IDs resources.
- [object CiProduct.Relationships.PrimaryRepositories](./primaryrepositories-data.dictionary.md)
  The data, links, and paging information that describe the relationship between the Products resource and the Repositories resource that represents the primary repository.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/ciproduct/relationships-data.dictionary/app-data.dictionary)*