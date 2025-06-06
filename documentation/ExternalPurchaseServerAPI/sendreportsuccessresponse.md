# SendReportSuccessResponse

**Framework**: External Purchase Server API  
**Kind**: dictionary

A response that contains the request identifier and indicates the server successfully received your external purchase report.

**Availability**:
- External Purchase Server API 1.0.0+

## Declaration

```swift
object SendReportSuccessResponse
```

#### Discussion

The [`Send External Purchase Report`](send-external-purchase-report.md) endpoint returns this response when the server successfully receives a report that passes validation checks. Record the [`requestIdentifier`](requestidentifier.md) in your system. Use the  `requestIdentifer` to get the report by sending a request to the [`Retrieve External Purchase Report`](retrieve-external-purchase-report.md) endpoint.

## See Also

- [Send External Purchase Report](send-external-purchase-report.md)
  Report required information about external purchase tokens and associated transactions.
- [object ExternalPurchaseReport](externalpurchasereport.md)
  The contents of an external purchase report for a single token.
- [object SendReportErrorResponse](sendreporterrorresponse.md)
  An error response that indicates your external purchase report didn’t succeed, including error details for the line items in your report.


---

*[View on Apple Developer](https://developer.apple.com/documentation/externalpurchaseserverapi/sendreportsuccessresponse)*