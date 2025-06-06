# PKDeferredPaymentSummaryItem

**Framework**: PassKit (Apple Pay and Wallet)  
**Kind**: class

An object that defines a summary item for a payment that occurs at a later date, such as a pre-order.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- visionOS 1.0+
- watchOS 8.0+

## Declaration

```swift
class PKDeferredPaymentSummaryItem
```

## Topics

### Setting the payment date
- [var deferredDate: Date](pkdeferredpaymentsummaryitem/deferreddate.md)
  The date, in the future, of the payment.

## Relationships

### Inherits From
- [PKPaymentSummaryItem](pkpaymentsummaryitem.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [var deferredBilling: PKDeferredPaymentSummaryItem](pkdeferredpaymentrequest/deferredbilling.md)
  An object that contains details about the deferred payment.


---

*[View on Apple Developer](https://developer.apple.com/documentation/passkit/pkdeferredpaymentsummaryitem)*