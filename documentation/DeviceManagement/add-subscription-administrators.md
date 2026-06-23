# Add Subscription Administrators

**Framework**: Device Management  
**Kind**: httpRequest

Add administrators for subscriptions.

#### Discussion

Send a POST request to designate users as administrators for specific subscriptions. The request body requires an `adamIds` array of subscription identifiers and a `clientUserIds` array of user identifiers. The server processes this request synchronously.

##### Example Request and Response

**Request**:

```json
{
    "adamIds": [12345],
    "clientUserIds": ["vpp-user"]
}
```

**Response**:

```json
{
    "uId": "2049025000431439",
    "tokenExpirationDate": "2030-11-08T22:33:22+0000",
    "versionId": "f5897284-ed94-510f-8914-3b88c9c67799"
}
```

## Topics

### Request
- [object ManageSubscriptionAdminsRequest](managesubscriptionadminsrequest.md)
### Response
- [object ManageSubscriptionAdminsResponse](managesubscriptionadminsresponse.md)
- [object ErrorResponse](errorresponse.md)
  The response that contains the error that occurs.
### Content Metadata
- [Managing subscriptions](managing-subscriptions.md)
  Administer auto-renewable subscription seats for your organization.

## Endpoint

`POST https://vpp.itunes.apple.com/mdm/v2/subscriptions/admins/add`

## Request Body

[`ManageSubscriptionAdminsRequest`](managesubscriptionadminsrequest.md)

## See Also

- [Get Subscriptions](get-subscriptions.md)
  Get the subscriptions that your organization manages.
- [Get Subscription Assignments](get-subscription-assignments.md)
  Get the subscription assignments for users in your organization.
- [Associate Subscriptions](associate-subscriptions.md)
  Associate subscriptions with client user IDs.
- [Disassociate Subscriptions](disassociate-subscriptions.md)
  Disassociate subscriptions from client user IDs.
- [Get Subscription Administrators](get-subscription-administrators.md)
  Get the administrators for subscriptions that your organization manages.
- [Remove Subscription Administrators](remove-subscription-administrators.md)
  Remove administrators from subscriptions.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/add-subscription-administrators)*