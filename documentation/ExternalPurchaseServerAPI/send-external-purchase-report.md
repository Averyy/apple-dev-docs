# Send External Purchase Report

**Framework**: External Purchase Server API  
**Kind**: httpRequest

Report required information about external purchase tokens and associated transactions.

**Availability**:
- External Purchase Server API 1.0.0+

## Mentions

- [Reporting corrections](reportcorrections.md)
- [Reporting unrecognized and transactionless tokens](reportwithouttransactions.md)
- [Reporting tokens with transactions](reportwithtransactions.md)

#### Discussion

Call this endpoint to report an external purchase token that your app or website receives, and the transactions and events associated with the token. For information on the reporting requirements, see the [`Commission, transaction reports, and payments`](https://developer.apple.comhttps://developer.apple.com/support/apps-using-alternative-payment-providers-in-the-eu#commission-reports-and-payments) section of the article Using alternative payment options on the App Store in the European Union.

To send the report, add your data to the [`ExternalPurchaseReport`](externalpurchasereport.md) request body. For more information about creating reports, see the following:

- [`Reporting tokens with transactions`](reportwithtransactions.md)
- [`Reporting unrecognized and transactionless tokens`](reportwithouttransactions.md)
- [`Reporting corrections`](reportcorrections.md)

The server indicates it successfully received your report by returning an `HTTP 200` response with your [`requestIdentifier`](requestidentifier.md) in the [`SendReportSuccessResponse`](sendreportsuccessresponse.md). If you receive an `HTTP 400` error response with a [`SendReportErrorResponse`](sendreporterrorresponse.md) object, the server didn’t successfully receive any of the data in the report. Fix the errors listed in the response object, and resubmit the full report using the same [`requestIdentifier`](requestidentifier.md). The server also sends an `HTTP 400` error if the request is a duplicate, or if it’s malformed.

##### Testing in the Sandbox Environment

Call this endpoint using its sandbox URL only for tokens that the system generates in the sandbox environment. For more information about identifying sandbox tokens, see [`Receiving and decoding external purchase tokens`](https://developer.apple.com/documentation/StoreKit/receiving-and-decoding-external-purchase-tokens).

> ❗ **Important**: The sandbox tokens and any test transaction data you submit through the sandbox URLs of the External Purchase Server API are not actual transactions.

## Request Body

The request body that contains the report information.

## See Also

- [object ExternalPurchaseReport](externalpurchasereport.md)
  The contents of an external purchase report for a single token.
- [object SendReportSuccessResponse](sendreportsuccessresponse.md)
  A response that contains the request identifier and indicates the server successfully received your external purchase report.
- [object SendReportErrorResponse](sendreporterrorresponse.md)
  An error response that indicates your external purchase report didn’t succeed, including error details for the line items in your report.


---

*[View on Apple Developer](https://developer.apple.com/documentation/externalpurchaseserverapi/send-external-purchase-report)*