# init(_:isIncluded:footer:)

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
@preconcurrency init(_ title: LocalizedStringKey, isIncluded: @escaping (Product) -> Bool, @ViewBuilder footer: () -> Footer = EmptyView.init)
```

Available when `Header` is `Text`, `Content` is `Never`, and `Footer` conforms to `View`.

## See Also

### Creating subscription option sections
- [init(some StringProtocol, isIncluded: (Product) -> Bool, footer: () -> Footer)](./init%28_,isincluded,footer%29-36k79.md)
- [init(isIncluded: (Product) -> Bool, header: () -> Header, footer: () -> Footer)](./init%28isincluded,header,footer%29.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/storekit/subscriptionoptionsection/init(_:isincluded:footer:)-17lo3)*