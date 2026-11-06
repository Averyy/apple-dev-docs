# Transaction.OwnershipType

**Framework**: StoreKit  
**Kind**: struct  
**Role**: Structure

Values that indicate whether the customer purchased the product or has access to it through Family Sharing, an organization, or a group.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
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
- [static let familyShared: Transaction.OwnershipType](./ownershiptype-swift.struct/familyshared.md)
  The transaction belongs to a family member who benefits from the service.
- [static let purchased: Transaction.OwnershipType](./ownershiptype-swift.struct/purchased.md)
  The transaction belongs to the purchaser.
- [static var assigned: Transaction.OwnershipType](./ownershiptype-swift.struct/assigned.md)
  The transaction belongs to a customer who has access through an organization or group.
### Getting a localized description
- [var localizedDescription: String](./ownershiptype-swift.struct/localizeddescription.md)
  The localized text that describes the ownership type.

## Relationships

### Conforms To
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [RawRepresentable](../../Swift/rawrepresentable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Getting purchase details
- [let isUpgraded: Bool](./isupgraded.md)
  A Boolean that indicates whether the user upgraded to another subscription.
- [let ownershipType: Transaction.OwnershipType](./ownershiptype-swift.property.md)
  A value that indicates whether the customer purchased the product or has access to it through Family Sharing, an organization, or a group.
- [let purchasedQuantity: Int](./purchasedquantity.md)
  The number of purchased seats or consumable products.


---

*[View on Apple Developer](https://developer.apple.com/documentation/storekit/transaction/ownershiptype-swift.struct)*