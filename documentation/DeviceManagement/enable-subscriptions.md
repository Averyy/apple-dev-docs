# Enable Subscriptions

**Framework**: Device Management  
**Kind**: httpRequest

Declare that your device management service supports subscription management.

#### Discussion

Send a POST request to declare that your device management service supports subscription management. Until you enable subscription management for a token, content managers can’t purchase subscriptions into the organizational unit that the token represents.

This request takes no body. The server processes it synchronously and returns the resulting `subscriptionManagement` state.

> ⚠️ **Warning**:  Enabling subscription management for an organizational unit is permanent. After an organizational unit opts in as enabled, you can’t disable it. Enable an organizational unit only after your device management service is ready to manage subscription assignments for it.

##### Example Request and Response

**Request**:

```None
curl --location --request POST 'https://vpp.itunes.apple.com/mdm/v2/subscriptions/enable' \
--header 'Authorization: Bearer {sToken}'
```

**Response**:

```json
{
    "mdmInfo": null,
    "subscriptionManagement": true,
    "tokenExpirationDate": "2030-11-08T22:33:22+0000",
    "uId": "2049025000431439"
}
```

To declare that an organizational unit doesn’t support subscriptions, use [`Disable Subscriptions`](disable-subscriptions.md).

## Topics

### Response
- [object SubscriptionManagementResponse](subscriptionmanagementresponse.md)
  A confirmation response that reports your device management service’s subscription management support.
- [object ErrorResponse](errorresponse.md)
  The response that contains the error that occurs.
### Content Metadata
- [Managing subscriptions](managing-subscriptions.md)
  Administer auto-renewable subscription seats for your organization.

## Endpoint

`POST https://vpp.itunes.apple.com/mdm/v2/subscriptions/enable`

## See Also

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
- [Get Subscription Administrators](get-subscription-administrators.md)
  Get the administrators for subscriptions that your organization manages.
- [Add Subscription Administrators](add-subscription-administrators.md)
  Add administrators for subscriptions.
- [Remove Subscription Administrators](remove-subscription-administrators.md)
  Remove administrators from subscriptions.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/enable-subscriptions)*