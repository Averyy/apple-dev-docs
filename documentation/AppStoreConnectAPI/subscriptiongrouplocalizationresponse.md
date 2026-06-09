# SubscriptionGroupLocalizationResponse

**Framework**: App Store Connect API  
**Kind**: dictionary

The response body for endpoints that create, read, or modify a single subscription group localization.

**Availability**:
- App Store Connect API 2.0+

## Declaration

```swift
object SubscriptionGroupLocalizationResponse
```

## Properties

- `data` (SubscriptionGroupLocalization) *(required)*
- `included` ([SubscriptionGroup])
- `links` (DocumentLinks) *(required)*

## See Also

- [object SubscriptionGroupLocalization](subscriptiongrouplocalization.md)
  The localized display name and optional custom app name for a subscription group, shown to customers on the App Store.
- [object SubscriptionGroupLocalizationCreateRequest](subscriptiongrouplocalizationcreaterequest.md)
  The request body you use to create a subscription group localization.
- [object SubscriptionGroupLocalizationUpdateRequest](subscriptiongrouplocalizationupdaterequest.md)
  The request body you use to update a subscription group localization update request.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/subscriptiongrouplocalizationresponse)*