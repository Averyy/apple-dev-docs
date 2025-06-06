# Transaction.OwnershipType

**Framework**: StoreKit  
**Kind**: struct

The types the system uses to describe whether the user purchased the product or it’s available to them through Family Sharing.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- macOS 12.0+
- tvOS 15.0+
- visionOS 1.0+
- watchOS 8.0+

## Declaration

```swift
struct OwnershipType
```

## Topics

### Getting ownership types
- [static let familyShared: Transaction.OwnershipType](transaction/ownershiptype-swift.struct/familyshared.md)
  The transaction belongs to a family member who benefits from the service.
- [static let purchased: Transaction.OwnershipType](transaction/ownershiptype-swift.struct/purchased.md)
  The transaction belongs to the purchaser.
### Getting a localized description
- [var localizedDescription: String](transaction/ownershiptype-swift.struct/localizeddescription.md)
  The localized text that describes the ownership type.

## Relationships

### Conforms To
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [let isUpgraded: Bool](transaction/isupgraded.md)
  A Boolean that indicates whether the user upgraded to another subscription.
- [let ownershipType: Transaction.OwnershipType](transaction/ownershiptype-swift.property.md)
  A value that indicates whether the transaction was purchased by the user, or is made available to them through Family Sharing.
- [let purchasedQuantity: Int](transaction/purchasedquantity.md)
  The number of consumable products purchased.


---

*[View on Apple Developer](https://developer.apple.com/documentation/storekit/transaction/ownershiptype-swift.struct)*