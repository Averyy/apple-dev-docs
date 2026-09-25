# InAppPurchaseContentResponse

**Framework**: App Store Connect API  
**Kind**: dictionary

A response containing a single hosted content record for an In-App Purchase.

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
  Hosted downloadable content associated with a non-consumable In-App Purchase.
- [object InAppPurchaseLocalizationCreateRequest](inapppurchaselocalizationcreaterequest.md)
  The request body you use to create an In-App Purchase localization.
- [object InAppPurchaseLocalizationUpdateRequest](inapppurchaselocalizationupdaterequest.md)
  The request body you use to update an In-App Purchase localization update request.
- [object InAppPurchaseLocalizationsResponse](inapppurchaselocalizationsresponse.md)
  The response body for endpoints that list localizations for an In-App Purchase.
- [object InAppPurchaseLocalization](inapppurchaselocalization.md)
  The localized display name and description for an In-App Purchase shown to customers in a specific language.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/inapppurchasecontentresponse)*