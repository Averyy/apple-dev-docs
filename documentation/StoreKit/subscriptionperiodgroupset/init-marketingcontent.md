# init(marketingContent:)

**Framework**: StoreKit  
**Kind**: init

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
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

- [init()](subscriptionperiodgroupset/init.md)
- [init(marketingContent: (Product.SubscriptionPeriod?) -> MarketingContent, label: (Product.SubscriptionPeriod?) -> Label)](subscriptionperiodgroupset/init(marketingcontent:label:).md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/storekit/subscriptionperiodgroupset/init(marketingcontent:))*