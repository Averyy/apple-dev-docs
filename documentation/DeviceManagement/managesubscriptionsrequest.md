# ManageSubscriptionsRequest

**Framework**: Device Management  
**Kind**: dictionary

The request for subscription management.

## Declaration

```swift
object ManageSubscriptionsRequest
```

## Mentions

- [Managing subscriptions](managing-subscriptions.md)

## Properties

- `adamIds` ([int64]) *(required)*: The set of Adam IDs for the subscriptions to manage.
- `clientUserIds` ([string]) *(required)*: The set of identifiers for users in your organization.
- `renewing` (boolean): A Boolean value that indicates whether the subscription is renewing. Used for association operations.
- `deferred` (boolean): A Boolean value that indicates whether the disassociation is deferred. Used for disassociation operations.

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
- [object ResponseSubscription](responsesubscription.md)
  A subscription with its assignment counts.
- [object ResponseSubscriptionAssignment](responsesubscriptionassignment.md)
  An assignment of a subscription to a user.
- [object SubscriptionCounts](subscriptioncounts.md)
  The subscription assignment counts broken down by assigned and available.
- [object SubscriptionCountsBreakdown](subscriptioncountsbreakdown.md)
  The breakdown of subscription counts by renewing and expiring status.
- [object ManageSubscriptionAdminsRequest](managesubscriptionadminsrequest.md)
  Request body for adding or removing subscription administrators.
- [object ManageSubscriptionAdminsResponse](managesubscriptionadminsresponse.md)
  Confirmation response returned after adding or removing subscription administrators.
- [object ResponseSubscriptionAdmin](responsesubscriptionadmin.md)
  An administrator for a subscription.
- [object MdmInfo](mdminfo.md)
  Information about the MDM client.
- [object EventResponse](eventresponse.md)
  The response that contains the event identifier.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/managesubscriptionsrequest)*