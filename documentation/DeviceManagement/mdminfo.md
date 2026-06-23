# MdmInfo

**Framework**: Device Management  
**Kind**: dictionary

Information about the MDM client.

**Availability**:
- VPP License Management 2.0+

## Declaration

```swift
object MdmInfo
```

## Mentions

- [Getting started with the management API](getting-started-with-the-management-api.md)
- [Upgrading to the new management API](upgrading-to-the-new-management-api.md)

## Properties

- `id` (string): A unique identifier that MDM uses for an organization.
- `metadata` (string): A free-form field that MDM uses to store metadata for an organization.
- `name` (string): The name of the current MDM client.

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
- [object ManageSubscriptionsRequest](managesubscriptionsrequest.md)
  The request for subscription management.
- [object ManageSubscriptionAdminsRequest](managesubscriptionadminsrequest.md)
- [object ManageSubscriptionAdminsResponse](managesubscriptionadminsresponse.md)
- [object ResponseSubscriptionAdmin](responsesubscriptionadmin.md)
- [object EventResponse](eventresponse.md)
  The response that contains the event identifier.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/mdminfo)*