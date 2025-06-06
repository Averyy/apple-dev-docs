# creationDate

**Framework**: External Purchase Server API  
**Kind**: typealias

The UNIX date, in milliseconds, that the customer authorized the transaction.

**Availability**:
- External Purchase Server API 1.0.0+

## Declaration

```swift
int64 creationDate
```

#### Discussion

For refunds and other events, use the UNIX date, in milliseconds, of the transaction.

## See Also

- [type eventType](eventtype.md)
  The type of transaction the line item reports, whether it’s a buy or refund.
- [type referenceLineItemId](referencelineitemid.md)
  The line item identifier of another transaction, that the report  references.


---

*[View on Apple Developer](https://developer.apple.com/documentation/externalpurchaseserverapi/creationdate)*