# TupleStoreContent

**Framework**: StoreKit  
**Kind**: struct

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
@preconcurrency struct TupleStoreContent<each Content> where repeat each Content : StoreContent
```

## Relationships

### Conforms To
- [Sendable](../Swift/Sendable.md)
- [StoreContent](storecontent.md)

## See Also

- [static func buildBlock<each Content>(repeat each Content) -> TupleStoreContent<repeat each Content>](storecontentbuilder/buildblock(_:).md)
- [static func buildEither<TrueContent, FalseContent>(first: TrueContent) -> _ConditionalContent<TrueContent, FalseContent>](storecontentbuilder/buildeither(first:).md)
- [static func buildEither<TrueContent, FalseContent>(second: FalseContent) -> _ConditionalContent<TrueContent, FalseContent>](storecontentbuilder/buildeither(second:).md)
- [static func buildExpression<Content>(Content) -> some StoreContent](storecontentbuilder/buildexpression(_:).md)
- [static func buildIf<Content>(Content?) -> Content?](storecontentbuilder/buildif(_:).md)
- [static func buildLimitedAvailability(any StoreContent) -> some StoreContent](storecontentbuilder/buildlimitedavailability(_:).md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/storekit/tuplestorecontent)*