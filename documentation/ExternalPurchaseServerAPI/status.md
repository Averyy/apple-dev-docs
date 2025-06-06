# status

**Framework**: External Purchase Server API  
**Kind**: typealias

A string value that represents the status of the token and the contents of the external purchase report.

**Availability**:
- External Purchase Server API 1.0.0+

## Declaration

```swift
string status
```

## Mentions

- [Reporting unrecognized tokens and tokens without transactions](reportwithouttransactions.md)

#### Discussion

Allowed values: `LINE_ITEM`, `NO_LINE_ITEM`, `UNRECOGNIZED_TOKEN`

This value is a property you provide in the [`ExternalPurchaseReport`](externalpurchasereport.md) request body when you call the [`Send External Purchase Report`](send-external-purchase-report.md) endpoint. The [`status`](status.md) indicates whether the token has any associated transactions. Include a status value as follows:

- Use `LINE_ITEM` when your external purchase report includes line items to report transactions.
- Use `NO_LINE_ITEM` to report that your app or website received an external purchase token, but the customer didn’t complete any transactions related to the token.
- Use `UNRECOGNIZED_TOKEN` to report that you’ve received an App Store Server Notification about an external purchase token assigned to your app, but your system doesn’t recognize the token.

## See Also

- [type requestIdentifier](requestidentifier.md)
  A UUID that uniquely identifies an external purchase report.
- [type externalPurchaseId](externalpurchaseid.md)
  The unique identifier of an external purchase token.


---

*[View on Apple Developer](https://developer.apple.com/documentation/externalpurchaseserverapi/status)*