# requestIdentifier

**Framework**: External Purchase Server API  
**Kind**: typealias

A UUID that uniquely identifies an external purchase report.

**Availability**:
- External Purchase Server API 1.0.0+

## Declaration

```swift
uuid requestIdentifier
```

## Mentions

- [Reporting corrections](reportcorrections.md)
- [Reporting unrecognized tokens and tokens without transactions](reportwithouttransactions.md)

#### Discussion

You generate this identifier when you send a report to the [`Send External Purchase Report`](send-external-purchase-report.md) endpoint. Use the same `requestIdentifier` only if you resubmit a report that previously failed. Use a new `requestIdentifier` for each new report, including for reports that correct line items you previously submitted successfully.

Use the `requestIdentifier` to get the report from the [`Retrieve External Purchase Report`](retrieve-external-purchase-report.md) endpoint.

## See Also

- [type externalPurchaseId](externalpurchaseid.md)
  The unique identifier of an external purchase token.
- [type status](status.md)
  A string value that represents the status of the token and the contents of the external purchase report.


---

*[View on Apple Developer](https://developer.apple.com/documentation/externalpurchaseserverapi/requestidentifier)*