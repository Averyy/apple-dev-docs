# Alternative Distribution Domains

**Framework**: App Store Connect API

Create and read alternative distribution domains.

#### Overview

You use the endpoints and objects in this API collection to add your alternative distribution app’s base domain to App Store Connect. For more information on adding a domain for your alternative distribution app, see [`Add an alternative distribution domain`](post-v1-alternativedistributiondomains.md).

All the individual pages for apps that your alternative marketplace app distributes need to be on this base domain and it also needs to house your sitemap to support marketplace search. For more information about your alternative marketplace’s sitemap, see [`Building a searchable catalog for your marketplace app for inclusion in Spotlight`](building-a-searchable-catalog-for-your-marketplace-app-for-inclusion-in-spotlight.md).

Your web distribution app needs to be served from this base domain.

## Topics

### Managing domains
- [Add an alternative distribution domain](post-v1-alternativedistributiondomains.md)
  Add an alternative distribution domain to your account.
- [Read alternative distribution domain information](get-v1-alternativedistributiondomains-_id_.md)
  Read information for a specific alternative distribution domain.
- [List alternative distribution domains](get-v1-alternativedistributiondomains.md)
  List all the alternative distribution domains for your account.
- [Delete an alternative distribution domain](delete-v1-alternativedistributiondomains-_id_.md)
  Delete the alternative distribution search domain for an app.
- [Add a marketplace domain](post-v1-marketplacedomains.md)
  Add an alternative marketplace domain to your account.
- [Read marketplace domain information](get-v1-marketplacedomains-_id_.md)
  Read information for a specific alternative marketplace domain.
- [List marketplace domains](get-v1-marketplacedomains.md)
  List all the alternative marketplace domains for your account.
- [Delete a marketplace domain](delete-v1-marketplacedomains-_id_.md)
  Delete the alternative marketplace search domain for an app.
### Objects
- [object AlternativeDistributionDomain](alternativedistributiondomain.md)
  The data structure that represents an alternative distribution domain resource.
- [object AlternativeDistributionDomainCreateRequest](alternativedistributiondomaincreaterequest.md)
  The request body you use to create an alternative distribution domain.
- [object AlternativeDistributionDomainResponse](alternativedistributiondomainresponse.md)
  A response that contains a single alternative distribution domain resource.
- [object AlternativeDistributionDomainsResponse](alternativedistributiondomainsresponse.md)
  A response that contains a list of alternative distribution domain resources.
- [object MarketplaceDomain](marketplacedomain.md)
  The data structure that represents an alternative marketplace domain resource.
- [object MarketplaceDomainCreateRequest](marketplacedomaincreaterequest.md)
  The request body you use to create an alternative marketplace domain.
- [object MarketplaceDomainResponse](marketplacedomainresponse.md)
  A response that contains a single alternative marketplace domain resource.
- [object MarketplaceDomainsResponse](marketplacedomainsresponse.md)
  A response that contains a list of alternative marketplace domain resources.

## See Also

- [Alternative Distribution Keys](alternative-distribution-keys.md)
  Create and manage keys for an alternative app distribution.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/alternative-distribution-domains)*