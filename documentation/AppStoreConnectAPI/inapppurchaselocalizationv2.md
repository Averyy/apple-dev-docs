# InAppPurchaseLocalizationV2

**Framework**: App Store Connect API  
**Kind**: dictionary

The localized display name and description for an in-app purchase configured with the v2 API, shown to customers in a specific language.

**Availability**:
- App Store Connect API 4.4.1+

## Declaration

```swift
object InAppPurchaseLocalizationV2
```

## Topics

### Objects and types
- [object InAppPurchaseLocalizationV2.Attributes](inapppurchaselocalizationv2/attributes-data.dictionary.md)
  Attributes that describe an in-app purchase localization resource.
- [object InAppPurchaseLocalizationV2.Relationships](inapppurchaselocalizationv2/relationships-data.dictionary.md)
  The relationships you include in the request and those on which you can operate.

## Properties

- `type` (string) *(required)*
- `id` (string) *(required)*
- `attributes` (InAppPurchaseLocalizationV2.Attributes)
- `relationships` (InAppPurchaseLocalizationV2.Relationships)
- `links` (ResourceLinks)

## See Also

- [object InAppPurchaseLocalizationV2CreateRequest](inapppurchaselocalizationv2createrequest.md)
  The request body you use to create an in-app purchase localization with the v2 API.
- [object InAppPurchaseLocalizationV2Response](inapppurchaselocalizationv2response.md)
  The response body for endpoints that create, read, or modify an in-app purchase localization with the v2 API.
- [object InAppPurchaseLocalizationV2UpdateRequest](inapppurchaselocalizationv2updaterequest.md)
  The request body you use to update an in-app purchase localization with the v2 API.
- [object InAppPurchaseLocalizationsV2Response](inapppurchaselocalizationsv2response.md)
  The response body for endpoints that list in-app purchase localizations configured with the v2 API.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/inapppurchaselocalizationv2)*