# FinanceStore.HistoryToken

**Framework**: FinanceKit  
**Kind**: struct

A structure that describes the starting point to use for financial data queries.

**Availability**:
- iOS 17.4+
- iPadOS 17.4+

## Declaration

```swift
struct HistoryToken
```

#### Overview

The framework returns this as part of a [`FinanceStore.Changes`](financestore/changes.md) instance when iterating over a `History` sequence.

## Topics

### Initializers
- [init(from: any Decoder) throws](financestore/historytoken/init(from:).md)
  Initializes a new history token using data from the provided decoder.
### Instance Methods
- [func encode(to: any Encoder) throws](financestore/historytoken/encode(to:).md)
  Encodes the history token into the provided encoder.

## Relationships

### Conforms To
- [Decodable](../swift/decodable.md)
- [Encodable](../swift/encodable.md)
- [Sendable](../swift/sendable.md)
- [SendableMetatype](../swift/sendablemetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/financekit/financestore/historytoken)*