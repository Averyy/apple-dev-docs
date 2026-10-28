# tokenNotificationURL

**Framework**: PassKit (Apple Pay and Wallet)  
**Kind**: property  
**Role**: Instance Property

A URL you provide to receive life-cycle notifications from the Apple Pay servers about the Apple Pay merchant token for the automatic reload payment.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- visionOS 1.0+

## Declaration

```swift
var tokenNotificationURL: URL? { get set }
```

```objc
@property (nonatomic, strong, nullable) NSURL * tokenNotificationURL;
```

## Discussion

The [`tokenNotificationURL`](./tokennotificationurl.md) is optional. Set this property to receive notifications for life-cycle updates to the merchant token, for example, when the card issuer or the user deletes the token.

For more information about handling merchant token life-cycle notifications, see [Receiving and handling merchant token notifications](../../ApplePayMerchantTokenManagementAPI/receiving-and-handling-merchant-token-notifications.md).

## See Also

### Managing payment tokens
- [var managementURL: URL](./managementurl.md)
  A URL to a web page where the user can manage and delete the payment method for the automatic reload payment.


---

*[View on Apple Developer](https://developer.apple.com/documentation/passkit/pkautomaticreloadpaymentrequest/tokennotificationurl)*