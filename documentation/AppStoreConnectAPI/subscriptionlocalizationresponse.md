# SubscriptionLocalizationResponse

**Framework**: App Store Connect API  
**Kind**: dictionary

The response body for endpoints that create, read, or modify a single subscription localization.

**Availability**:
- App Store Connect API 2.0+

## Declaration

```swift
object SubscriptionLocalizationResponse
```

## Properties

- `data` (SubscriptionLocalization) *(required)*
- `included` ([Subscription])
- `links` (DocumentLinks) *(required)*

## See Also

- [object SubscriptionLocalizationCreateRequest](subscriptionlocalizationcreaterequest.md)
  The request body you use to create a subscription localization.
- [object SubscriptionLocalizationUpdateRequest](subscriptionlocalizationupdaterequest.md)
  The request body you use to update a subscription localization update request.
- [object SubscriptionLocalization](subscriptionlocalization.md)
  The localized display name and description for an auto-renewable subscription shown to customers on the App Store.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/subscriptionlocalizationresponse)*