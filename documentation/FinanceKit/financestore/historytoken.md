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

## Topics

### Initializers
- [init(from: any Decoder) throws](financestore/historytoken/init(from:).md)
  Initializes a new history token using data from the provided decoder.
### Instance Methods
- [func encode(to: any Encoder) throws](financestore/historytoken/encode(to:).md)
  Persists a the  history token data using  the provided encoder.

## Relationships

### Conforms To
- [Decodable](../Swift/Decodable.md)
- [Encodable](../Swift/Encodable.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [struct FullyQualifiedOrderIdentifier](fullyqualifiedorderidentifier.md)
  A structure that specifies the characteristics of an order.
- [func saveOrder(signedArchive: Data) async throws -> FinanceStore.SaveOrderResult](financestore/saveorder(signedarchive:).md)
  Adds an order to the store or updates an existing order.


---

*[View on Apple Developer](https://developer.apple.com/documentation/financekit/financestore/historytoken)*