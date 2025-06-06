# FullyQualifiedOrderIdentifier

**Framework**: FinanceKit  
**Kind**: struct

A structure that specifies the characteristics of an order.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+

## Declaration

```swift
struct FullyQualifiedOrderIdentifier
```

## Topics

### Operators
- [static func == (FullyQualifiedOrderIdentifier, FullyQualifiedOrderIdentifier) -> Bool](fullyqualifiedorderidentifier/==(_:_:).md)
  Returns a Boolean value indicating whether two values are equal.
### Initializers
- [init(from: any Decoder) throws](fullyqualifiedorderidentifier/init(from:).md)
  Creates a new instance by decoding from the given decoder.
- [init(orderTypeIdentifier: String, orderIdentifier: String)](fullyqualifiedorderidentifier/init(ordertypeidentifier:orderidentifier:).md)
  Initializes the object with values that uniquely identify an order within an order type.
### Instance Properties
- [var hashValue: Int](fullyqualifiedorderidentifier/hashvalue.md)
  The hash value.
- [var orderIdentifier: String](fullyqualifiedorderidentifier/orderidentifier.md)
  A string the merchant uses to identify a specific customer order.
- [var orderTypeIdentifier: String](fullyqualifiedorderidentifier/ordertypeidentifier.md)
  A string that describes the order type.
### Instance Methods
- [func encode(to: any Encoder) throws](fullyqualifiedorderidentifier/encode(to:).md)
  Encodes this value into the given encoder.
- [func hash(into: inout Hasher)](fullyqualifiedorderidentifier/hash(into:).md)
  Hashes the essential components of this value by feeding them into the given hasher.
### Default Implementations
- [CustomStringConvertible Implementations](fullyqualifiedorderidentifier/customstringconvertible-implementations.md)
- [Equatable Implementations](fullyqualifiedorderidentifier/equatable-implementations.md)

## Relationships

### Conforms To
- [Copyable](../Swift/Copyable.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Decodable](../Swift/Decodable.md)
- [Encodable](../Swift/Encodable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [FinanceStore.HistoryToken](financestore/historytoken.md)
  A structure that describes the starting point to use for financial data queries.
- [func saveOrder(signedArchive: Data) async throws -> FinanceStore.SaveOrderResult](financestore/saveorder(signedarchive:).md)
  Adds an order to the store or updates an existing order.


---

*[View on Apple Developer](https://developer.apple.com/documentation/financekit/fullyqualifiedorderidentifier)*