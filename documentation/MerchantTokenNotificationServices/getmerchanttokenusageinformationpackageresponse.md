# GetMerchantTokenUsageInformationPackageResponse

**Framework**: Apple Pay Merchant Token Management API  
**Kind**: dictionary

The encrypted merchant token usage information package.

**Availability**:
- Apple Pay Merchant Token Management API 1.0.12+

## Declaration

```swift
object GetMerchantTokenUsageInformationPackageResponse
```

## Mentions

- [Adding merchant token usage information](../applepaymerchanttokenmanagementapi/adding-merchant-token-usage-information.md)

#### Discussion

The `data` needs to be a merchant token usage information package encrypted to the `merchantTokenPublicKey` using HPKE in authorization mode with `merchantPrivateKey` and the following options:

| Option | Value |
| --- | --- |
| `KEM` | DHKEM(P-384, HKDF-SHA384) |
| `KDF` | HKDF-SHA384 |
| `AEAD` | AES-256-GCM |

The `merchantPrivateKey` needs to correspond to the `merchantPublicKey` provided in the merchant token usage information availability notification. The `info` parameter needs to be the UTF-8 bytes of `ApplePayMerchantTokenUsageInformation_1.0` concatenated with the SHA-256 digest (in bytes) of the `merchantTokenIdentifier` (encoded using UTF-8). For the `ciphersuite`, use the `supportedCiphersuite` returned by Apple in the [`Retrieve Merchant Token Public Key`](retrieve-merchant-token-public-key.md).

## See Also

- [Retrieve Merchant Token Public Key](retrieve-merchant-token-public-key.md)
  Get the merchant token public key.
- [MerchantToken Usage Data Availability Notification](merchanttoken-usage-data-availability-notification.md)
  Notify Apple servers that the user’s devices can retrieve merchant token usage information.
- [object MerchantTokenUsageDataAvailabilityNotificationRequest](merchanttokenusagedataavailabilitynotificationrequest.md)
  The data for the merchant token usage data availability notification request.
- [Get MerchantToken Usage Information Package](get-merchanttoken-usage-information-package.md)
  Retrieve the merchant token usage information package from the merchant server.
- [object AutomaticReloadPaymentDetails](../applepaymerchanttokenusageinformation/automaticreloadpaymentdetails.md)
  Details about an automatic reload payment.
- [object CurrencyAmount](../applepaymerchanttokenusageinformation/currencyamount.md)
  An amount of money.
- [object DeferredPaymentDetails](../applepaymerchanttokenusageinformation/deferredpaymentdetails.md)
  Details about a deferred payment, such as a hotel booking or a preorder.
- [object PastPayment](../applepaymerchanttokenusageinformation/pastpayment.md)
  A past payment.
- [object RecurringPaymentDetails](../applepaymerchanttokenusageinformation/recurringpaymentdetails.md)
  Details about a recurring payment, typically a subscription.
- [object UpcomingPayment](../applepaymerchanttokenusageinformation/upcomingpayment.md)
  An upcoming payment.
- [object UsageInformation](../applepaymerchanttokenusageinformation/usageinformation.md)
  Information about the usage of a merchant token, such as past and upcoming payments.


---

*[View on Apple Developer](https://developer.apple.com/documentation/merchanttokennotificationservices/getmerchanttokenusageinformationpackageresponse)*