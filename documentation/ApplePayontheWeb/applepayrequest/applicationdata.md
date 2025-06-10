# applicationData

**Framework**: Apple Pay on the Web  
**Kind**: property

A Base64-encoded string used to contain your application-specific data.

**Availability**:
- Safari Desktop 10.0+
- Safari Mobile 10.0+

## Declaration

```swift
DOMString applicationData;
```

#### Discussion

Use this property to contain additional data as may be appropriate for your website. For example, the application data may be a shopping cart identifier or an order number that your backend system needs to identify this transaction.

You’re responsible for sending the full application data to your server, if needed.

> ❗ **Important**:  If you use [`RegisterMerchantRequest`](https://developer.apple.com/documentation/ApplePayWebMerchantRegistrationAPI/RegisterMerchantRequest) in the [`Apple Pay Web Merchant Registration API`](https://developer.apple.com/documentation/ApplePayWebMerchantRegistrationAPI) to register merchants, you must include the merchant domain in [`applicationData`](applepayrequest/applicationdata.md). The payment service provider can use the domain in [`applicationData`](applepayrequest/applicationdata.md) to ensure they know which merchant the payment token is for. The payment service provider uses the value in [`applicationData`](applepayrequest/applicationdata.md) in a step necessary to validate the payment data. For more information, see [`Payment token format reference`](https://developer.apple.com/documentation/PassKit/payment-token-format-reference).

The [`applicationData`](applepayrequest/applicationdata.md) string must be a valid Base64-encoded string; otherwise, the system ignores it.


---

*[View on Apple Developer](https://developer.apple.com/documentation/applepayontheweb/applepayrequest/applicationdata)*