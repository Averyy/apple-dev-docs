# Send Consumption Information

**Framework**: App Store Server API  
**Kind**: httpRequest

Send consumption information about a consumable in-app purchase or auto-renewable subscription to the App Store after your server receives a consumption request notification.

**Availability**:
- App Store Server API 1.0+

## Mentions

- [App Store Server API changelog](app-store-server-api-changelog.md)
- [Identifying rate limits](identifying-rate-limits.md)

#### Discussion

The App Store uses a variety of factors to determine if a refund request is approved or denied. To help inform and improve the refund process, you can send information about a user’s consumption of the in-app purchase to the App Store when the user requests a refund. The App Store uses the consumption information you provide to inform its refund decisions.

When a customer initiates a refund request for a consumable in-app purchase or auto-renewable subscription, the App Store sends a `CONSUMPTION_REQUEST` [`notificationType`](https://developer.apple.com/documentation/AppStoreServerNotifications/notificationType) to your server through your [`App Store Server Notifications V2`](https://developer.apple.com/documentation/AppStoreServerNotifications/App-Store-Server-Notifications-V2) endpoint. If the customer provided consent, respond by calling this API and sending the consumption data in the [`ConsumptionRequest`](consumptionrequest.md) to the App Store. If not, don’t respond to the `CONSUMPTION_REQUEST` notification.

Respond within 12 hours of receiving the `CONSUMPTION_REQUEST` notification.

For information about configuring your server to receive App Store server notifications, see [`Enabling App Store Server Notifications`](https://developer.apple.com/documentation/AppStoreServerNotifications/enabling-app-store-server-notifications). For information about initiating refund requests in an app, see any of the refund request methods, including [`beginRefundRequest(in:)`](https://developer.apple.com/documentation/StoreKit/Transaction/beginRefundRequest(in:)-9k0pj), [`beginRefundRequest(for:in:)`](https://developer.apple.com/documentation/StoreKit/Transaction/beginRefundRequest(for:in:)-65tph), [`beginRefundRequest(in:)`](https://developer.apple.com/documentation/StoreKit/Transaction/beginRefundRequest(in:)-63bvd), and [`beginRefundRequest(for:in:)`](https://developer.apple.com/documentation/StoreKit/Transaction/beginRefundRequest(for:in:)-9mscy).

##### Obtain Valid Consent

You must obtain valid consent from the user before sharing their personal data with Apple in the [`Send Consumption Information`](send-consumption-information.md) API. You, the developer, are solely responsible for obtaining valid consent because you’re sharing with Apple the data that you collected from the user.

The requirements to obtain valid consent vary under applicable law, and Apple can’t advise you on specific ways to obtain valid consent. Developers are responsible for determining specific compliance with applicable laws. If your app violates Apple’s guidelines, App Review will reach out and work with you to address any concerns.

Here are some general guidelines to keep in mind for obtaining valid consent:

- Valid consent is freely given, specific, informed, and unambiguous as to a user’s wishes with respect to their personal data.
- As an example, when requesting consent, you may include: clear language that conveys to a user that you will provide Apple with some of their personal data to assist with reviewing the user’s app refund requests; clear language that conveys to users that they can withdraw their consent at any time; and a method for users to give their affirmative consent.
- Opt-in consent is a higher standard for consent than offering an opt-out. Generally, if you don’t offer an individual the opportunity to opt out, it can be difficult to show that consent is freely given.
- After you’ve obtained consent, if there is a change in circumstances causing you to conclude that the user’s consent is no longer valid — for example, due to a change in the way you use or share data, or if the user withdraws consent for this purpose — you should update the [`customerConsented`](customerconsented.md) flag and not send any further data from that user.

> ❗ **Important**:  Don’t use the [`App Tracking Transparency`](https://developer.apple.com/documentation/AppTrackingTransparency) prompt to obtain consent for sharing data with Apple through the [`Send Consumption Information`](send-consumption-information.md) API. Obtaining consent needed to use the [`Send Consumption Information`](send-consumption-information.md) endpoint is unrelated to [`App Tracking Transparency`](https://developer.apple.com/documentation/AppTrackingTransparency). These two features are distinct and unrelated.

 Don’t use the [`App Tracking Transparency`](https://developer.apple.com/documentation/AppTrackingTransparency) prompt to obtain consent for sharing data with Apple through the [`Send Consumption Information`](send-consumption-information.md) API. Obtaining consent needed to use the [`Send Consumption Information`](send-consumption-information.md) endpoint is unrelated to [`App Tracking Transparency`](https://developer.apple.com/documentation/AppTrackingTransparency). These two features are distinct and unrelated.

The data you share with Apple through the [`Send Consumption Information`](send-consumption-information.md) API isn’t used for tracking. You must separately obtain consent from users when sharing data with Apple using the [`Send Consumption Information`](send-consumption-information.md) API.

##### Disclose Data Usage

If you adopt the [`Send Consumption Information`](send-consumption-information.md) API, answer the app privacy questions to disclose in your labels any data you collect from your users and what you’re using it for. For more information about app privacy labels, see [`App privacy details on the App Store`](https://developer.apple.comhttps://developer.apple.com/app-store/app-privacy-details/).

Apple uses and protects the data you share through the [`Send Consumption Information`](send-consumption-information.md) API in accordance with [`Apple’s Privacy Policy`](https://developer.apple.comhttps://www.apple.com/legal/privacy/en-ww/). For additional information about how Apple protects data, see [`Apple Platform Security Guide`](https://developer.apple.comhttps://support.apple.com/guide/security/welcome/web). Apple retains the data you provide through the [`Send Consumption Information`](send-consumption-information.md) API for the period necessary to fulfill the purpose for which the data was collected, which is to improve the refund process by obtaining data that assists with reviewing the customer’s refund request. Apple may share the data you provide through the [`Send Consumption Information`](send-consumption-information.md) API with service providers who act on our behalf, our partners, or others at your direction. Apple will not share the data with third parties for their own marketing purposes. For more information, see [`App Store & Privacy`](https://developer.apple.comhttps://www.apple.com/legal/privacy/data/en/app-store/).

##### Handle Requests to Access or Delete Consumption Data

If your users request access to or deletion of their personal data related to consumption information, inform them that they may submit requests directly to Apple by visiting [`privacy.apple.com`](https://developer.apple.comhttps://privacy.apple.com). If your app stores data in CloudKit on behalf of your users, see [`Responding to Requests to Delete Data`](https://developer.apple.com/documentation/CloudKit/responding-to-requests-to-delete-data), [`Providing User Access to CloudKit Data`](https://developer.apple.com/documentation/CloudKit/providing-user-access-to-cloudkit-data), and [`Changing Access Controls on User Data`](https://developer.apple.com/documentation/CloudKit/changing-access-controls-on-user-data) for more information.

## Request Body

The request body.

## See Also

- [object ConsumptionRequest](consumptionrequest.md)
  The request body containing consumption information.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appstoreserverapi/send-consumption-information)*