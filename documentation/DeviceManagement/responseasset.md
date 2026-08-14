# ResponseAsset

**Framework**: Device Management  
**Kind**: dictionary

The asset that the organization owns.

**Availability**:
- VPP License Management 2.0+

## Declaration

```swift
object ResponseAsset
```

## Mentions

- [Managing assets](managing-assets.md)

## Properties

- `adamId` (string): The unique identifier for the product in the store.
- `assignedCount` (int32): The assigned amount of the asset.
- `availableCount` (int32): The available amount of the asset.
- `deviceAssignable` (boolean): The flag denoting whether the asset is device-assignable.
- `pricingParam` (string): The quality of the product in the store.
- `productType` (string): The asset product type.
- `retiredCount` (int32): The retired amount of the asset.
- `revocable` (boolean): The flag denoting whether the asset is revocable.
- `totalCount` (int32): The total amount of the asset.
- `supportedPlatforms` ([string]): The platforms that the asset supports.

## See Also

- [object Asset](asset.md)
  A product in the store.
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

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/responseasset)*