# StoreContentBuilder

**Framework**: StoreKit  
**Kind**: struct

A result builder that creates store content from closures that you provide.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- macOS 15.0+
- tvOS 18.0+
- visionOS 2.0+
- watchOS 11.0+

## Declaration

```swift
@resultBuilder
struct StoreContentBuilder
```

## Topics

### Building store content
- [static func buildBlock<each Content>(repeat each Content) -> TupleStoreContent<repeat each Content>](storecontentbuilder/buildblock(_:).md)
- [static func buildEither<TrueContent, FalseContent>(first: TrueContent) -> _ConditionalContent<TrueContent, FalseContent>](storecontentbuilder/buildeither(first:).md)
- [static func buildEither<TrueContent, FalseContent>(second: FalseContent) -> _ConditionalContent<TrueContent, FalseContent>](storecontentbuilder/buildeither(second:).md)
- [static func buildExpression<Content>(Content) -> some StoreContent](storecontentbuilder/buildexpression(_:).md)
- [static func buildIf<Content>(Content?) -> Content?](storecontentbuilder/buildif(_:).md)
- [static func buildLimitedAvailability(any StoreContent) -> some StoreContent](storecontentbuilder/buildlimitedavailability(_:).md)
- [struct TupleStoreContent](tuplestorecontent.md)

## See Also

- [struct SubscriptionOptionGroup](subscriptionoptiongroup.md)
  A group of subscription options that includes optional views for labels and marketing content.
- [struct SubscriptionOptionGroupSet](subscriptionoptiongroupset.md)
  A set of groups of subscription options that include optional views for labels and marketing content.
- [struct SubscriptionPeriodGroupSet](subscriptionperiodgroupset.md)
- [struct SubscriptionOptionSection](subscriptionoptionsection.md)
- [protocol StoreContent](storecontent.md)
  A type that represents the content of a store.


---

*[View on Apple Developer](https://developer.apple.com/documentation/storekit/storecontentbuilder)*