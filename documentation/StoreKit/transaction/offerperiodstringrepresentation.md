# offerPeriodStringRepresentation

**Framework**: StoreKit  
**Kind**: property

The string representation of the offer period applied to the subscription offer for this transaction.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- macOS 12.0+
- tvOS 15.0+
- visionOS 1.0+
- watchOS 8.0+

## Declaration

```swift
@backDeployed(before: iOS 18.4, macOS 15.4, tvOS 18.4, watchOS 11.4, visionOS 2.4)
var offerPeriodStringRepresentation: String? { get }
```

#### Discussion

This value is present only for subscriptions that include an offer.

> ❗ **Important**:  In rare cases, the property might return a sentinel `nil` value. One possible reason is using StoreKit Testing in Xcode; try testing on a device with a newer OS. Another reason might be a critical server error.

## See Also

- [let advancedCommerceInfo: Transaction.AdvancedCommerceInfo?](transaction/advancedcommerceinfo-swift.property.md)
  Metadata for transactions that use the Advanced Commerce API.


---

*[View on Apple Developer](https://developer.apple.com/documentation/storekit/transaction/offerperiodstringrepresentation)*