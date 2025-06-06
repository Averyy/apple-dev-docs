# buildEither(first:)

**Framework**: MapKit  
**Kind**: method

Compares content in a multistatement closure, resulting in use of the conditional content if the first argument you provide evaluates to  true.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst ?+
- macOS 14.0+
- tvOS 17.0+
- visionOS ?+
- watchOS 10.0+

## Declaration

```swift
static func buildEither<TrueContent, FalseContent>(first: TrueContent) -> _ConditionalMapContent<TrueContent, FalseContent> where TrueContent : MapContent, FalseContent : MapContent
```

#### Return Value

Returns the conditional map content that meets the conditions the content builder expresses.

## Parameters

- `first`: The content that represents the   content element to compare against.

## See Also

- [static func buildEither<TrueContent, FalseContent>(second: FalseContent) -> _ConditionalMapContent<TrueContent, FalseContent>](mapcontentbuilder/buildeither(second:).md)
  Compares content in a multistatement closure, resulting in use of the conditional content if the second argument you provide evaluates to true.
- [static func buildExpression<Content>(Content) -> Content](mapcontentbuilder/buildexpression(_:).md)
  Builds an expression within the map content builder.
- [static func buildIf<Content>(Content?) -> Content?](mapcontentbuilder/buildif(_:).md)
  Compares content in a multistatement closure, that produces an optional view that’s visible if the argument you provide evaluates to true.
- [static func buildLimitedAvailability(any MapContent) -> some MapContent](mapcontentbuilder/buildlimitedavailability(_:).md)
  Provides support for “if” statements with “available” macro clauses in multi-statement closures, producing conditional content for the “then” branch, such the conditionally-available branch.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkit/mapcontentbuilder/buildeither(first:))*