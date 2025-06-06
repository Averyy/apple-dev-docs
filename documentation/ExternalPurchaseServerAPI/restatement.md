# restatement

**Framework**: External Purchase Server API  
**Kind**: typealias

A Boolean value that indicates a line item contains a correction.

**Availability**:
- External Purchase Server API 1.0.0+

## Declaration

```swift
boolean restatement
```

## Mentions

- [Reporting corrections](reportcorrections.md)

#### Discussion

Set this value to `true` to indicate the line item is restating a previously submitted line item, and contains corrections.

> ❗ **Important**: Restated line items overwrite the previous submission with the same [`lineItemId`](lineitemid.md). Be sure to include all the data in the line item, even those fields that are unchanged from the original.

Restated line items overwrite the previous submission with the same [`lineItemId`](lineitemid.md). Be sure to include all the data in the line item, even those fields that are unchanged from the original.

To report erroneously submitted line items, set both the `restatement` and [`erroneouslySubmitted`](erroneouslysubmitted.md) fields to `true`.

For more information on correcting previously submitted line items, see [`Reporting corrections`](reportcorrections.md).

## See Also

- [type erroneouslySubmitted](erroneouslysubmitted.md)
  A Boolean value that indicates whether a line item was submitted in error.


---

*[View on Apple Developer](https://developer.apple.com/documentation/externalpurchaseserverapi/restatement)*