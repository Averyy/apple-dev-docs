# autoRenewPreference

**Framework**: StoreKit  
**Kind**: property

The product ID of the auto-renewable subscription that will automatically renew.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- macOS 12.0+
- tvOS 15.0+
- visionOS 1.0+
- watchOS 8.0+

## Declaration

```swift
let autoRenewPreference: String?
```

#### Discussion

This value is the product ID of the auto-renewable subscription that will renew after the current period expires. The value may be:

- The same as [`currentProductID`](product/subscriptioninfo/renewalinfo/currentproductid.md) if the subscription will renew with the same product.
- Another product ID value if the subscription will renew to a different product.
- `nil` if the subscription won’t renew in the next period. This may occur for several reasons, including when the person disables auto-renew for the subscription, the subscription lapses due to a billing issue, or you increase the subscription price and the person doesn’t accept the increase.

## See Also

- [let state: Product.SubscriptionInfo.RenewalState](product/subscriptioninfo/status-swift.struct/state.md)
  The renewal state of the auto-renewable subscription.
- [let willAutoRenew: Bool](product/subscriptioninfo/renewalinfo/willautorenew.md)
  A Boolean value that indicates whether the subscription automatically renews in the next period.
- [let expirationReason: Product.SubscriptionInfo.RenewalInfo.ExpirationReason?](product/subscriptioninfo/renewalinfo/expirationreason-swift.property.md)
  The reason the auto-renewable subscription expired.
- [Product.SubscriptionInfo.RenewalInfo.ExpirationReason](product/subscriptioninfo/renewalinfo/expirationreason-swift.struct.md)
  The reasons for auto-renewable subscription expirations.


---

*[View on Apple Developer](https://developer.apple.com/documentation/storekit/product/subscriptioninfo/renewalinfo/autorenewpreference)*