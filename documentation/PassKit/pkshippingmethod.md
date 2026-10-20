# PKShippingMethod

**Framework**: PassKit (Apple Pay and Wallet)  
**Kind**: class  
**Role**: Class

An object that defines a shipping method for delivering physical goods.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 11.0+
- visionOS 1.0+
- watchOS 3.0+

## Declaration

```swift
class PKShippingMethod
```

```objc
@interface PKShippingMethod : PKPaymentSummaryItem
```

## Topics

### Working with shipping methods
- [var detail: String?](./pkshippingmethod/detail.md)
  A user-readable description of the shipping method.
- [var dateComponentsRange: PKDateComponentsRange?](./pkshippingmethod/datecomponentsrange.md)
  An expected range of delivery or shipping dates for a package, or the time range when an item is available for pickup.
- [var identifier: String?](./pkshippingmethod/identifier.md)
  A unique identifier for the shipping method, used by the app.
- [class PKDateComponentsRange](./pkdatecomponentsrange.md)
  An object that specifies the start and end dates for a range of time.

## Relationships

### Inherits From
- [PKPaymentSummaryItem](./pkpaymentsummaryitem.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)

## See Also

### Working with billing and shipping information
- [var billingContact: PKContact?](./pkpayment/billingcontact.md)
  The user-selected billing address for this transaction.
- [var shippingContact: PKContact?](./pkpayment/shippingcontact.md)
  The user-selected shipping address for this transaction.
- [var shippingMethod: PKShippingMethod?](./pkpayment/shippingmethod.md)
  The user-selected shipping method for this transaction.
- [class PKContact](./pkcontact.md)
  An object that encapsulates contact information needed for billing and shipping.


---

*[View on Apple Developer](https://developer.apple.com/documentation/passkit/pkshippingmethod)*