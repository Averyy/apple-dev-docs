# Territory

**Framework**: App Store Connect API  
**Kind**: dictionary

An App Store region (country or territory) where apps, subscriptions, and in-app purchases are offered.

**Availability**:
- App Store Connect API 1.2+

## Declaration

```swift
object Territory
```

## Topics

### Objects
- [object Territory.Attributes](territory/attributes-data.dictionary.md)
  Attributes that describe a Territories resource.

## Properties

- `attributes` (Territory.Attributes)
- `id` (string) *(required)*
- `links` (ResourceLinks)
- `type` (string) *(required)*

## See Also

- [object TerritoryResponse](territoryresponse.md)
  The response body for endpoints that read a single App Store territory.
- [object TerritoriesWithoutIncludesResponse](territorieswithoutincludesresponse.md)
  A response containing a list of App Store territories, without related resources.
- [object TerritoriesResponse](territoriesresponse.md)
  The response body for endpoints that list available App Store territories.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/territory)*