# MarketplaceSearchDetail

**Framework**: App Store Connect API  
**Kind**: dictionary

The search configuration for an alternative marketplace, specifying how apps are indexed and surfaced in search.

**Availability**:
- App Store Connect API 3.3+

## Declaration

```swift
object MarketplaceSearchDetail
```

## Topics

### Objects
- [object MarketplaceSearchDetail.Attributes](marketplacesearchdetail/attributes-data.dictionary.md)
  Attributes that describe a marketplace search detail resource.

## Properties

- `attributes` (MarketplaceSearchDetail.Attributes)
- `id` (string) *(required)*
- `links` (ResourceLinks)
- `type` (string) *(required)*

## See Also

- [object MarketplaceSearchDetailCreateRequest](marketplacesearchdetailcreaterequest.md)
  The request body you use to create an alternative marketplace search detail.
- [object MarketplaceSearchDetailResponse](marketplacesearchdetailresponse.md)
  A response containing the search configuration for a single alternative marketplace.
- [object MarketplaceSearchDetailUpdateRequest](marketplacesearchdetailupdaterequest.md)
  The request body you use to update an alternative marketplace search detail.
- [object AppMarketplaceSearchDetailLinkageResponse](appmarketplacesearchdetaillinkageresponse.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/marketplacesearchdetail)*