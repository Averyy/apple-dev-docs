# Retrieve Merchant Token Public Key

**Framework**: Apple Pay Merchant Token Management API  
**Kind**: httpRequest  
**Role**: Web Service Endpoint

Get the merchant token public key.

**Availability**:
- Apple Pay Merchant Token Management API 1.0.12+

## Discussion

Your server calls this API to get the public key of a particular merchant token. This public key is created by the merchant token owner’s device. The key is a `P-384` public key. The response includes the `supportedCiphersuite`, which specifies the cipher suite to use when calling the `Merchant-Token-Usage-Data-Availability-Notification` or responding to [`Get MerchantToken Usage Information Package`](./get-merchanttoken-usage-information-package.md).

## Endpoint

`POST https://apple-pay-gateway.apple.com/paymentservices/v1/merchantId/{merchantId}/merchantToken/publicKey`

## Parameters

### Path Parameters

- `merchantId` (string) *(required)*: Your merchant identifier.

  **Maximum Length**: `64`

### Header Parameters

- `Accept` (string): The response format the client expects, for example, `application/json` for JSON.
- `Content-Type` (string) *(required)*: The format of the data sent in the request body, for example, `application/json` for JSON payloads.
- `x-request-id` (string) *(required)*: The header used to uniquely identify the request.

## Request Body

**Content-Type**: `application/json`  
**Type**: `RetrieveMerchantTokenPublicKeyRequest`

The request body you use for the merchant token public key.

## Responses

- `200` OK (`RetrieveMerchantTokenPublicKeyResponse`, `application/json`): Successful response.
- `202` Accepted (`ErrorResponse`, `application/json`): Accepted. The public key isn’t yet available. Apple notifies via `tokenNotificationURL` when it’s available.
- `400` Bad Request (`ErrorResponse`, `application/json`): Bad request.
- `403` Forbidden (`ErrorResponse`, `application/json`): Authorization failed.
- `404` Not Found (`ErrorResponse`, `application/json`): Resource not found.
- `409` Conflict (`ErrorResponse`, `application/json`): Metadata conflict. Update the `tokenNotificationURL`.
- `500` Internal Server Error (`ErrorResponse`, `application/json`): Internal server error.

## See Also

### Merchant token usage information
- [MerchantToken Usage Data Availability Notification](./merchanttoken-usage-data-availability-notification.md)
  Notify Apple servers that the user’s devices can retrieve merchant token usage information.
- [object MerchantTokenUsageDataAvailabilityNotificationRequest](./merchanttokenusagedataavailabilitynotificationrequest.md)
  The data for the merchant token usage data availability notification request.
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

*[View on Apple Developer](https://developer.apple.com/documentation/merchanttokennotificationservices/retrieve-merchant-token-public-key)*