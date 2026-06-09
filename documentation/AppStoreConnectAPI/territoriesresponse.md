# TerritoriesResponse

**Framework**: App Store Connect API  
**Kind**: dictionary

The response body for endpoints that list available App Store territories.

**Availability**:
- App Store Connect API 1.2+

## Declaration

```swift
object TerritoriesResponse
```

## Properties

- `data` ([Territory]) *(required)*
- `links` (PagedDocumentLinks) *(required)*
- `meta` (PagingInformation)

## See Also

- [object Territory](territory.md)
  An App Store region (country or territory) where apps, subscriptions, and in-app purchases are offered.
- [object TerritoryResponse](territoryresponse.md)
  The response body for endpoints that read a single App Store territory.
- [object TerritoriesWithoutIncludesResponse](territorieswithoutincludesresponse.md)
  A response containing a list of App Store territories, without related resources.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/territoriesresponse)*