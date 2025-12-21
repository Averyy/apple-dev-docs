# External Purchase Server API

**Framework**: External Purchase Server API  
**Kind**: module

Send and manage reports you send to Apple for tokens you receive when your app provides external purchases for digital goods and services.

**Availability**:
- External Purchase Server API 1.0.0+

#### Overview

Call this REST API from your server to report external purchase tokens and your customers’ transactions related to the tokens. Use this API if your app uses [`External Purchase`](https://developer.apple.com/documentation/StoreKit/external-purchase) API and provides alternative payment options for digital goods and services, using any of the following:

- : An alternative payment processor that lets customers complete transactions within your app.
- : Directing customers to complete a transaction for digital goods and services on your external website, or a distribution channel of your choice.

Report all tokens, including those that didn’t result in a transaction, and report the transactions associated with the tokens. For more information on the reporting requirements, including scope and report timing expectations, see the [`Commission, transaction reports, and payments`](https://developer.apple.comhttps://developer.apple.com/support/apps-using-alternative-payment-providers-in-the-eu#commission-reports-and-payments) section of the article Using alternative payment options on the App Store in the European Union.

##### Authorize Your Api Calls

Calls to the API require JSON Web Tokens (JWTs) for authorization. Get keys to create JWTs from your organization’s App Store Connect account. See [`Creating API keys to authorize API requests`](https://developer.apple.com/documentation/AppStoreServerAPI/creating-api-keys-to-authorize-api-requests) to create your keys. See [`Generating JSON Web Tokens for API requests`](https://developer.apple.com/documentation/AppStoreServerAPI/generating-json-web-tokens-for-api-requests) to generate tokens using your keys, and send API requests.

##### Report External Purchase Tokens and Transactions

When customers initiate an external purchase, your app or website receives a token. You need to report the token and the transactions associated with the token. For more information on how you receive tokens, see [`Receiving and decoding external purchase tokens`](https://developer.apple.com/documentation/StoreKit/receiving-and-decoding-external-purchase-tokens). To send a report, call the [`Send External Purchase Report`](send-external-purchase-report.md) endpoint for each token. Send reports in all of the following cases:

- To report a token, with line items, when a customer completes one or more transactions.
- To report a token, without line items, when a customer doesn’t complete any transactions.
- To report an unrecognized token, when you receive an App Store Server Notification about a token that you don’t have recorded in your system.
- To report duplicate `ACQUISITION` and `SERVICES` tokens.

For more information, see [`Reporting tokens with transactions`](reportwithtransactions.md) and [`Reporting unrecognized and transactionless tokens`](reportwithouttransactions.md).

If you successfully send a report that you later find to be incorrect, you need to correct your submission. For more information, see [`Reporting corrections`](reportcorrections.md).

##### Retrieve Reports

Call the [`Retrieve External Purchase Report`](retrieve-external-purchase-report.md) endpoint to get reports you previously sent to Apple. Specify which report to retrieve by using the same `requestIdentifier` value that you provide when you send the report.

##### Receive Notifications for Unreported Tokens

The App Store server sends an `EXTERNAL_PURCHASE_TOKEN` [`notificationType`](https://developer.apple.com/documentation/AppStoreServerNotifications/notificationType) to your [`App Store Server Notifications V2`](https://developer.apple.com/documentation/AppStoreServerNotifications/App-Store-Server-Notifications-V2) endpoint in the following cases:

- To indicate unreported tokens, using the UNREPORTED subtype
- To remind you of active custom link tokens, using the ACTIVE_TOKEN_REMINDER subtype.

If you receive the `EXTERNAL_PURCHASE_TOKEN` notification, send a report for the token the notification specifies. To check for notifications you might have missed — for example, due to a server outage — send a request to the [`Get Notification History`](https://developer.apple.com/documentation/AppStoreServerAPI/Get-Notification-History) endpoint to get a list of notifications that App Store Server Notifications attempted to send to your server.

For more information on notifications, see [`Enabling App Store Server Notifications`](https://developer.apple.com/documentation/AppStoreServerNotifications/enabling-app-store-server-notifications). Configure the [`App Store Server Notifications V2`](https://developer.apple.com/documentation/AppStoreServerNotifications/App-Store-Server-Notifications-V2) endpoint on your server to receive version 2 notifications.

##### Test Using the Sandbox Environment

When you test your app in the sandbox environment, the [`External Purchase`](https://developer.apple.com/documentation/StoreKit/external-purchase) API returns tokens that are valid only in that environment. These tokens have an `externalPurchaseId` that starts with the string “`SANDBOX`”. To test your server’s token reporting implementation, send reports for sandbox tokens to the Sandbox URL of the [`Send External Purchase Report`](send-external-purchase-report.md) endpoint.

> ❗ **Important**: External purchase tokens generated in the sandbox environment are for testing only. The sandbox tokens and any test transaction data you submit through the sandbox URLs of the External Purchase Server API are not actual transactions.

## Topics

### Essentials
- [Creating API keys to authorize API requests](../AppStoreServerAPI/creating-api-keys-to-authorize-api-requests.md)
  Create API keys you use to sign JSON Web Tokens and authorize API requests.
- [Generating JSON Web Tokens for API requests](../AppStoreServerAPI/generating-json-web-tokens-for-api-requests.md)
  Create JSON Web Tokens signed with your private key to authorize requests for App Store Server API and External Purchase Server API.
- [External Purchase Server API changelog](changelog.md)
  Learn about new features and updates in the External Purchase Server API.
### External purchase tokens
- [Receiving and decoding external purchase tokens](../StoreKit/receiving-and-decoding-external-purchase-tokens.md)
  Receive tokens for external purchases that you use to report transactions to Apple.
### External purchase reporting
- [Send External Purchase Report](send-external-purchase-report.md)
  Report required information about external purchase tokens and associated transactions.
- [object ExternalPurchaseReport](externalpurchasereport.md)
  The contents of an external purchase report for a single token.
- [object SendReportSuccessResponse](sendreportsuccessresponse.md)
  A response that contains the request identifier and indicates the server successfully received your external purchase report.
- [object SendReportErrorResponse](sendreporterrorresponse.md)
  An error response that indicates your external purchase report didn’t succeed, including error details for the line items in your report.
### External purchase report transactions
- [Reporting tokens with transactions](reportwithtransactions.md)
  Create reports for external purchase tokens that result in completed transactions, including one-time charges, subscriptions and renewals, and refunds.
- [Reporting corrections](reportcorrections.md)
  Submit a report with corrections if you find errors in, or have adjustments to, a successfully submitted transaction.
- [object OneTimeBuyLineItem](onetimebuylineitem.md)
  The line item that indicates a one-time charge transaction.
- [object RefundLineItem](refundlineitem.md)
  The line item that indicates a refund transaction.
- [object SubscriptionBuyLineItem](subscriptionbuylineitem.md)
  The line item that indicates a subscription-related event or transaction.
- [Line item fields](lineitems.md)
  Properties that describe a single transaction or correction in an external purchase report.
### External purchase report without transactions
- [Reporting unrecognized and transactionless tokens](reportwithouttransactions.md)
  Create reports for external purchase tokens that didn’t result in completed transactions, duplicate tokens, or tokens that you learn of from an App Store server notification.
### External purchase report retrieval
- [Retrieve External Purchase Report](retrieve-external-purchase-report.md)
  Get an external purchase report by providing its request identifier.
- [object RetrieveReportSuccessResponse](retrievereportsuccessresponse.md)
  A response that indicates success and includes your external purchase report data.
### Error handling
- [Error messages and codes](errorcodes.md)
  Error messages and codes for reports and endpoints.


---

*[View on Apple Developer](https://developer.apple.com/documentation/ExternalPurchaseServerAPI)*