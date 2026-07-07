# buildLimitedAvailability(_:)

**Framework**: StoreKit  
**Kind**: method

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- macOS 15.0+
- tvOS 18.0+
- visionOS 2.0+
- watchOS 11.0+

## Declaration

```swift
static func buildLimitedAvailability(_ content: any StoreContent) -> some StoreContent
```

## See Also

- [static func buildBlock<each Content>(repeat each Content) -> TupleStoreContent<repeat each Content>](storecontentbuilder/buildblock(_:).md)
- [static func buildEither<TrueContent, FalseContent>(first: TrueContent) -> _ConditionalContent<TrueContent, FalseContent>](storecontentbuilder/buildeither(first:).md)
- [static func buildEither<TrueContent, FalseContent>(second: FalseContent) -> _ConditionalContent<TrueContent, FalseContent>](storecontentbuilder/buildeither(second:).md)
- [static func buildExpression<Content>(Content) -> some StoreContent](storecontentbuilder/buildexpression(_:).md)
- [static func buildIf<Content>(Content?) -> Content?](storecontentbuilder/buildif(_:).md)
- [struct TupleStoreContent](tuplestorecontent.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/storekit/storecontentbuilder/buildlimitedavailability(_:))*