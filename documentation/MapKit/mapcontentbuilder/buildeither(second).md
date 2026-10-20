# buildEither(second:)

**Framework**: MapKit  
**Kind**: method  
**Role**: Type Method

Compares content in a multistatement closure, resulting in use of the conditional content if the second argument you provide evaluates to true.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- tvOS 17.0+
- visionOS
- watchOS 10.0+

## Declaration

```swift
static func buildEither<TrueContent, FalseContent>(second: FalseContent) -> _ConditionalMapContent<TrueContent, FalseContent> where TrueContent : MapContent, FalseContent : MapContent
```

#### Return Value

Returns the conditional map content that meets the conditions the content builder expresses.

## Parameters

- `second`: The content that represents the `false` content element to compare against.

## See Also

### Conditionally building map content
- [static func buildEither<TrueContent, FalseContent>(first: TrueContent) -> _ConditionalMapContent<TrueContent, FalseContent>](./buildeither%28first%29.md)
  Compares content in a multistatement closure, resulting in use of the conditional content if the first argument you provide evaluates to  true.
- [static func buildExpression<Content>(Content) -> Content](./buildexpression%28_%29.md)
  Builds an expression within the map content builder.
- [static func buildIf<Content>(Content?) -> Content?](./buildif%28_%29.md)
  Compares content in a multistatement closure, that produces an optional view that’s visible if the argument you provide evaluates to true.
- [static func buildLimitedAvailability(any MapContent) -> some MapContent](./buildlimitedavailability%28_%29.md)
  Provides support for “if” statements with “available” macro clauses in multi-statement closures, producing conditional content for the “then” branch, such the conditionally-available branch.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkit/mapcontentbuilder/buildeither(second:))*