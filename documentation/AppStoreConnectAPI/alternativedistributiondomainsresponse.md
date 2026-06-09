# AlternativeDistributionDomainsResponse

**Framework**: App Store Connect API  
**Kind**: dictionary

The response body for endpoints that list alternative distribution domains.

**Availability**:
- App Store Connect API 3.4.1+

## Declaration

```swift
object AlternativeDistributionDomainsResponse
```

## Properties

- `data` ([AlternativeDistributionDomain]) *(required)*
- `links` (PagedDocumentLinks) *(required)*
- `meta` (PagingInformation)

## See Also

- [object AlternativeDistributionDomain](alternativedistributiondomain.md)
  A web domain authorized to distribute your app outside the App Store via web distribution or an alternative marketplace.
- [object AlternativeDistributionDomainCreateRequest](alternativedistributiondomaincreaterequest.md)
  The request body you use to create an alternative distribution domain.
- [object AlternativeDistributionDomainResponse](alternativedistributiondomainresponse.md)
  The response body for endpoints that create or read a single alternative distribution domain.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/alternativedistributiondomainsresponse)*