# ResponseSubscription

**Framework**: Device Management  
**Kind**: dictionary

A subscription with its assignment counts.

## Declaration

```swift
object ResponseSubscription
```

## Topics

### Objects and Data Types
- [object SubscriptionCounts](subscriptioncounts.md)
  The subscription assignment counts broken down by assigned and available.

## Properties

- `parentAdamId` (int64): The parent Adam ID for the subscription.
- `adamId` (int64): The Adam ID for the subscription.
- `status` (string): The current state of the subscription.
- `periodEndDate` (string): The end date of the current billing period in ISO-8601 calendar date format (`YYYY-MM-DD`).
- `counts` (SubscriptionCounts): The assignment counts for the subscription, broken down by renewal state.

## See Also

- [object Asset](asset.md)
  A product in the store.
- [object ResponseAsset](responseasset.md)
  The asset that the organization owns.
- [object UnlimitedResponseAsset](unlimitedresponseasset.md)
  An asset with an unlimited license that the organization owns.
- [object Assignment](assignment.md)
  The asset assignment for a user or device.
- [object RequestUser](requestuser.md)
  The requested user in the organization.
- [object ResponseUser](responseuser.md)
  The user in the organization.
- [object ResponseSubscriptionAssignment](responsesubscriptionassignment.md)
  An assignment of a subscription to a user.
- [object SubscriptionCounts](subscriptioncounts.md)
  The subscription assignment counts broken down by assigned and available.
- [object SubscriptionCountsBreakdown](subscriptioncountsbreakdown.md)
  The breakdown of subscription counts by renewing and expiring status.
- [object ManageSubscriptionsRequest](managesubscriptionsrequest.md)
  The request for subscription management.
- [object ManageSubscriptionAdminsRequest](managesubscriptionadminsrequest.md)
- [object ManageSubscriptionAdminsResponse](managesubscriptionadminsresponse.md)
- [object ResponseSubscriptionAdmin](responsesubscriptionadmin.md)
- [object MdmInfo](mdminfo.md)
  Information about the MDM client.
- [object EventResponse](eventresponse.md)
  The response that contains the event identifier.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/responsesubscription)*