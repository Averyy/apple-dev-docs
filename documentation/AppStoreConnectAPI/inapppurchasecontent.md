# InAppPurchaseContent

**Framework**: App Store Connect API  
**Kind**: dictionary

Hosted downloadable content associated with a non-consumable In-App Purchase.

**Availability**:
- App Store Connect API 2.0+

## Declaration

```swift
object InAppPurchaseContent
```

## Topics

### Objects
- [object InAppPurchaseContent.Attributes](inapppurchasecontent/attributes-data.dictionary.md)
  Attributes that describe an In-App Purchase content resource.
- [object InAppPurchaseContent.Relationships](inapppurchasecontent/relationships-data.dictionary.md)
  The relationships you include in the request and those on which you can operate.

## Properties

- `attributes` (InAppPurchaseContent.Attributes)
- `id` (string) *(required)*
- `links` (ResourceLinks)
- `relationships` (InAppPurchaseContent.Relationships)
- `type` (string) *(required)*

## See Also

- [object InAppPurchaseContentResponse](inapppurchasecontentresponse.md)
  A response containing a single hosted content record for an In-App Purchase.
- [object InAppPurchaseLocalizationCreateRequest](inapppurchaselocalizationcreaterequest.md)
  The request body you use to create an In-App Purchase localization.
- [object InAppPurchaseLocalizationUpdateRequest](inapppurchaselocalizationupdaterequest.md)
  The request body you use to update an In-App Purchase localization update request.
- [object InAppPurchaseLocalizationsResponse](inapppurchaselocalizationsresponse.md)
  The response body for endpoints that list localizations for an In-App Purchase.
- [object InAppPurchaseLocalization](inapppurchaselocalization.md)
  The localized display name and description for an In-App Purchase shown to customers in a specific language.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/inapppurchasecontent)*