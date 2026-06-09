# SubscriptionSubmission

**Framework**: App Store Connect API  
**Kind**: dictionary

A submission of an auto-renewable subscription to App Store review.

**Availability**:
- App Store Connect API 2.0+

## Declaration

```swift
object SubscriptionSubmission
```

## Topics

### Objects
- [object SubscriptionSubmission.Relationships](subscriptionsubmission/relationships-data.dictionary.md)
  The relationships you include in the request and those on which you can operate.

## Properties

- `id` (string) *(required)*
- `links` (ResourceLinks)
- `relationships` (SubscriptionSubmission.Relationships)
- `type` (string) *(required)*

## See Also

- [object SubscriptionGroupSubmissionCreateRequest](subscriptiongroupsubmissioncreaterequest.md)
  The request body you use to create a subscription group submission.
- [object SubscriptionGroupSubmission](subscriptiongroupsubmission.md)
  A submission of a subscription group to App Store review, required before offering subscriptions to customers.
- [object SubscriptionGroupSubmissionResponse](subscriptiongroupsubmissionresponse.md)
  A response confirming the submission of a subscription group for App Store review.
- [object SubscriptionSubmissionCreateRequest](subscriptionsubmissioncreaterequest.md)
  The request body you use to create a subscription submission.
- [object SubscriptionSubmissionResponse](subscriptionsubmissionresponse.md)
  A response confirming the submission of a subscription for App Store review.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/subscriptionsubmission)*