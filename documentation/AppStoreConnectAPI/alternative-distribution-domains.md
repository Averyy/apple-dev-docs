# Alternative Distribution Domains

**Framework**: App Store Connect API

Create and read alternative distribution domains.

#### Overview

You use the endpoints and objects in this API collection to add your alternative distribution app’s base domain to App Store Connect. For more information on adding a domain for your alternative distribution app, see [`Add an Alternative Distribution Domain`](post-v1-alternativedistributiondomains.md).

All the individual pages for apps that your alternative marketplace app distributes need to be on this base domain and it also needs to house your sitemap to support marketplace search. For more information about your alternative marketplace’s sitemap, see [`Building a searchable catalog for your marketplace app for inclusion in Spotlight`](building-a-searchable-catalog-for-your-marketplace-app-for-inclusion-in-spotlight.md).

Your web distribution app needs to be served from this base domain.

## Topics

### Managing domains
- [Add an Alternative Distribution Domain](post-v1-alternativedistributiondomains.md)
  Add an alternative distribution domain to your account.
- [Read Alternative Distribution Domain Information](get-v1-alternativedistributiondomains-_id_.md)
  Read information for a specific alternative distribution domain.
- [List Alternative Distribution Domains](get-v1-alternativedistributiondomains.md)
  List all the alternative distribution domains for your account.
- [Delete an Alternative Distribution Domain](delete-v1-alternativedistributiondomains-_id_.md)
  Delete the alternative distribution search domain for an app.
### Objects
- [object AlternativeDistributionDomain](alternativedistributiondomain.md)
  A web domain authorized to distribute your app outside the App Store via web distribution or an alternative marketplace.
- [object AlternativeDistributionDomainCreateRequest](alternativedistributiondomaincreaterequest.md)
  The request body you use to create an alternative distribution domain.
- [object AlternativeDistributionDomainResponse](alternativedistributiondomainresponse.md)
  The response body for endpoints that create or read a single alternative distribution domain.
- [object AlternativeDistributionDomainsResponse](alternativedistributiondomainsresponse.md)
  The response body for endpoints that list alternative distribution domains.

## See Also

- [Alternative Distribution Keys](alternative-distribution-keys.md)
  Create and manage keys for an alternative app distribution.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/alternative-distribution-domains)*