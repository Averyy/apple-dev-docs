# InAppPurchaseContentResponse

**Framework**: App Store Connect API  
**Kind**: dictionary

A response containing a single hosted content record for an in-app purchase.

**Availability**:
- App Store Connect API 2.0+

## Declaration

```swift
object InAppPurchaseContentResponse
```

## Properties

- `data` (InAppPurchaseContent) *(required)*
- `included` ([InAppPurchaseV2])
- `links` (DocumentLinks) *(required)*

## See Also

- [object InAppPurchaseContent](inapppurchasecontent.md)
  Hosted downloadable content associated with a non-consumable in-app purchase.
- [object InAppPurchaseLocalizationCreateRequest](inapppurchaselocalizationcreaterequest.md)
  The request body you use to create an in-app purchase localization.
- [object InAppPurchaseLocalizationUpdateRequest](inapppurchaselocalizationupdaterequest.md)
  The request body you use to update an in-app purchase localization update request.
- [object InAppPurchaseLocalizationsResponse](inapppurchaselocalizationsresponse.md)
  The response body for endpoints that list localizations for an in-app purchase.
- [object InAppPurchaseLocalization](inapppurchaselocalization.md)
  The localized display name and description for an in-app purchase shown to customers in a specific language.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/inapppurchasecontentresponse)*