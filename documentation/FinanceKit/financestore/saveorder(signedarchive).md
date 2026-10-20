# saveOrder(signedArchive:)

**Framework**: FinanceKit  
**Kind**: method  
**Role**: Instance Method

Adds an order to the store or updates an existing order.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+

## Declaration

```swift
func saveOrder(signedArchive: Data) async throws -> FinanceStore.SaveOrderResult
```

#### Discussion

`Data` must be the archive data of a valid, signed order.

## See Also

### Orders
- [struct FullyQualifiedOrderIdentifier](../fullyqualifiedorderidentifier.md)
  A structure that specifies the characteristics of an order.


---

*[View on Apple Developer](https://developer.apple.com/documentation/financekit/financestore/saveorder(signedarchive:))*