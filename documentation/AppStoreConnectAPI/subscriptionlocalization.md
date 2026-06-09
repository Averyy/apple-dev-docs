# SubscriptionLocalization

**Framework**: App Store Connect API  
**Kind**: dictionary

The localized display name and description for an auto-renewable subscription shown to customers on the App Store.

**Availability**:
- App Store Connect API 2.0+

## Declaration

```swift
object SubscriptionLocalization
```

## Topics

### Objects
- [object SubscriptionLocalization.Attributes](subscriptionlocalization/attributes-data.dictionary.md)
  Attributes that describe a subscription localization resource.
- [object SubscriptionLocalization.Relationships](subscriptionlocalization/relationships-data.dictionary.md)
  The relationships you include in the request and those on which you can operate.

## Properties

- `attributes` (SubscriptionLocalization.Attributes)
- `id` (string) *(required)*
- `links` (ResourceLinks)
- `relationships` (SubscriptionLocalization.Relationships)
- `type` (string) *(required)*

## See Also

- [object SubscriptionLocalizationCreateRequest](subscriptionlocalizationcreaterequest.md)
  The request body you use to create a subscription localization.
- [object SubscriptionLocalizationUpdateRequest](subscriptionlocalizationupdaterequest.md)
  The request body you use to update a subscription localization update request.
- [object SubscriptionLocalizationResponse](subscriptionlocalizationresponse.md)
  The response body for endpoints that create, read, or modify a single subscription localization.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/subscriptionlocalization)*