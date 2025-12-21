# Apple Pay Merchant Token Management API

**Framework**: Apple Pay Merchant Token Management API  
**Kind**: module

Retrieve and manage payment life-cycle events for your Apple Pay merchant tokens.

**Availability**:
- App Store Connect API 1.0+

#### Overview

The Apple Pay Merchant Token Management API is a REST API that enables merchants to get the details of a life-cycle event after receiving a merchant token event notification. You can also use this API to inform Apple Pay servers to invalidate your token when it’s no longer in use.

Merchant tokens offer a reliable solution for taking recurring, deferred, and automatic reload payments with Apple Pay. Users can manage their merchant tokens in Wallet. You can enrich the token management experience by providing usage information, using the [`Apple Pay Merchant Token Usage Information API`](https://developer.apple.com/documentation/applepaymerchanttokenusageinformation). This helps users understand past payments and keep track of upcoming payments.

Apple Pay utilizes a tap-and-pull model to deliver events related to merchant tokens. In this process, the Apple Pay server notifies you of an event. Then you can subsequently retrieve the event details using the provided `eventId`. You can access the event details for seven days. The API between the device and you, the merchant, requires Transport Layer Security (TLS), and the device presents the merchant-provided `authenticationToken` to authenticate requests.

In addition, you can call the Apple Pay server to unlink Merchant Payment Account Numbers (MPANs). Access to the APIs between the Apple Pay server and the merchant requires mutual TLS.

A  associates a payment card, merchant, and user. Apple Pay issues a merchant token when a customer initiates a purchase using Apple Pay in your app or on your website. When your app or website creates a payment request for a recurring payment or an automatic reload payment, it passes your server’s notification URL in the `tokenNotificationURL` parameter. For more information about `tokenNotificationURL`, see [`PKAutomaticReloadPaymentRequest`](https://developer.apple.com/documentation/PassKit/PKAutomaticReloadPaymentRequest), [`PKRecurringPaymentRequest`](https://developer.apple.com/documentation/PassKit/PKRecurringPaymentRequest), [`ApplePayAutomaticReloadPaymentRequest`](https://developer.apple.com/documentation/ApplePayontheWeb/ApplePayAutomaticReloadPaymentRequest), [`ApplePayRecurringPaymentRequest`](https://developer.apple.com/documentation/ApplePayontheWeb/ApplePayRecurringPaymentRequest), [`PKDeferredPaymentRequest`](https://developer.apple.com/documentation/PassKit/PKDeferredPaymentRequest), and [`ApplePayDeferredPaymentRequest`](https://developer.apple.com/documentation/ApplePayontheWeb/ApplePayDeferredPaymentRequest).

If a life-cycle event affects the token — for example, the card’s expiration date changes, or the user or issuer deletes the token — Apple Pay sends you a notification with an event identifier to that `tokenNotificationURL`. You retrieve the details of the event by calling [`Get Details of a Merchant Token Event`](merchant-token-event-retrieval.md) with the event identifier.

## Topics

### Essentials
- [Adding merchant token usage information](../applepaymerchanttokenmanagementapi/adding-merchant-token-usage-information.md)
  Create directories and add files, images, and localization for your merchant token usage information package.
- [Apple Pay Merchant Token Usage Information API](../applepaymerchanttokenusageinformation/applepaymerchanttokenusageinformation.md)
  Add details about your merchant token usage information package.
### Merchant token notification handling
- [Receiving and handling merchant token notifications](../applepaymerchanttokenmanagementapi/receiving-and-handling-merchant-token-notifications.md)
  Implement an endpoint to receive and handle merchant token life-cycle updates from Apple Pay.
- [Send Merchant Token Event](send-merchant-token-event.md)
  Receive and handle merchant token life-cycle updates from Apple Pay.
- [Update Merchant Metadata](update-merchant-metadata.md)
  Update the merchant token’s notification URL.
### Merchant token event retrieval
- [Get Details of a Merchant Token Event](merchant-token-event-retrieval.md)
  Get the details of a merchant token event after receiving a notification.
- [object MerchantTokenEventResponse](merchanttokeneventresponse.md)
  A response body that contains information about a life-cycle event for a merchant token.
- [object MerchantTokenMetadata](merchanttokenmetadata.md)
  The card information related to a merchant token, including its card art and metadata.
- [object CardArt](cardart.md)
  Data for displaying art to represent a card.
- [object CardMetadata](cardmetadata.md)
  Data about the card, including its expiration date and suffix.
### Merchant token usage information
- [Retrieve Merchant Token Public Key](retrieve-merchant-token-public-key.md)
  Get the merchant token public key.
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
### Merchant token invalidation
- [Invalidate a Merchant Token](unlinking-merchanttoken.md)
  Invalidate a merchant token associated with your merchant identifier, making it invalid for future transaction authorizations.
- [object MerchantTokenUnlinkRequest](merchanttokenunlinkrequest.md)
  The request body you use to invalidate a merchant token.
### Error handling
- [object ErrorResponse](errorresponse.md)
  Information about errors that the API returns in the response body whenever an API request is unsuccessful.
### Dictionaries
- [object MerchantMetadata](merchantmetadata.md)
  The metadata of the merchant that updated on the server.
- [object MerchantTokenUsageMetadata](merchanttokenusagemetadata.md)
  Metadata about where and how to retrieve the latest usage information.
- [object RetrieveMerchantTokenPublicKeyRequest](retrievemerchanttokenpublickeyrequest.md)
  Get the merchant token public key request.
- [object RetrieveMerchantTokenPublicKeyResponse](retrievemerchanttokenpublickeyresponse.md)
  Get the merchant token public key response.
- [object UpdateMerchantMetadataRequest](updatemerchantmetadatarequest.md)
  Update the merchant token’s notification metadata.


---

*[View on Apple Developer](https://developer.apple.com/documentation/MerchantTokenNotificationServices)*