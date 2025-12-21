# status

**Framework**: External Purchase Server API  
**Kind**: typealias

A string value you provide to indicate the status of the token and the contents of the external purchase report.

**Availability**:
- External Purchase Server API 1.0.0+

## Declaration

```swift
string status
```

## Mentions

- [Reporting unrecognized and transactionless tokens](reportwithouttransactions.md)
- [External Purchase Server API changelog](changelog.md)

#### Discussion

The [`status`](status.md) property indicates whether the token you’re reporting has any associated transactions. You provide this property in the [`ExternalPurchaseReport`](externalpurchasereport.md) request body when you call the [`Send External Purchase Report`](send-external-purchase-report.md) endpoint.

## See Also

- [type requestIdentifier](requestidentifier.md)
  A UUID that uniquely identifies an external purchase report.
- [type externalPurchaseId](externalpurchaseid.md)
  The unique identifier of an external purchase token.


---

*[View on Apple Developer](https://developer.apple.com/documentation/externalpurchaseserverapi/status)*