# InAppPurchaseLocalization

**Framework**: App Store Connect API  
**Kind**: dictionary

The localized display name and description for an in-app purchase shown to customers in a specific language.

**Availability**:
- App Store Connect API 2.0+

## Declaration

```swift
object InAppPurchaseLocalization
```

## Topics

### Objects and types
- [object InAppPurchaseLocalization.Attributes](inapppurchaselocalization/attributes-data.dictionary.md)
  Attributes that describe an in-app purchase localization resource.
- [object InAppPurchaseLocalization.Relationships](inapppurchaselocalization/relationships-data.dictionary.md)
  The relationships you include in the request and those on which you can operate.

## Properties

- `attributes` (InAppPurchaseLocalization.Attributes)
- `id` (string) *(required)*
- `links` (ResourceLinks)
- `relationships` (InAppPurchaseLocalization.Relationships)
- `type` (string) *(required)*

## See Also

- [object InAppPurchaseContentResponse](inapppurchasecontentresponse.md)
  A response containing a single hosted content record for an in-app purchase.
- [object InAppPurchaseContent](inapppurchasecontent.md)
  Hosted downloadable content associated with a non-consumable in-app purchase.
- [object InAppPurchaseLocalizationCreateRequest](inapppurchaselocalizationcreaterequest.md)
  The request body you use to create an in-app purchase localization.
- [object InAppPurchaseLocalizationUpdateRequest](inapppurchaselocalizationupdaterequest.md)
  The request body you use to update an in-app purchase localization update request.
- [object InAppPurchaseLocalizationsResponse](inapppurchaselocalizationsresponse.md)
  The response body for endpoints that list localizations for an in-app purchase.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/inapppurchaselocalization)*