# Subscription and Subscription Group Submissions

**Framework**: App Store Connect API

Create review submissions for auto-renewable subscriptions and subscription groups.

**Availability**:
- App Store Connect API 2.0+

#### Overview

> ❗ **Important**:  This is deprecated. Use [`Review submissions`](review-submissions.md) instead.

## Topics

### Endpoints
- [Create a review submission for a subscription group](post-v1-subscriptiongroupsubmissions.md)
  Create a subscription group submission for review.
- [Create a review submission for a subscription](post-v1-subscriptionsubmissions.md)
  Create a review submission for an auto-renewable subscription.
### Objects
- [object SubscriptionGroupSubmissionCreateRequest](subscriptiongroupsubmissioncreaterequest.md)
  The request body you use to create a subscription group submission.
- [object SubscriptionGroupSubmission](subscriptiongroupsubmission.md)
  A submission of a subscription group to App Store review, required before offering subscriptions to customers.
- [object SubscriptionGroupSubmissionResponse](subscriptiongroupsubmissionresponse.md)
  A response confirming the submission of a subscription group for App Store review.
- [object SubscriptionSubmissionCreateRequest](subscriptionsubmissioncreaterequest.md)
  The request body you use to create a subscription submission.
- [object SubscriptionSubmission](subscriptionsubmission.md)
  A submission of an auto-renewable subscription to App Store review.
- [object SubscriptionSubmissionResponse](subscriptionsubmissionresponse.md)
  A response confirming the submission of a subscription for App Store review.

## See Also

- [Submitting subscriptions and subscription groups for App Review](submitting-subscriptions-and-subscription-groups-for-app-review.md)
  Attach localizations and screenshots to a subscription version, then submit subscriptions and subscription groups for App Review.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreconnectapi/subscription-and-subscription-group-submissions)*