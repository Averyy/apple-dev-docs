# externalPurchaseId

**Framework**: External Purchase Server API  
**Kind**: typealias

The unique identifier of an external purchase token.

**Availability**:
- External Purchase Server API 1.0.0+

## Declaration

```swift
string externalPurchaseId
```

## Mentions

- [Reporting unrecognized and transactionless tokens](reportwithouttransactions.md)

#### Discussion

Decode an external purchase token to get its [`externalPurchaseId`](externalpurchaseid.md). For more information, see [`Receiving and decoding external purchase tokens`](https://developer.apple.com/documentation/StoreKit/receiving-and-decoding-external-purchase-tokens).

## See Also

- [type requestIdentifier](requestidentifier.md)
  A UUID that uniquely identifies an external purchase report.
- [type status](status.md)
  A string value you provide to indicate the status of the token and the contents of the external purchase report.


---

*[View on Apple Developer](https://developer.apple.com/documentation/externalpurchaseserverapi/externalpurchaseid)*