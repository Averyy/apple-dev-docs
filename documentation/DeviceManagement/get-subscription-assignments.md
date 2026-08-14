# Get Subscription Assignments

**Framework**: Device Management  
**Kind**: httpRequest

Get the subscription assignments for users in your organization.

## Mentions

- [Getting started with the management API](getting-started-with-the-management-api.md)

#### Discussion

##### Example Request and Response

**Request**:

```None
?parentAdamId=54321&adamId=12345
```

**Response**:

```json
{
    "assignments": [
        {
            "adamId": 12345,
            "clientUserId": "vpp-user",
            "renewing": true
        }
    ],
    "nextCursor": "NjY5MjY0ODEtZTA4ZC00MmRhLTkxYjItMzdmMDI1MTVkYjQy",
    "uId": "2049025000431439",
    "tokenExpirationDate": "2030-11-08T22:33:22+0000",
    "versionId": "0d434f66-4e0c-4556-a4a9-87a9bcc7da7c"
}
```

## Topics

### Response
- [object GetSubscriptionAssignmentsResponse](getsubscriptionassignmentsresponse.md)
  The response that contains the requested subscription assignments.
- [object ErrorResponse](errorresponse.md)
  The response that contains the error that occurs.
### Content Metadata
- [Managing subscriptions](managing-subscriptions.md)
  Administer auto-renewable subscription seats for your organization.

## Endpoint

`GET https://vpp.itunes.apple.com/mdm/v2/subscriptions/assignments`

## Parameters

- `parentAdamId` ([int64]): The filter for subscription assignments by parent Adam ID.
- `adamId` ([int64]): The filter for subscription assignments by Adam ID.
- `clientUserId` ([string]): The filter for subscription assignments by client user ID.
- `cursor` (string): The cursor for pagination to fetch the next page of results.

## See Also

- [Enable Subscriptions](enable-subscriptions.md)
  Declare that your device management service supports subscription management.
- [Disable Subscriptions](disable-subscriptions.md)
  Declare that your device management service doesn’t support subscription management.
- [Get Subscriptions](get-subscriptions.md)
  Get the subscriptions that your organization manages.
- [Associate Subscriptions](associate-subscriptions.md)
  Associate subscriptions with client user IDs.
- [Disassociate Subscriptions](disassociate-subscriptions.md)
  Disassociate subscriptions from client user IDs.
- [Get Subscription Administrators](get-subscription-administrators.md)
  Get the administrators for subscriptions that your organization manages.
- [Add Subscription Administrators](add-subscription-administrators.md)
  Add administrators for subscriptions.
- [Remove Subscription Administrators](remove-subscription-administrators.md)
  Remove administrators from subscriptions.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/get-subscription-assignments)*