# init(_:isIncluded:footer:)

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
@preconcurrency init(_ title: LocalizedStringKey, isIncluded: @escaping (Product) -> Bool, @ViewBuilder footer: () -> Footer = EmptyView.init)
```

## See Also

- [init(some StringProtocol, isIncluded: (Product) -> Bool, footer: () -> Footer)](subscriptionoptionsection/init(_:isincluded:footer:)-36k79.md)
- [init(isIncluded: (Product) -> Bool, header: () -> Header, footer: () -> Footer)](subscriptionoptionsection/init(isincluded:header:footer:).md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/storekit/subscriptionoptionsection/init(_:isincluded:footer:)-17lo3)*