# tokenNotificationURL

**Framework**: Apple Pay on the Web  
**Kind**: property

A URL you provide to receive life-cycle notifications from the Apple Pay servers about the Apple Pay merchant token for the recurring payment.

**Availability**:
- Safari Desktop 10.0+
- Safari Mobile 10.0+

## Declaration

```swift
DOMString tokenNotificationURL;
```

#### Discussion

The [`tokenNotificationURL`](applepayautomaticreloadpaymentrequest/tokennotificationurl.md) is optional. Set this property to receive notifications for life-cycle updates to the merchant token, for example, when the card issuer or the user deletes the merchant token.

For more information about handling merchant token life-cycle notifications, see [`Receiving and handling merchant token notifications`](https://developer.apple.com/documentation/ApplePayMerchantTokenManagementAPI/receiving-and-handling-merchant-token-notifications).


---

*[View on Apple Developer](https://developer.apple.com/documentation/applepayontheweb/applepayautomaticreloadpaymentrequest/tokennotificationurl)*