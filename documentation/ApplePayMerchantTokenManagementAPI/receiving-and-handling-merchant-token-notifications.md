# Receiving and handling merchant token notifications

**Framework**: ApplePayMerchantTokenManagementAPI  
**Role**: Article

Implement an endpoint to receive and handle merchant token life-cycle updates from Apple Pay.

#### Overview

A *merchant token* associates a payment card, merchant, and user. Apple Pay issues a merchant token when a customer initiates a purchase using Apple Pay in your app or on your website. When your app or website creates a payment request for a recurring payment or an automatic-reload payment, you pass your server’s notification URL in the `tokenNotificationURL` parameter. When a life-cycle event affects the token — for example, the card’s expiration date changes, or the user or issuer deletes the token — Apple Pay sends you a notification with a unique event identifier to that `tokenNotificationURL`.

Implement the [`Send Merchant Token Event`](../MerchantTokenNotificationServices/send-merchant-token-event.md) endpoint at the `tokenNotificationURL` you provide to receive and handle merchant token updates from Apple Pay.

##### Configure your server for Apple Pay’s requirements

To incorporate Apple Pay, your server needs to adhere to the following requirements.

- HTTPS support
- A valid SSL certificate
- Support for the Transport Layer Security (TLS) 1.2 protocol, and at least one of the required cipher suites
- A strict allow list for Apple Pay IP addresses for merchant validation
- A strict allow list for Apple IP addresses for domain verification

For more information about meeting these requirements for your server, see [Setting Up Your Server](../ApplePayontheWeb/setting-up-your-server.md).

##### Create allow lists

For inbound merchant token notifications from Apple, allow the following IP addresses:

- `17.58.0.0/18`
- `17.58.192.0/18`

For merchant token event endpoints, allow the following URLs and IP addresses:

| Domain name | Primary | Disaster recovery |
| --- | --- | --- |
| `apple-pay-gateway-nc-pod*.apple.com` | `17.171.78.0 / 23` | `17.141.128.0 / 23` |
| `apple-pay-gateway-pr-pod*.apple.com` | `17.141.128.0 / 23` | `17.171.78.0 / 23` |
| `apple-pay-gateway-stage.apple.com` | `17.171.85.44` | NA |
| `apple-pay-gateway-cert.apple.com` | `17.171.85.7` | NA |

> **Note**:  Set up these allow lists for receiving and handling merchant token events in addition to the lists in [Setting Up Your Server](../ApplePayontheWeb/setting-up-your-server.md) that you set up generally for Apple Pay.

##### Enable your token notification endpoint

Add an endpoint that accepts a `GET` request in the following format:

```other
https://merchant.example.com/your-endpoint-for-notification/notification/merchantToken/{eventId}
```

Replace `merchant.example.com` with your server’s domain and top level domain (TLD) and `your-endpoint-for-notification` with your server’s path to the endpoint. Apple Pay appends the path component `notification/merchantToken`, and a unique event identifier as a path component after `notification/merchantToken`.

Provide the first part of the notification URL to payment requests that accept a `tokenNotificationURL` parameter.

```other
https://merchant.example.com/your-endpoint-for-notification
```

For more information about the endpoint, see [`Send Merchant Token Event`](../MerchantTokenNotificationServices/send-merchant-token-event.md).

For more information about payment requests that accept `tokenNotificationURL` as a parameter, see [`PKAutomaticReloadPaymentRequest`](../PassKit/pkautomaticreloadpaymentrequest.md), [`PKRecurringPaymentRequest`](../PassKit/pkrecurringpaymentrequest.md), [`ApplePayAutomaticReloadPaymentRequest`](../ApplePayontheWeb/applepayautomaticreloadpaymentrequest.md), and [`ApplePayRecurringPaymentRequest`](../ApplePayontheWeb/applepayrecurringpaymentrequest.md).

##### Receive and handle notifications

When a life-cycle event occurs to a card associated with a merchant token, Apple Pay sends a `GET` request to your [`Send Merchant Token Event`](../MerchantTokenNotificationServices/send-merchant-token-event.md) endpoint. Use the unique event identifier that Apple Pay sends and your merchant identifier to fetch information about this notification’s event. For more information, see [`Get Details of a Merchant Token Event`](../MerchantTokenNotificationServices/merchant-token-event-retrieval.md).

Process the event in your system with the appropriate action. Respond with `200` `OK` if your endpoint successfully receives the notification, even if your endpoint can’t find the related merchant token or event identifier. Respond with `500` `Internal` `Server` `Error` if your endpoint isn’t able to process the notification request. Apple Pay immediately retries the notification up to three times if the response isn’t `200`.

## See Also

### Merchant token notification handling
- [Send Merchant Token Event](../MerchantTokenNotificationServices/send-merchant-token-event.md)
  Receive and handle merchant token life-cycle updates from Apple Pay.
- [Update Merchant Metadata](../MerchantTokenNotificationServices/update-merchant-metadata.md)
  Update the merchant token’s notification URL.


---

*[View on Apple Developer](https://developer.apple.com/documentation/applepaymerchanttokenmanagementapi/receiving-and-handling-merchant-token-notifications)*