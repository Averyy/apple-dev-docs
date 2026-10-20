# FinanceStore.HistoryToken

**Framework**: FinanceKit  
**Kind**: struct  
**Role**: Structure

A structure that describes the starting point to use for financial data queries.

**Availability**:
- iOS 17.4+
- iPadOS 17.4+

## Declaration

```swift
struct HistoryToken
```

#### Overview

The framework returns this as part of a [`FinanceStore.Changes`](./changes.md) instance when iterating over a `History` sequence.

## Topics

### Initializers
- [init(from: any Decoder) throws](./historytoken/init%28from%29.md)
  Initializes a new history token using data from the provided decoder.
### Instance Methods
- [func encode(to: any Encoder) throws](./historytoken/encode%28to%29.md)
  Encodes the history token into the provided encoder.

## Relationships

### Conforms To
- [Decodable](../../Swift/decodable.md)
- [Encodable](../../Swift/encodable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/financekit/financestore/historytoken)*