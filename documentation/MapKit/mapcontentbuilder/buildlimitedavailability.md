# buildLimitedAvailability(_:)

**Framework**: MapKit  
**Kind**: method

Provides support for “if” statements with “available” macro clauses in multi-statement closures, producing conditional content for the “then” branch, such the conditionally-available branch.

**Availability**:
- iOS 17.5+
- iPadOS 17.5+
- Mac Catalyst ?+
- macOS 14.5+
- tvOS 17.5+
- visionOS 1.2+
- watchOS 10.5+

## Declaration

```swift
static func buildLimitedAvailability(_ content: any MapContent) -> some MapContent
```

#### Return Value

Returns the conditional map content that meets the conditions the content builder expresses.

## Parameters

- `content`: The map builder content the expression builder operates on.

## See Also

- [static func buildEither<TrueContent, FalseContent>(first: TrueContent) -> _ConditionalMapContent<TrueContent, FalseContent>](mapcontentbuilder/buildeither(first:).md)
  Compares content in a multistatement closure, resulting in use of the conditional content if the first argument you provide evaluates to  true.
- [static func buildEither<TrueContent, FalseContent>(second: FalseContent) -> _ConditionalMapContent<TrueContent, FalseContent>](mapcontentbuilder/buildeither(second:).md)
  Compares content in a multistatement closure, resulting in use of the conditional content if the second argument you provide evaluates to true.
- [static func buildExpression<Content>(Content) -> Content](mapcontentbuilder/buildexpression(_:).md)
  Builds an expression within the map content builder.
- [static func buildIf<Content>(Content?) -> Content?](mapcontentbuilder/buildif(_:).md)
  Compares content in a multistatement closure, that produces an optional view that’s visible if the argument you provide evaluates to true.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkit/mapcontentbuilder/buildlimitedavailability(_:))*