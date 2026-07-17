# InAppPurchaseLocalizationV2Response

**Framework**: App Store Connect API  
**Kind**: dictionary

The response body for endpoints that create, read, or modify an in-app purchase localization with the v2 API.

**Availability**:
- App Store Connect API 4.4.1+

## Declaration

```swift
object InAppPurchaseLocalizationV2Response
```

## Properties

- `data` (InAppPurchaseLocalizationV2) *(required)*
- `included` ([InAppPurchaseVersion])
- `links` (DocumentLinks) *(required)*

## See Also

- [object InAppPurchaseLocalizationV2](inapppurchaselocalizationv2.md)
  The localized display name and description for an in-app purchase configured with the v2 API, shown to customers in a specific language.
- [object InAppPurchaseLocalizationV2CreateRequest](inapppurchaselocalizationv2createrequest.md)
  The request body you use to create an in-app purchase localization with the v2 API.
- [object InAppPurchaseLocalizationV2UpdateRequest](inapppurchaselocalizationv2updaterequest.md)
  The request body you use to update an in-app purchase localization with the v2 API.
- [object InAppPurchaseLocalizationsV2Response](inapppurchaselocalizationsv2response.md)
  The response body for endpoints that list in-app purchase localizations configured with the v2 API.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/inapppurchaselocalizationv2response)*