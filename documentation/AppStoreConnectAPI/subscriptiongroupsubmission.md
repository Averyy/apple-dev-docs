# SubscriptionGroupSubmission

**Framework**: App Store Connect API  
**Kind**: dictionary  
**Role**: Object

A submission of a subscription group to App Store review, required before offering subscriptions to customers.

**Availability**:
- App Store Connect API 2.0+ - Deprecated in 4.4.1

> **Deprecated**: This object is deprecated. Use the review submissions workflow instead.

## Declaration

```
object SubscriptionGroupSubmission
```

## Properties

- `id` (string) *(required)*
- `links` (ResourceLinks)
- `type` (string) *(required)*: **Allowed Values**: `subscriptionGroupSubmissions`

## See Also

### Objects
- [object SubscriptionGroupSubmissionCreateRequest](./subscriptiongroupsubmissioncreaterequest.md)
  The request body you use to create a subscription group submission.
- [object SubscriptionGroupSubmissionResponse](./subscriptiongroupsubmissionresponse.md)
  A response confirming the submission of a subscription group for App Store review.
- [object SubscriptionSubmissionCreateRequest](./subscriptionsubmissioncreaterequest.md)
  The request body you use to create a subscription submission.
- [object SubscriptionSubmission](./subscriptionsubmission.md)
  A submission of an auto-renewable subscription to App Store review.
- [object SubscriptionSubmissionResponse](./subscriptionsubmissionresponse.md)
  A response confirming the submission of a subscription for App Store review.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/subscriptiongroupsubmission)*