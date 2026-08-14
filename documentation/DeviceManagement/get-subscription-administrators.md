# Get Subscription Administrators

**Framework**: Device Management  
**Kind**: httpRequest

Get the administrators for subscriptions that your organization manages.

#### Discussion

##### Example Request and Response

**Request**:

```None
?adamId=12345&includeUserState=true
```

**Response**:

```json
{
    "admins": [
        {
            "adamId": 12345,
            "clientUserId": "vpp-user",
            "idHash": "rRVS8rlBrJjRqYwL8aNGDJG2CbU=",
            "userStatus": "Associated"
        }
    ],
    "nextCursor": "NjY5MjY0ODEtZTA4ZC00MmRhLTkxYjItMzdmMDI1MTVkYjQy",
    "uId": "2049025000431439",
    "tokenExpirationDate": "2030-11-08T22:33:22+0000",
    "versionId": "f5897284-ed94-510f-8914-3b88c9c67799"
}
```

## Topics

### Response
- [object GetSubscriptionAdminsResponse](getsubscriptionadminsresponse.md)
  The response that contains the requested subscription administrators.
- [object ErrorResponse](errorresponse.md)
  The response that contains the error that occurs.
### Content Metadata
- [Managing subscriptions](managing-subscriptions.md)
  Administer auto-renewable subscription seats for your organization.

## Endpoint

`GET https://vpp.itunes.apple.com/mdm/v2/subscriptions/admins`

## Parameters

- `adamId` ([int64]): The filter for subscription administrators by Adam ID.
- `includeUserState` (boolean): When `true`, includes the user status for each administrator in the response.
- `cursor` (string): The cursor for pagination to fetch the next page of results.

## See Also

- [Enable Subscriptions](enable-subscriptions.md)
  Declare that your device management service supports subscription management.
- [Disable Subscriptions](disable-subscriptions.md)
  Declare that your device management service doesn’t support subscription management.
- [Get Subscriptions](get-subscriptions.md)
  Get the subscriptions that your organization manages.
- [Get Subscription Assignments](get-subscription-assignments.md)
  Get the subscription assignments for users in your organization.
- [Associate Subscriptions](associate-subscriptions.md)
  Associate subscriptions with client user IDs.
- [Disassociate Subscriptions](disassociate-subscriptions.md)
  Disassociate subscriptions from client user IDs.
- [Add Subscription Administrators](add-subscription-administrators.md)
  Add administrators for subscriptions.
- [Remove Subscription Administrators](remove-subscription-administrators.md)
  Remove administrators from subscriptions.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/get-subscription-administrators)*