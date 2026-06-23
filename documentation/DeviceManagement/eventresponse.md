# EventResponse

**Framework**: Device Management  
**Kind**: dictionary

The response that contains the event identifier.

**Availability**:
- VPP License Management 2.0+

## Declaration

```swift
object EventResponse
```

## Mentions

- [Managing assets](managing-assets.md)
- [Managing users](managing-users.md)

## Topics

### Objects and Data Types
- [object MdmInfo](mdminfo.md)
  Information about the MDM client.

## Properties

- `eventId` (string): The unique identifier for the asynchronous event.
- `mdmInfo` (MdmInfo): The current information for the provided token. The response only includes this field when MDM sets a value using the [`Client Config`](client-config-4szk1.md) endpoint.
- `tokenExpirationDate` (string): The token expiration date in an ISO-8601 format. Note: The server shows all dates and times in UTC.
- `uId` (string): The unique library identifier. When querying records using multiple tokens that may share libraries, use the `uId` field to filter duplicates and avoid double-counting records when different content managers upload duplicate tokens.

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
- [object MdmInfo](mdminfo.md)
  Information about the MDM client.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/eventresponse)*