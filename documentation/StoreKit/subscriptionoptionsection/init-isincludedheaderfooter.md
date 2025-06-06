# init(isIncluded:header:footer:)

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
@preconcurrency init(isIncluded: @escaping (Product) -> Bool, @ViewBuilder header: () -> Header = EmptyView.init, @ViewBuilder footer: () -> Footer = EmptyView.init)
```

## See Also

- [init(LocalizedStringKey, isIncluded: (Product) -> Bool, footer: () -> Footer)](subscriptionoptionsection/init(_:isincluded:footer:)-17lo3.md)
- [init(some StringProtocol, isIncluded: (Product) -> Bool, footer: () -> Footer)](subscriptionoptionsection/init(_:isincluded:footer:)-36k79.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/storekit/subscriptionoptionsection/init(isincluded:header:footer:))*