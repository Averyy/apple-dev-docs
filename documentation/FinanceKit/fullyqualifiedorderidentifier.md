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

### Initializers
- [init(orderTypeIdentifier: String, orderIdentifier: String)](fullyqualifiedorderidentifier/init(ordertypeidentifier:orderidentifier:).md)
  Initializes the object with values that uniquely identify an order within an order type.
### Instance Properties
- [var orderIdentifier: String](fullyqualifiedorderidentifier/orderidentifier.md)
  A string the merchant uses to identify a specific customer order.
- [var orderTypeIdentifier: String](fullyqualifiedorderidentifier/ordertypeidentifier.md)
  A string that describes the order type.

## Relationships

### Conforms To
- [Copyable](../swift/copyable.md)
- [CustomStringConvertible](../swift/customstringconvertible.md)
- [Decodable](../swift/decodable.md)
- [Encodable](../swift/encodable.md)
- [Equatable](../swift/equatable.md)
- [Escapable](../swift/escapable.md)
- [Hashable](../swift/hashable.md)
- [Sendable](../swift/sendable.md)
- [SendableMetatype](../swift/sendablemetatype.md)

## See Also

- [func saveOrder(signedArchive: Data) async throws -> FinanceStore.SaveOrderResult](financestore/saveorder(signedarchive:).md)
  Adds an order to the store or updates an existing order.


---

*[View on Apple Developer](https://developer.apple.com/documentation/financekit/fullyqualifiedorderidentifier)*