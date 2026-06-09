# PromotedPurchasesResponse

**Framework**: App Store Connect API  
**Kind**: dictionary

The response body for endpoints that list promoted in-app purchases and subscriptions for an app.

**Availability**:
- App Store Connect API 2.0+

## Declaration

```swift
object PromotedPurchasesResponse
```

## Properties

- `data` ([PromotedPurchase]) *(required)*
- `included` ([*])
- `links` (PagedDocumentLinks) *(required)*
- `meta` (PagingInformation)

## See Also

- [object PromotedPurchaseResponse](promotedpurchaseresponse.md)
  The response body for endpoints that read or modify a promoted in-app purchase or subscription.
- [object PromotedPurchaseCreateRequest](promotedpurchasecreaterequest.md)
  The request body you use to create a promoted purchase.
- [object PromotedPurchaseUpdateRequest](promotedpurchaseupdaterequest.md)
  The request body you use to update a promoted purchase update request.
- [object AppPromotedPurchasesLinkagesRequest](apppromotedpurchaseslinkagesrequest.md)
  The request body for updating the ordered list of in-app purchases and subscriptions promoted on an app’s product page.
- [object AppPromotedPurchasesLinkagesResponse](apppromotedpurchaseslinkagesresponse.md)
  A response containing the resource identifiers of in-app purchases and subscriptions promoted on an app’s product page.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/promotedpurchasesresponse)*