# inAppOwnershipType

**Framework**: App Store Server API  
**Kind**: typealias  
**Role**: Type

A string that describes whether the transaction was purchased by the customer, or is available to them through Family Sharing, an organization, or a group.

**Availability**:
- App Store Server API 1.0+

## Declaration

```
string inAppOwnershipType
```

## Possible Values

- `FAMILY_SHARED`: The transaction belongs to a family member who benefits from service.
- `PURCHASED`: The transaction belongs to the purchaser.
- `ASSIGNED`: The transaction belongs to a customer who has access through an organization or group.

## Mentions

- [App Store Server API changelog](./app-store-server-api-changelog.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreserverapi/inappownershiptype)*