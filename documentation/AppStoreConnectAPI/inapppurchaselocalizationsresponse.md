# InAppPurchaseLocalizationsResponse

**Framework**: App Store Connect API  
**Kind**: dictionary

The response body for endpoints that list localizations for an in-app purchase.

**Availability**:
- App Store Connect API 2.0+

## Declaration

```swift
object InAppPurchaseLocalizationsResponse
```

## Properties

- `data` ([InAppPurchaseLocalization]) *(required)*
- `included` ([InAppPurchaseV2])
- `links` (PagedDocumentLinks) *(required)*
- `meta` (PagingInformation)

## See Also

- [object InAppPurchaseContentResponse](inapppurchasecontentresponse.md)
  A response containing a single hosted content record for an in-app purchase.
- [object InAppPurchaseContent](inapppurchasecontent.md)
  Hosted downloadable content associated with a non-consumable in-app purchase.
- [object InAppPurchaseLocalizationCreateRequest](inapppurchaselocalizationcreaterequest.md)
  The request body you use to create an in-app purchase localization.
- [object InAppPurchaseLocalizationUpdateRequest](inapppurchaselocalizationupdaterequest.md)
  The request body you use to update an in-app purchase localization update request.
- [object InAppPurchaseLocalization](inapppurchaselocalization.md)
  The localized display name and description for an in-app purchase shown to customers in a specific language.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/inapppurchaselocalizationsresponse)*