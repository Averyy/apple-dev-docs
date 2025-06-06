# Send Merchant Token Event

**Framework**: Apple Pay Merchant Token Management API  
**Kind**: httpRequest

Receive and handle merchant token life-cycle updates from Apple Pay.

**Availability**:
- App Store Connect API 1.0.10+

#### Discussion

You implement this endpoint on your server to receive notifications about merchant token life-cycle events. When a life-cycle event affects the merchant token — for example, the card’s expiration date changes, or the user or issuer deletes the token — Apple Pay calls this endpoint to notify you.

To receive requests at this endpoint, your server needs to support the Transport Layer Security (TLS) 1.2 protocol or later.

Process the event in your system with the appropriate action. Respond with `200` `OK` if your endpoint successfully receives the notification, even if your endpoint can’t find the related merchant token or event identifier. Respond with `500` `Internal` `Server` `Error` if your endpoint isn’t able to process the notification request. Apple Pay immediately retries the notification up to three times if the response isn’t `200`.

For more information about implementing this endpoint on your server, see [`Receiving and handling merchant token notifications`](https://developer.apple.com/documentation/ApplePayMerchantTokenManagementAPI/receiving-and-handling-merchant-token-notifications).

## See Also

- [Receiving and handling merchant token notifications](../applepaymerchanttokenmanagementapi/receiving-and-handling-merchant-token-notifications.md)
  Implement an endpoint to receive and handle merchant token life-cycle updates from Apple Pay.


---

*[View on Apple Developer](https://developer.apple.com/documentation/merchanttokennotificationservices/send-merchant-token-event)*