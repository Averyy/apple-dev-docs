# Retrieve Merchant Token Public Key

**Framework**: Apple Pay Merchant Token Management API  
**Kind**: httpRequest

Get the merchant token public key.

**Availability**:
- Apple Pay Merchant Token Management API 1.0.12+

#### Discussion

Your server calls this API to get the public key of a particular merchant token. This public key is created by the merchant token owner’s device. The key is a `P-384` public key. The response includes the `supportedCiphersuite`, which specifies the cipher suite to use when calling the `Merchant-Token-Usage-Data-Availability-Notification` or responding to [`Get MerchantToken Usage Information Package`](get-merchanttoken-usage-information-package.md).

## Request Body

The request body you use for the merchant token public key.

## See Also

- [MerchantToken Usage Data Availability Notification](merchanttoken-usage-data-availability-notification.md)
  Notify Apple servers that the user’s devices can retrieve merchant token usage information.
- [object MerchantTokenUsageDataAvailabilityNotificationRequest](merchanttokenusagedataavailabilitynotificationrequest.md)
  The data for the merchant token usage data availability notification request.
- [Get MerchantToken Usage Information Package](get-merchanttoken-usage-information-package.md)
  Retrieve the merchant token usage information package from the merchant server.
- [object GetMerchantTokenUsageInformationPackageResponse](getmerchanttokenusageinformationpackageresponse.md)
  The encrypted merchant token usage information package.
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

*[View on Apple Developer](https://developer.apple.com/documentation/merchanttokennotificationservices/retrieve-merchant-token-public-key)*