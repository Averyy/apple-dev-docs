# Transaction.Reason

**Framework**: StoreKit  
**Kind**: struct

A cause of a purchase transaction, indicating whether it’s a customer’s purchase or an auto-renewable subscription renewal that the system initiates.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- tvOS 17.0+
- visionOS 1.0+
- watchOS 10.0+

## Declaration

```swift
struct Reason
```

## Topics

### Transaction reasons
- [static let purchase: Transaction.Reason](transaction/reason-swift.struct/purchase.md)
  A transaction reason that indicates a purchase is initiated by a customer.
- [static let renewal: Transaction.Reason](transaction/reason-swift.struct/renewal.md)
  A transaction reason that indicates the App Store server initiated a purchase transaction to renew an auto-renewable subscription.

## Relationships

### Conforms To
- [Equatable](../swift/equatable.md)
- [Hashable](../swift/hashable.md)
- [RawRepresentable](../swift/rawrepresentable.md)
- [Sendable](../swift/sendable.md)
- [SendableMetatype](../swift/sendablemetatype.md)

## See Also

- [let reason: Transaction.Reason](transaction/reason-swift.property.md)
  The cause of the purchase transaction, whether it’s a customer’s purchase or an auto-renewable subscription renewal that the system initiates.


---

*[View on Apple Developer](https://developer.apple.com/documentation/storekit/transaction/reason-swift.struct)*