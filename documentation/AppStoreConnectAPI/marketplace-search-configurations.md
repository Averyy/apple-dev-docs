# Marketplace Search Configurations

**Framework**: App Store Connect API

Add and read information for alternative marketplace search configurations.

#### Overview

Alternative marketplaces can use a sitemap that uses an industry-standard specification, with additional features specified by Apple. To learn more about the data structure for the sitemap, see [`Building a searchable catalog for your marketplace app for inclusion in Spotlight`](building-a-searchable-catalog-for-your-marketplace-app-for-inclusion-in-spotlight.md). To add the URL for this sitemap to [`Applebot`](https://developer.apple.comhttps://support.apple.com/en-us/HT204683) web crawler use the [`Add a marketplace search detail url`](post-v1-marketplacesearchdetails.md) endpoint.

## Topics

### Managing search URLs
- [Building a searchable catalog for your marketplace app for inclusion in Spotlight](building-a-searchable-catalog-for-your-marketplace-app-for-inclusion-in-spotlight.md)
  Set up and build your alternative marketplace’s searchable index.
- [Add a marketplace search detail url](post-v1-marketplacesearchdetails.md)
  Add a search detail URL for the alternative marketplace.
- [Read the marketplace search detail url](get-v1-apps-_id_-marketplacesearchdetail.md)
  Get search detail URL for the alternative marketplace.
- [Get the marketplace search detail ID for an app](get-v1-apps-_id_-relationships-marketplacesearchdetail.md)
- [Modify a marketplace search detail url](patch-v1-marketplacesearchdetails-_id_.md)
  Update the search detail URL for the alternative marketplace.
- [Delete a marketplace search detail url](delete-v1-marketplacesearchdetails-_id_.md)
  Delete search detail URL for the alternative marketplace.
### Objects
- [object MarketplaceSearchDetail](marketplacesearchdetail.md)
  The search configuration for an alternative marketplace, specifying how apps are indexed and surfaced in search.
- [object MarketplaceSearchDetailCreateRequest](marketplacesearchdetailcreaterequest.md)
  The request body you use to create an alternative marketplace search detail.
- [object MarketplaceSearchDetailResponse](marketplacesearchdetailresponse.md)
  A response containing the search configuration for a single alternative marketplace.
- [object MarketplaceSearchDetailUpdateRequest](marketplacesearchdetailupdaterequest.md)
  The request body you use to update an alternative marketplace search detail.
- [object AppMarketplaceSearchDetailLinkageResponse](appmarketplacesearchdetaillinkageresponse.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/marketplace-search-configurations)*