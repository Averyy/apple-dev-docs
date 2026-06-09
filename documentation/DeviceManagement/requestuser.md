# RequestUser

**Framework**: Device Management  
**Kind**: dictionary

The requested user in the organization.

**Availability**:
- VPP License Management 2.0+

## Declaration

```swift
object RequestUser
```

## Properties

- `clientUserId` (string) *(required)*: The unique identifier for a user in your organization.
- `email` (string): The email address for the user.
- `managedAppleId` (string): The Managed Apple Account for the user.

## See Also

- [object Asset](asset.md)
  A product in the store.
- [object ResponseAsset](responseasset.md)
  The asset that the organization owns.
- [object UnlimitedResponseAsset](unlimitedresponseasset.md)
  An asset with an unlimited license that the organization owns.
- [object Assignment](assignment.md)
  The asset assignment for a user or device.
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
- [object ManageSubscriptionsRequest](managesubscriptionsrequest.md)
  The request for subscription management.
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

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/requestuser)*