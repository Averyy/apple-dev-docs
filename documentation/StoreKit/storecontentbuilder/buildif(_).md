# buildIf(_:)

**Framework**: StoreKit  
**Kind**: method  
**Role**: Type Method

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
static func buildIf<Content>(_ section: Content?) -> Content? where Content : StoreContent
```

## See Also

### Building store content
- [static func buildBlock<each Content>(repeat each Content) -> TupleStoreContent<repeat each Content>](./buildblock%28_%29.md)
- [static func buildEither<TrueContent, FalseContent>(first: TrueContent) -> _ConditionalContent<TrueContent, FalseContent>](./buildeither%28first%29.md)
- [static func buildEither<TrueContent, FalseContent>(second: FalseContent) -> _ConditionalContent<TrueContent, FalseContent>](./buildeither%28second%29.md)
- [static func buildExpression<Content>(Content) -> some StoreContent](./buildexpression%28_%29.md)
- [static func buildLimitedAvailability(any StoreContent) -> some StoreContent](./buildlimitedavailability%28_%29.md)
- [struct TupleStoreContent](../tuplestorecontent.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/storekit/storecontentbuilder/buildif(_:))*