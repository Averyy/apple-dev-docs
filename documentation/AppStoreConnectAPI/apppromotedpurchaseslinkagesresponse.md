# AppPromotedPurchasesLinkagesResponse

**Framework**: App Store Connect API  
**Kind**: dictionary

A response containing the resource identifiers of in-app purchases and subscriptions promoted on an app’s product page.

**Availability**:
- App Store Connect API 2.0+

## Declaration

```swift
object AppPromotedPurchasesLinkagesResponse
```

## Topics

### Objects
- [object AppPromotedPurchasesLinkagesResponse.Data](apppromotedpurchaseslinkagesresponse/data-data.dictionary.md)
  The resource linkage identifying a promoted purchase associated with the app promoted purchases linkages response.

## Properties

- `data` ([AppPromotedPurchasesLinkagesResponse.Data]) *(required)*
- `links` (PagedDocumentLinks) *(required)*
- `meta` (PagingInformation)

## See Also

- [object PromotedPurchaseResponse](promotedpurchaseresponse.md)
  The response body for endpoints that read or modify a promoted in-app purchase or subscription.
- [object PromotedPurchasesResponse](promotedpurchasesresponse.md)
  The response body for endpoints that list promoted in-app purchases and subscriptions for an app.
- [object PromotedPurchaseCreateRequest](promotedpurchasecreaterequest.md)
  The request body you use to create a promoted purchase.
- [object PromotedPurchaseUpdateRequest](promotedpurchaseupdaterequest.md)
  The request body you use to update a promoted purchase update request.
- [object AppPromotedPurchasesLinkagesRequest](apppromotedpurchaseslinkagesrequest.md)
  The request body for updating the ordered list of in-app purchases and subscriptions promoted on an app’s product page.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/apppromotedpurchaseslinkagesresponse)*