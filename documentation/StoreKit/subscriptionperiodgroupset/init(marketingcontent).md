# init(marketingContent:)

**Framework**: StoreKit  
**Kind**: init  
**Role**: Initializer

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- tvOS 18.0+
- visionOS 2.0+
- watchOS 11.0+

## Declaration

```swift
@MainActor
@preconcurrency init(@ViewBuilder marketingContent: @escaping (Product.SubscriptionPeriod?) -> MarketingContent) where Label == AutomaticSubscriptionOptionGroupLabel
```

## See Also

### Creating subscription period group sets
- [init()](./init%28%29.md)
- [init(marketingContent: (Product.SubscriptionPeriod?) -> MarketingContent, label: (Product.SubscriptionPeriod?) -> Label)](./init%28marketingcontent,label%29.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/storekit/subscriptionperiodgroupset/init(marketingcontent:))*