# Send Consumption Information

**Framework**: App Store Server API  
**Kind**: httpRequest  
**Role**: Web Service Endpoint

Send consumption information about an In-App Purchase to the App Store after your server receives a consumption request notification.

**Availability**:
- App Store Server API 1.19+

## Mentions

- [App Store Server API changelog](./app-store-server-api-changelog.md)
- [Identifying rate limits](./identifying-rate-limits.md)

## Discussion

The App Store uses a variety of factors to determine if a refund request is approved or denied. To help inform and improve the refund process, you can send information about a customer’s consumption of the In-App Purchase to the App Store when the customer requests a refund. The App Store uses the consumption information you provide to inform its refund decisions.

When a customer initiates a refund request for any product type (consumable, non-consumable, non-renewing subscription, or auto-renewable subscription), the App Store sends a `CONSUMPTION_REQUEST` [`notificationType`](../AppStoreServerNotifications/notificationtype.md) to your server through your [`App Store Server Notifications V2`](../AppStoreServerNotifications/app-store-server-notifications-v2.md) endpoint. If the customer provided consent, respond by calling this API and sending the consumption data in the [`ConsumptionRequest`](./consumptionrequest.md) to the App Store. If not, don’t respond to the `CONSUMPTION_REQUEST` notification.

Respond within 12 hours of receiving the `CONSUMPTION_REQUEST` notification.

For information about configuring your server to receive App Store server notifications, see [Enabling App Store Server Notifications](../AppStoreServerNotifications/enabling-app-store-server-notifications.md). For information about initiating refund requests in an app, see any of the refund request methods, including [`beginRefundRequest(in:)`](../StoreKit/transaction/beginrefundrequest%28in%29-9k0pj.md), [`beginRefundRequest(for:in:)`](../StoreKit/transaction/beginrefundrequest%28for,in%29-65tph.md), [`beginRefundRequest(in:)`](../StoreKit/transaction/beginrefundrequest%28in%29-63bvd.md), and [`beginRefundRequest(for:in:)`](../StoreKit/transaction/beginrefundrequest%28for,in%29-9mscy.md).

### Obtain valid consent

You must obtain valid consent from the customer before sharing their personal data with Apple in the [`Send Consumption Information`](./send-consumption-information.md) API. You, the developer, are solely responsible for obtaining valid consent because you’re sharing with Apple the data that you collected from the customer.

The requirements to obtain valid consent vary under applicable law, and Apple can’t advise you on specific ways to obtain valid consent. Developers are responsible for determining specific compliance with applicable laws. If your app violates Apple’s guidelines, App Review will reach out and work with you to address any concerns.

Here are some general guidelines to keep in mind for obtaining valid consent:

- Valid consent is freely given, specific, informed, and unambiguous as to a customer’s wishes with respect to their personal data.
- As an example, when requesting consent, you may include: clear language that conveys to a customer that you will provide Apple with some of their personal data to assist with reviewing the customer’s app refund requests; clear language that conveys to customers that they can withdraw their consent at any time; and a method for customers to give their affirmative consent.
- Opt-in consent is a higher standard for consent than offering an opt-out. Generally, if you don’t offer an individual the opportunity to opt out, it can be difficult to show that consent is freely given.
- After you’ve obtained consent, if there is a change in circumstances causing you to conclude that the customer’s consent is no longer valid — for example, due to a change in the way you use or share data, or if the customer withdraws consent for this purpose — you should update the [`customerConsented`](./customerconsented.md) flag and not send any further data from that customer.

> ❗ **Important**:  Don’t use the [App Tracking Transparency](../AppTrackingTransparency/AppTrackingTransparency.md) prompt to obtain consent for sharing data with Apple through the [`Send Consumption Information`](./send-consumption-information.md) API. Obtaining consent needed to use the [`Send Consumption Information`](./send-consumption-information.md) endpoint is unrelated to [App Tracking Transparency](../AppTrackingTransparency/AppTrackingTransparency.md). These two features are distinct and unrelated.

The data you share with Apple through the [`Send Consumption Information`](./send-consumption-information.md) API isn’t used for tracking. You must separately obtain consent from customers when sharing data with Apple using the [`Send Consumption Information`](./send-consumption-information.md) API.

### Disclose data usage

If you adopt the [`Send Consumption Information`](./send-consumption-information.md) API, answer the app privacy questions to disclose in your labels any data you collect from your customers and what you’re using it for. For more information about app privacy labels, see [App privacy details on the App Store](https://developer.apple.com/app-store/app-privacy-details/).

Apple uses and protects the data you share through the [`Send Consumption Information`](./send-consumption-information.md) API in accordance with [Apple’s Privacy Policy](https://www.apple.com/legal/privacy/en-ww/). For additional information about how Apple protects data, see [Apple Platform Security Guide](https://support.apple.com/guide/security/welcome/web). Apple retains the data you provide through the [`Send Consumption Information`](./send-consumption-information.md) API for the period necessary to fulfill the purpose for which the data was collected, which is to improve the refund process by obtaining data that assists with reviewing the customer’s refund request. Apple may share the data you provide through the [`Send Consumption Information`](./send-consumption-information.md) API with service providers who act on our behalf, our partners, or others at your direction. Apple will not share the data with third parties for their own marketing purposes. For more information, see [App Store & Privacy](https://www.apple.com/legal/privacy/data/en/app-store/).

### Handle requests to access or delete consumption data

If your customers request access to or deletion of their personal data related to consumption information, inform them that they may submit requests directly to Apple by visiting [privacy.apple.com](https://privacy.apple.com). If your app stores data in CloudKit on behalf of your customers, see [Responding to Requests to Delete Data](../CloudKit/responding-to-requests-to-delete-data.md), [Providing User Access to CloudKit Data](../CloudKit/providing-user-access-to-cloudkit-data.md), and [Changing Access Controls on User Data](../CloudKit/changing-access-controls-on-user-data.md) for more information.

## Endpoint

`PUT https://api.storekit-sandbox.apple.com/inApps/v2/transactions/consumption/{transactionId}`

## Parameters

### Path Parameters

- `transactionId` (transactionId) *(required)*: The transaction identifier for which you’re providing consumption information. You receive this identifier in the `CONSUMPTION_REQUEST` notification the App Store sends to your server’s [`App Store Server Notifications V2`](../AppStoreServerNotifications/app-store-server-notifications-v2.md) endpoint.

## Request Body

**Content-Type**: `application/json`  
**Type**: `ConsumptionRequest`

The request body.

## Responses

- `202` Accepted: The App Store server received the consumption information.
- `400` Bad Request (`(InvalidTransactionIdError | FamilyTransactionNotSupportedError | AppTransactionIdNotSupportedError | InvalidCustomerConsentedError | InvalidDeliveryStatusError | InvalidSampleContentProvidedError | InvalidRefundPreferenceError | ConsumptionPercentageOutOfRangeError | UndeliveredConsumptionPercentageNonZeroError | ConsumptionPercentageAutoRenewableSubscriptionError | AdvancedCommerceTransactionNotSupportedError | InvalidAssignedTransactionNotSupportedError)`, `application/json`): Invalid request. See the error code for more information. If there’s no error code, the request is malformed.
- `401` Unauthorized: The JSON Web Token (JWT) in the authorization header is invalid. For more information, see [Generating JSON Web Tokens for API requests](./generating-json-web-tokens-for-api-requests.md).
- `404` Not Found (`TransactionIdNotFoundError`, `application/json`): The transaction identifier wasn’t found.
- `429` (`RateLimitExceededError`, `application/json`): The request exceeded the rate limit. For more information, see [Identifying rate limits](./identifying-rate-limits.md).
- `500` Internal Server Error (`GeneralInternalError`, `application/json`): Server error. Try again later.

## See Also

### Consumption information
- [object ConsumptionRequest](./consumptionrequest.md)
  The request body that contains consumption information for an In-App Purchase.
- [Send Consumption Information V1](./send-consumption-information-v1.md)
  Send consumption information about a consumable In-App Purchase or auto-renewable subscription to the App Store after your server receives a consumption request notification.
- [object ConsumptionRequestV1](./consumptionrequestv1.md)
  The request body containing consumption information.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreserverapi/send-consumption-information)*