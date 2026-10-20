# Transaction.AdvancedCommerceInfo.Refund.Reason

**Framework**: StoreKit  
**Kind**: struct  
**Role**: Structure

The reason for the refund.

**Availability**:
- iOS 18.4+
- iPadOS 18.4+
- Mac Catalyst 18.4+
- macOS 15.4+
- tvOS 18.4+
- visionOS 2.4+
- watchOS 11.4+

## Declaration

```swift
struct Reason
```

## Topics

### Type Properties
- [static let legal: Transaction.AdvancedCommerceInfo.Refund.Reason](./reason-swift.struct/legal.md)
  The customer requested a refund based on a legal reason.
- [static let modifyItems: Transaction.AdvancedCommerceInfo.Refund.Reason](./reason-swift.struct/modifyitems.md)
- [static let other: Transaction.AdvancedCommerceInfo.Refund.Reason](./reason-swift.struct/other.md)
  The customer requested a refund for other reasons.
- [static let unfulfilled: Transaction.AdvancedCommerceInfo.Refund.Reason](./reason-swift.struct/unfulfilled.md)
  The customer had issues with receiving or using the Apple In-App Purchase.
- [static let unintended: Transaction.AdvancedCommerceInfo.Refund.Reason](./reason-swift.struct/unintended.md)
  The customer didn’t intend to make the Apple In-App Purchase.
- [static let unsatisfied: Transaction.AdvancedCommerceInfo.Refund.Reason](./reason-swift.struct/unsatisfied.md)
  The customer wasn’t satisfied with the Apple In-App Purchase.

## Relationships

### Conforms To
- [Equatable](../../../../Swift/equatable.md)
- [Hashable](../../../../Swift/hashable.md)
- [RawRepresentable](../../../../Swift/rawrepresentable.md)
- [Sendable](../../../../Swift/sendable.md)
- [SendableMetatype](../../../../Swift/sendablemetatype.md)

## See Also

### Structures
- [Transaction.AdvancedCommerceInfo.Refund.RefundType](./refundtype.md)
  The type of refund.


---

*[View on Apple Developer](https://developer.apple.com/documentation/storekit/transaction/advancedcommerceinfo-swift.struct/refund/reason-swift.struct)*