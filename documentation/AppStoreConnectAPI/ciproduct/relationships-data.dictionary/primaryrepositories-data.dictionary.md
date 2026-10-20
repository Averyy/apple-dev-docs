# CiProduct.Relationships.PrimaryRepositories

**Framework**: App Store Connect API  
**Kind**: dictionary  
**Role**: Object

The data, links, and paging information that describe the relationship between the Products resource and the Repositories resource that represents the primary repository.

**Availability**:
- App Store Connect API 1.5+

## Declaration

```
object CiProduct.Relationships.PrimaryRepositories
```

## Topics

### Objects
- [object CiProduct.Relationships.PrimaryRepositories.Data](./primaryrepositories-data.dictionary/data-data.dictionary.md)
  The type and ID of a related Repositories resource that represents the product’s primary repositories.

## Properties

- `data` ([CiProduct.Relationships.PrimaryRepositories.Data]): The ID and type of the related Repositories resource that represents the primary repository.
- `links` (RelationshipLinks): The navigational links that include the self-link.
- `meta` (PagingInformation): The paging information.

## See Also

### Objects
- [object CiProduct.Relationships.App](./app-data.dictionary.md)
  The data and links that describe the relationship between the Products and Apps resources.
- [object CiProduct.Relationships.BundleId](./bundleid-data.dictionary.md)
  The data and links that describe the relationship between the Products and the Bundle IDs resources.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/ciproduct/relationships-data.dictionary/primaryrepositories-data.dictionary)*