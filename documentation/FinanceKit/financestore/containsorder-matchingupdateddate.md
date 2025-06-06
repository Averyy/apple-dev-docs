# containsOrder(matching:updatedDate:)

**Framework**: FinanceKit  
**Kind**: method

Checks whether the finance store contains an order.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+

## Declaration

```swift
func containsOrder(matching fqoid: FullyQualifiedOrderIdentifier, updatedDate: Date? = nil) async throws -> FinanceStore.ContainsOrderResult
```

#### Discussion

This returns `.notFound` for any orders that the process isn’t entitled to access.


---

*[View on Apple Developer](https://developer.apple.com/documentation/financekit/financestore/containsorder(matching:updateddate:))*