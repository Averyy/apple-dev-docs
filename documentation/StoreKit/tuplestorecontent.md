# TupleStoreContent

**Framework**: StoreKit  
**Kind**: struct  
**Role**: Structure

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
@preconcurrency struct TupleStoreContent<each Content> where repeat each Content : StoreContent
```

## Relationships

### Conforms To
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)
- [StoreContent](./storecontent.md)

## See Also

### Building store content
- [static func buildBlock<each Content>(repeat each Content) -> TupleStoreContent<repeat each Content>](./storecontentbuilder/buildblock%28_%29.md)
- [static func buildEither<TrueContent, FalseContent>(first: TrueContent) -> _ConditionalContent<TrueContent, FalseContent>](./storecontentbuilder/buildeither%28first%29.md)
- [static func buildEither<TrueContent, FalseContent>(second: FalseContent) -> _ConditionalContent<TrueContent, FalseContent>](./storecontentbuilder/buildeither%28second%29.md)
- [static func buildExpression<Content>(Content) -> some StoreContent](./storecontentbuilder/buildexpression%28_%29.md)
- [static func buildIf<Content>(Content?) -> Content?](./storecontentbuilder/buildif%28_%29.md)
- [static func buildLimitedAvailability(any StoreContent) -> some StoreContent](./storecontentbuilder/buildlimitedavailability%28_%29.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/storekit/tuplestorecontent)*