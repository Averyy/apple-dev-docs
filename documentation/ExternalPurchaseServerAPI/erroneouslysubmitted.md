# erroneouslySubmitted

**Framework**: External Purchase Server API  
**Kind**: typealias

A Boolean value that indicates whether a line item was submitted in error.

**Availability**:
- External Purchase Server API 1.0.0+

## Declaration

```swift
boolean erroneouslySubmitted
```

## Mentions

- [Reporting corrections](reportcorrections.md)

#### Discussion

Only use this field when submitting corrections to a report. Set this field to `true` to indicate that you previously submitted the line item erroneously. This effectively undoes the line item submission. When submitting a correction, set the [`restatement`](restatement.md) field to `true`.

For more information on correcting previously submitted line items, see [`Reporting corrections`](reportcorrections.md).

## See Also

- [type restatement](restatement.md)
  A Boolean value that indicates a line item contains a correction.


---

*[View on Apple Developer](https://developer.apple.com/documentation/externalpurchaseserverapi/erroneouslysubmitted)*