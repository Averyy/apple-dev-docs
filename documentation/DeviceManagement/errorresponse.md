# ErrorResponse

**Framework**: Device Management  
**Kind**: dictionary

The response that contains the error that occurs.

**Availability**:
- VPP License Management 2.0+

## Declaration

```swift
object ErrorResponse
```

## Mentions

- [Handling error responses](handling-error-responses.md)

## Topics

### Objects and Data Types
- [object ResponseErrorInfo](responseerrorinfo.md)
  Information about the error.

## Properties

- `errorInfo` (ResponseErrorInfo): The request-specific information regarding the failure.
- `errorMessage` (string): The human-readable error message that describes the failure.
- `errorNumber` (int32): The error number that represents the failure.

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
  Request body for adding or removing subscription administrators.
- [object ManageSubscriptionAdminsResponse](managesubscriptionadminsresponse.md)
  Confirmation response returned after adding or removing subscription administrators.
- [object ResponseSubscriptionAdmin](responsesubscriptionadmin.md)
  An administrator for a subscription.
- [object MdmInfo](mdminfo.md)
  Information about the MDM client.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/errorresponse)*