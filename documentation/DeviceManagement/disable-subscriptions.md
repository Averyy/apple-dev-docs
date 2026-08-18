# Disable Subscriptions

**Framework**: Device Management  
**Kind**: httpRequest

Declare that your device management service doesn’t support subscription management.

#### Discussion

Send a POST request to declare that your device management service doesn’t support subscriptions for the organizational unit that the token represents. Apple School Manager and Apple Business Manager use this declaration to indicate to content managers that the organizational unit doesn’t support subscriptions, rather than leaving its support status unstated.

This request takes no body. The server processes it synchronously and returns the resulting `subscriptionManagement` state.

> ❗ **Important**:  Disabling is a positive declaration that an organizational unit doesn’t support subscriptions. You can also use it to reverse an earlier [`Enable Subscriptions`](enable-subscriptions.md) request, but only while the organizational unit has no subscriptions. If any subscriptions exist there, the request fails with error `9818` (`Subscriptions exist for the organizational unit, so subscription management can't be disabled.`). For more information, see [`Handling error responses`](handling-error-responses.md).

##### Example Request and Response

**Request**:

```None
curl --location --request POST 'https://vpp.itunes.apple.com/mdm/v2/subscriptions/disable' \
--header 'Authorization: Bearer {sToken}'
```

**Response**:

```json
{
    "mdmInfo": null,
    "subscriptionManagement": false,
    "tokenExpirationDate": "2030-11-08T22:33:22+0000",
    "uId": "2049025000431439"
}
```

To declare that an organizational unit supports subscriptions, use [`Enable Subscriptions`](enable-subscriptions.md).

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

`POST https://vpp.itunes.apple.com/mdm/v2/subscriptions/disable`

## See Also

- [Enable Subscriptions](enable-subscriptions.md)
  Declare that your device management service supports subscription management.
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

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/disable-subscriptions)*