# InAppPurchaseLocalizationsV2Response

**Framework**: App Store Connect API  
**Kind**: dictionary

The response body for endpoints that list In-App Purchase localizations configured with the v2 API.

**Availability**:
- App Store Connect API 4.4.1+

## Declaration

```swift
object InAppPurchaseLocalizationsV2Response
```

## Properties

- `data` ([InAppPurchaseLocalizationV2]) *(required)*
- `included` ([InAppPurchaseVersion])
- `links` (PagedDocumentLinks) *(required)*
- `meta` (PagingInformation)

## See Also

- [object InAppPurchaseLocalizationV2](inapppurchaselocalizationv2.md)
  The localized display name and description for an In-App Purchase configured with the v2 API, shown to customers in a specific language.
- [object InAppPurchaseLocalizationV2CreateRequest](inapppurchaselocalizationv2createrequest.md)
  The request body you use to create an In-App Purchase localization with the v2 API.
- [object InAppPurchaseLocalizationV2Response](inapppurchaselocalizationv2response.md)
  The response body for endpoints that create, read, or modify an In-App Purchase localization with the v2 API.
- [object InAppPurchaseLocalizationV2UpdateRequest](inapppurchaselocalizationv2updaterequest.md)
  The request body you use to update an In-App Purchase localization with the v2 API.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/inapppurchaselocalizationsv2response)*