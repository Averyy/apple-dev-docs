# Reporting unrecognized tokens and tokens without transactions

**Framework**: External Purchase Server API

Create reports for external purchase tokens that didn’t result in completed transactions, or tokens that you learn of from an App Store server notification.

#### Overview

If a customer doesn’t successfully complete an external purchase, you must still report the token, even if it has no transaction. App Store Server Notifications V2 notifies you of external purchase tokens you haven’t yet reported, 10 days after the system created the token. You need to report the token, including when your system doesn’t have a record of the token.

Send a request to the [`Send External Purchase Report`](send-external-purchase-report.md) endpoint to report all external purchase tokens. Add the following information in the [`ExternalPurchaseReport`](externalpurchasereport.md) request body:

- Supply a [`requestIdentifier`](requestidentifier.md), to uniquely identify the report.
- Provide the [`externalPurchaseId`](externalpurchaseid.md) of the token you’re reporting.

Then, specify the type of report in the [`status`](status.md) field:

- Use `NO_LINE_ITEM` when the external purchase token doesn’t have any associated transactions.
- Use `UNRECOGNIZED_TOKEN` when you receive an App Store server notification with a external purchase token your system doesn’t recognize.

Don’t provide a `lineItems` field in the request body when using either of these status values.

##### Report a Token Without a Completed Transaction

Use the `NO_LINE_ITEM` status to report an external purchase token that didn’t result in any completed transactions. The following example shows the `ExternalPurchaseReport` request body for a token without any associated transactions:

```json
{
    "requestIdentifier": "87e7d6d1-b98d-4a8f-b6a4-41ba992a6cad",
    "externalPurchaseId": "168f34da-19a5-465d-9b1a-fdb0b781b9b9",
    "status": "NO_LINE_ITEM"
}
```

##### Report an Unrecognized Token

Apple sends notifications to your [`App Store Server Notifications V2`](https://developer.apple.com/documentation/AppStoreServerNotifications/App-Store-Server-Notifications-V2) endpoint for external purchase tokens that remain unreported after 10 days. The notification has a [`notificationType`](https://developer.apple.com/documentation/AppStoreServerNotifications/notificationType) of `EXTERNAL_PURCHASE_TOKEN` and a [`subtype`](https://developer.apple.com/documentation/AppStoreServerNotifications/subtype) of `UNREPORTED`. It provides the token’s [`externalPurchaseId`](externalpurchaseid.md) in the [`externalPurchaseToken`](https://developer.apple.com/documentation/AppStoreServerNotifications/externalPurchaseToken) field of notification’s payload.

Compare the `externalPurchaseId` to the tokens in your system. If your system doesn’t have a record of a matching token, use the  `UNRECOGNIZED_TOKEN` [`status`](status.md) to send a report to Apple. The following example shows the [`ExternalPurchaseReport`](externalpurchasereport.md) request body for an unrecognized token:

```json
{
    "requestIdentifier": "94d0d7fb-c393-4813-92eb-9614e7540f6d",
    "externalPurchaseId": "<externalPurchaseId from notification>",
    "status": "UNRECOGNIZED_TOKEN"
}
```


---

*[View on Apple Developer](https://developer.apple.com/documentation/externalpurchaseserverapi/reportwithouttransactions)*