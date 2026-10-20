# FullyQualifiedOrderIdentifier

**Framework**: FinanceKit  
**Kind**: struct  
**Role**: Structure

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
- [init(orderTypeIdentifier: String, orderIdentifier: String)](./fullyqualifiedorderidentifier/init%28ordertypeidentifier,orderidentifier%29.md)
  Initializes the object with values that uniquely identify an order within an order type.
### Instance Properties
- [var orderIdentifier: String](./fullyqualifiedorderidentifier/orderidentifier.md)
  A string the merchant uses to identify a specific customer order.
- [var orderTypeIdentifier: String](./fullyqualifiedorderidentifier/ordertypeidentifier.md)
  A string that describes the order type.

## Relationships

### Conforms To
- [Copyable](../Swift/copyable.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Decodable](../Swift/decodable.md)
- [Encodable](../Swift/encodable.md)
- [Equatable](../Swift/equatable.md)
- [Escapable](../Swift/escapable.md)
- [Hashable](../Swift/hashable.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Orders
- [func saveOrder(signedArchive: Data) async throws -> FinanceStore.SaveOrderResult](./financestore/saveorder%28signedarchive%29.md)
  Adds an order to the store or updates an existing order.


---

*[View on Apple Developer](https://developer.apple.com/documentation/financekit/fullyqualifiedorderidentifier)*