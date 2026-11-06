# Product.SubscriptionInfo.RenewalInfo.MultiSeatInfo

**Framework**: StoreKit  
**Kind**: struct  
**Role**: Structure

The price tiers of a multiseat subscription at its next renewal.

**Availability**:
- iOS 27.3+ (Beta)
- iPadOS 27.3+ (Beta)
- Mac Catalyst 27.3+ (Beta)
- macOS 27.3+ (Beta)
- tvOS 27.3+ (Beta)
- visionOS 27.3+ (Beta)
- watchOS 27.3+ (Beta)

## Declaration

```swift
struct MultiSeatInfo
```

## Topics

### Getting the renewal price tiers
- [let renewalPriceTiers: [Transaction.MultiSeatInfo.PriceTier]](./multiseatinfo-swift.struct/renewalpricetiers.md)
  The price tiers of the seats at the next renewal, with the number of seats at each price.

## Relationships

### Conforms To
- [Equatable](../../../../Swift/equatable.md)
- [Hashable](../../../../Swift/hashable.md)
- [Sendable](../../../../Swift/sendable.md)
- [SendableMetatype](../../../../Swift/sendablemetatype.md)

## See Also

### Getting multiseat renewal information
- [let renewalQuantity: Int?](./renewalquantity.md)
  The number of seats in a multiseat subscription at its next renewal.
- [let multiSeatInfo: Product.SubscriptionInfo.RenewalInfo.MultiSeatInfo?](./multiseatinfo-swift.property.md)
  The seat information for the next renewal of a multiseat subscription.


---

*[View on Apple Developer](https://developer.apple.com/documentation/storekit/product/subscriptioninfo/renewalinfo/multiseatinfo-swift.struct)*