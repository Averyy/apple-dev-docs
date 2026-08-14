# StatusResponse

**Framework**: Device Management  
**Kind**: dictionary

The status of an asynchronous event.

## Declaration

```swift
object StatusResponse
```

## Mentions

- [Handling error responses](handling-error-responses.md)
- [Managing assets](managing-assets.md)
- [Managing users](managing-users.md)

#### Discussion

Compare `numCompleted` against `numRequested` to track the progress of an event. When an event finishes with failures, `failures` describes each one.

## Topics

### Objects and Data Types
- [object ErrorResponse](errorresponse.md)
  The response that contains the error that occurs.
- [object MdmInfo](mdminfo.md)
  Information about the MDM client.

## Properties

- `eventStatus` (string): The current status of the asynchronous event.
- `eventType` (string): The type of the asynchronous event.
- `failures` ([ErrorResponse]): The set of failures that occurred while the server processed the event.
- `mdmInfo` (MdmInfo): The client-specific information that the server stores for your device management service.
- `numCompleted` (int32): The number of tasks from the request that the server completed.
- `numRequested` (int32): The total number of tasks in the request.
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
  The request body for adding or removing subscription administrators.
- [object ManageSubscriptionAdminsResponse](managesubscriptionadminsresponse.md)
  The confirmation response that the server returns after adding or removing subscription administrators.
- [object ResponseSubscriptionAdmin](responsesubscriptionadmin.md)
  An administrator for a subscription.
- [object SubscriptionManagementResponse](subscriptionmanagementresponse.md)
  A confirmation response that reports your device management service’s subscription management support.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/statusresponse)*