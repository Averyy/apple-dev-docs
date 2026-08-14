# Assignment

**Framework**: Device Management  
**Kind**: dictionary

The asset assignment for a user or device.

**Availability**:
- VPP License Management 2.0+

## Declaration

```swift
object Assignment
```

## Mentions

- [Subscribing to notifications](subscribing-to-notifications.md)

## Properties

- `adamId` (string): The unique identifier for a product in the store.
- `clientUserId` (string): The unique identifier for an active user in your organization.
- `idHash` (string)
- `pricingParam` (string): The quality of a product in the store.
- `serialNumber` (string): The unique identifier for a device in your organization.
- `userStatus` (string)

## See Also

- [object Asset](asset.md)
  A product in the store.
- [object ResponseAsset](responseasset.md)
  The asset that the organization owns.
- [object UnlimitedResponseAsset](unlimitedresponseasset.md)
  An asset with an unlimited license that the organization owns.
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
- [object ManageSubscriptionsRequest](managesubscriptionsrequest.md)
  The request for subscription management.
- [object ManageSubscriptionAdminsRequest](managesubscriptionadminsrequest.md)
  The request body for adding or removing subscription administrators.
- [object ManageSubscriptionAdminsResponse](managesubscriptionadminsresponse.md)
  The confirmation response that the server returns after adding or removing subscription administrators.
- [object ResponseSubscriptionAdmin](responsesubscriptionadmin.md)
  An administrator for a subscription.
- [object SubscriptionManagementResponse](subscriptionmanagementresponse.md)
  A confirmation response that reports your device management service’s subscription management support.
- [object MdmInfo](mdminfo.md)
  Information about the MDM client.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/assignment)*