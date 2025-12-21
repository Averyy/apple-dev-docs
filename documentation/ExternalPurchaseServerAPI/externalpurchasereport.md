# ExternalPurchaseReport

**Framework**: External Purchase Server API  
**Kind**: dictionary

The contents of an external purchase report for a single token.

**Availability**:
- External Purchase Server API 1.0.0+

## Declaration

```swift
object ExternalPurchaseReport
```

## Mentions

- [Reporting tokens with transactions](reportwithtransactions.md)
- [Reporting unrecognized and transactionless tokens](reportwithouttransactions.md)
- [External Purchase Server API changelog](changelog.md)
- [Reporting corrections](reportcorrections.md)

#### Discussion

This object is the request body for the [`Send External Purchase Report`](send-external-purchase-report.md) endpoint. Populate this object with data about a single external purchase token that you’re reporting, including its transactions. The [`Retrieve External Purchase Report`](retrieve-external-purchase-report.md) endpoint also returns this object when you request a report you previously successfully submitted.

The `requestIdentifier` field identifies the report. Generate a UUID for each report you send.

> 💡 **Tip**: Store the [`requestIdentifier`](requestidentifier.md) value in your records with the external purchase token to identify your reports.

The [`externalPurchaseId`](externalpurchaseid.md) field is the token’s identifier. To get that value, decode the external purchase token you receive in your app or on your website. For more information, see [`Receiving and decoding external purchase tokens`](https://developer.apple.com/documentation/StoreKit/receiving-and-decoding-external-purchase-tokens).

The [`status`](status.md) field represents the token’s status, which you provide to indicate the report’s contents and whether it includes a `lineItems` array. The [`status`](status.md) value determines the type of report you send:

- Use a `LINE_ITEM` status to report a token with transactions that you list in the `lineItems` array.  Use this status when a token has associated transactions, and to send corrections to previously submitted line items. For more information, see [`Reporting tokens with transactions`](reportwithtransactions.md).
- Use a `NO_LINE_ITEM` status for a report of a token that didn’t result in any successful transactions. Don’t include `lineItems` in the request with this status.  For more information, see [`Reporting unrecognized and transactionless tokens`](reportwithouttransactions.md).
- Use an `UNRECOGNIZED_TOKEN` status to report a token you receive in an App Store Server Notification, but that you don’t have recorded in your system. Don’t include `lineItems` in the request with this status. For more information, see [`Reporting unrecognized and transactionless tokens`](reportwithouttransactions.md).
- Use a `DUPLICATE_TOKEN` status to report a `SERVICES` or `ACQUISITION` token that you recognize, but which you aren’t using to report transactions because it’s a duplicate token. Don’t include `lineItems` in the request with this status. For more information, see [`Reporting unrecognized and transactionless tokens`](reportwithouttransactions.md).

You can also submit corrections to restate line items, or retract a previous submission. For more information, see [`Reporting corrections`](reportcorrections.md).

A line item represents each transaction for the token identified by the `externalPurchaseId`. There are three types of line items:

- [`OneTimeBuyLineItem`](onetimebuylineitem.md), for one-time charges
- [`RefundLineItem`](refundlineitem.md), for refunds
- [`SubscriptionBuyLineItem`](subscriptionbuylineitem.md), for auto-renewable subscription events and transactions

Include as many line items as there are transactions that apply to the token. If your system completes new transactions after you successfully submit a report for a token, send a new report for the token with the new transactions.

## Topics

### Data types
- [type requestIdentifier](requestidentifier.md)
  A UUID that uniquely identifies an external purchase report.
- [type externalPurchaseId](externalpurchaseid.md)
  The unique identifier of an external purchase token.
- [type status](status.md)
  A string value you provide to indicate the status of the token and the contents of the external purchase report.

## See Also

- [Send External Purchase Report](send-external-purchase-report.md)
  Report required information about external purchase tokens and associated transactions.
- [object SendReportSuccessResponse](sendreportsuccessresponse.md)
  A response that contains the request identifier and indicates the server successfully received your external purchase report.
- [object SendReportErrorResponse](sendreporterrorresponse.md)
  An error response that indicates your external purchase report didn’t succeed, including error details for the line items in your report.


---

*[View on Apple Developer](https://developer.apple.com/documentation/externalpurchaseserverapi/externalpurchasereport)*