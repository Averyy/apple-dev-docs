# UnlimitedResponseAsset

**Framework**: Device Management  
**Kind**: dictionary

An asset with an unlimited license that the organization owns.

## Declaration

```swift
object UnlimitedResponseAsset
```

## Mentions

- [Managing assets](managing-assets.md)

#### Overview

The server returns this object in the `unlimitedAssets` array of [`GetAssetsResponse`](getassetsresponse.md) when the `unlimited` query parameter is set to `true`. This object omits the `availableCount`, `totalCount`, and `retiredCount` fields, which don’t apply to unlimited licenses.

## Properties

- `adamId` (string): The unique identifier for the product in the store.
- `assignedCount` (int32): The assigned amount of the asset.
- `deviceAssignable` (boolean): The flag denoting whether the asset is device-assignable.
- `pricingParam` (string): The quality of the product in the store.
- `productType` (string): The asset product type.
- `revocable` (boolean): The flag denoting whether the asset is revocable.
- `supportedPlatforms` ([string]): The platforms that the asset supports.

## See Also

- [object Asset](asset.md)
  A product in the store.
- [object ResponseAsset](responseasset.md)
  The asset that the organization owns.
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
- [object ManageSubscriptionAdminsResponse](managesubscriptionadminsresponse.md)
- [object ResponseSubscriptionAdmin](responsesubscriptionadmin.md)
- [object MdmInfo](mdminfo.md)
  Information about the MDM client.
- [object EventResponse](eventresponse.md)
  The response that contains the event identifier.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/unlimitedresponseasset)*