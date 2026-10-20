# TerritoriesWithoutIncludesResponse

**Framework**: App Store Connect API  
**Kind**: dictionary  
**Role**: Object

A response containing a list of App Store territories, without related resources.

**Availability**:
- App Store Connect API 3.0+

## Declaration

```
object TerritoriesWithoutIncludesResponse
```

## Properties

- `data` ([Territory]) *(required)*
- `links` (PagedDocumentLinks) *(required)*
- `meta` (PagingInformation)

## See Also

### Objects
- [object Territory](./territory.md)
  An App Store region (country or territory) where apps, subscriptions, and In-App Purchases are offered.
- [object TerritoryResponse](./territoryresponse.md)
  The response body for endpoints that read a single App Store territory.
- [object TerritoriesResponse](./territoriesresponse.md)
  The response body for endpoints that list available App Store territories.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/territorieswithoutincludesresponse)*