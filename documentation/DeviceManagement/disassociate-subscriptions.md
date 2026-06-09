# Disassociate Subscriptions

**Framework**: Device Management  
**Kind**: httpRequest

Disassociate subscriptions from client user IDs.

#### Discussion

##### Example Request and Response

**Request**:

```json
{
    "adamIds": [12345],
    "clientUserIds": ["vpp-user"],
    "deferred": true
}
```

**Response**:

```json
{
    "eventId": "c3f990d3-d8c5-41c6-8394-edb1f759a9d2",
    "tokenExpirationDate": "2030-11-08T22:33:22+0000",
    "uId": "2049025000431439"
}
```

## Topics

### Request and Response
- [object ManageSubscriptionsRequest](managesubscriptionsrequest.md)
  The request for subscription management.
- [object EventResponse](eventresponse.md)
  The response that contains the event identifier.
- [object ErrorResponse](errorresponse.md)
  The response that contains the error that occurs.
### Content Metadata
- [Managing subscriptions](managing-subscriptions.md)
  Administer auto-renewable subscription seats for your organization.

## Endpoint

`POST https://vpp.itunes.apple.com/mdm/v2/subscriptions/disassociate`

## Request Body

[`ManageSubscriptionsRequest`](managesubscriptionsrequest.md)

## See Also

- [Get Subscriptions](get-subscriptions.md)
  Get the subscriptions that your organization manages.
- [Get Subscription Assignments](get-subscription-assignments.md)
  Get the subscription assignments for users in your organization.
- [Associate Subscriptions](associate-subscriptions.md)
  Associate subscriptions with client user IDs.
- [Get Subscription Administrators](get-subscription-administrators.md)
  Get the administrators for subscriptions that your organization manages.
- [Add Subscription Administrators](add-subscription-administrators.md)
  Add administrators for subscriptions.
- [Remove Subscription Administrators](remove-subscription-administrators.md)
  Remove administrators from subscriptions.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/disassociate-subscriptions)*