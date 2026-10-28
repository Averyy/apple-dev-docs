# MerchantTokenUsageDataAvailabilityNotificationRequest

**Framework**: Apple Pay Merchant Token Management API  
**Kind**: dictionary  
**Role**: Object

The data for the merchant token usage data availability notification request.

**Availability**:
- Apple Pay Merchant Token Management API 1.0.12+

## Declaration

```
object MerchantTokenUsageDataAvailabilityNotificationRequest
```

## Discussion

Use this API to notify Apple servers that the user’s device can retrieve merchant token usage information. The request includes metadata about encryption and where to retrieve the usage information.

The `merchantPublicKey` passed in the request needs to be a `P-384` public key.

## Properties

- `merchantTokenIdentifier` (string) *(required)*: The unique identifier of the merchant token.

  **Maximum Length**: `64`
- `merchantTokenUsageMetadata` (MerchantTokenUsageMetadata) *(required)*: Metadata that’s encrypted using the `merchantTokenPublicKey`.

## See Also

### Merchant token usage information
- [Retrieve Merchant Token Public Key](./retrieve-merchant-token-public-key.md)
  Get the merchant token public key.
- [MerchantToken Usage Data Availability Notification](./merchanttoken-usage-data-availability-notification.md)
  Notify Apple servers that the user’s devices can retrieve merchant token usage information.
- [Get MerchantToken Usage Information Package](./get-merchanttoken-usage-information-package.md)
  Retrieve the merchant token usage information package from the merchant server.
- [object GetMerchantTokenUsageInformationPackageResponse](./getmerchanttokenusageinformationpackageresponse.md)
  The encrypted merchant token usage information package.
- [object AutomaticReloadPaymentDetails](../ApplePayMerchantTokenUsageInformation/automaticreloadpaymentdetails.md)
  Details about an automatic reload payment.
- [object CurrencyAmount](../ApplePayMerchantTokenUsageInformation/currencyamount.md)
  An amount of money.
- [object DeferredPaymentDetails](../ApplePayMerchantTokenUsageInformation/deferredpaymentdetails.md)
  Details about a deferred payment, such as a hotel booking or a preorder.
- [object PastPayment](../ApplePayMerchantTokenUsageInformation/pastpayment.md)
  A past payment.
- [object PaymentIssueDetails](../ApplePayMerchantTokenUsageInformation/paymentissuedetails.md)
  Details about a payment issue, such as a declined payment.
- [object RecurringPaymentDetails](../ApplePayMerchantTokenUsageInformation/recurringpaymentdetails.md)
  Details about a recurring payment, typically a subscription.
- [object UpcomingPayment](../ApplePayMerchantTokenUsageInformation/upcomingpayment.md)
  An upcoming payment.
- [object UsageInformation](../ApplePayMerchantTokenUsageInformation/usageinformation.md)
  Information about the usage of a merchant token, such as past and upcoming payments.


---

*[View on Apple Developer](https://developer.apple.com/documentation/merchanttokennotificationservices/merchanttokenusagedataavailabilitynotificationrequest)*