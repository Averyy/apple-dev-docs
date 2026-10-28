# Get MerchantToken Usage Information Package

**Framework**: Apple Pay Merchant Token Management API  
**Kind**: httpRequest  
**Role**: Web Service Endpoint

Retrieve the merchant token usage information package from the merchant server.

**Availability**:
- Apple Pay Merchant Token Management API 1.0.12+

## Discussion

The user’s device calls this API to get the merchant token usage information package from the merchant server. Devices use the `webServiceURL` delivered to the Apple Pay server as part of the metadata.

For more information on formatting your merchant token usage information, see [Adding merchant token usage information](../ApplePayMerchantTokenManagementAPI/adding-merchant-token-usage-information.md)

## Endpoint

`GET https://merchant.example.com/v1/merchantToken/{merchantTokenIdentifier}/usageInformation`

## Parameters

### Path Parameters

- `merchantTokenIdentifier` (string) *(required)*: The unique identifier of the merchant token.

### Header Parameters

- `Authorization` (string) *(required)*: Authentication for the usage information. The scheme is `ApplePayMerchantTokenUsageInformation` with the `authenticationToken` as a parameter. For example, `ApplePayMerchantTokenUsageInformation {authenticationToken}`.

## Responses

- `200` OK (`GetMerchantTokenUsageInformationPackageResponse`, `application/json`): The request was successful and the response includes the encrypted merchant token usage information package.
- `401` Unauthorized (`ErrorResponse`, `application/json`): Unauthorized. See the body for more details.
- `404` Not Found (`ErrorResponse`, `application/json`): Not found. See the body for more details.

## See Also

### Merchant token usage information
- [Retrieve Merchant Token Public Key](./retrieve-merchant-token-public-key.md)
  Get the merchant token public key.
- [MerchantToken Usage Data Availability Notification](./merchanttoken-usage-data-availability-notification.md)
  Notify Apple servers that the user’s devices can retrieve merchant token usage information.
- [object MerchantTokenUsageDataAvailabilityNotificationRequest](./merchanttokenusagedataavailabilitynotificationrequest.md)
  The data for the merchant token usage data availability notification request.
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

*[View on Apple Developer](https://developer.apple.com/documentation/merchanttokennotificationservices/get-merchanttoken-usage-information-package)*