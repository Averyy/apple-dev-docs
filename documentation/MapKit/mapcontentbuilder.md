# MapContentBuilder

**Framework**: MapKit  
**Kind**: struct

A result builder that creates map content from closures you provide.

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
@resultBuilder
struct MapContentBuilder
```

#### Overview

The [`buildBlock(_:)`](mapcontentbuilder/buildblock(_:)-5ewn9.md) methods in this type create [`MapContent`](mapcontent.md) instances based on the number and types of sources you provide as parameters.

You don’t use this type directly. Instead, SwiftUI annotates the `content` parameter of the various `MapView` initializers with the `@MapContentBuilder` annotation, implicitly calling this builder for you.

## Topics

### Map content builders
- [static func buildBlock() -> EmptyMapContent](mapcontentbuilder/buildblock.md)
  Creates an empty map content block that contains no statements.
- [static func buildBlock<C>(C) -> C](mapcontentbuilder/buildblock(_:)-5ewn9.md)
  Creates a map content block that contains a single content result.
### Conditionally building map content
- [static func buildEither<TrueContent, FalseContent>(first: TrueContent) -> _ConditionalMapContent<TrueContent, FalseContent>](mapcontentbuilder/buildeither(first:).md)
  Compares content in a multistatement closure, resulting in use of the conditional content if the first argument you provide evaluates to  true.
- [static func buildEither<TrueContent, FalseContent>(second: FalseContent) -> _ConditionalMapContent<TrueContent, FalseContent>](mapcontentbuilder/buildeither(second:).md)
  Compares content in a multistatement closure, resulting in use of the conditional content if the second argument you provide evaluates to true.
- [static func buildExpression<Content>(Content) -> Content](mapcontentbuilder/buildexpression(_:).md)
  Builds an expression within the map content builder.
- [static func buildIf<Content>(Content?) -> Content?](mapcontentbuilder/buildif(_:).md)
  Compares content in a multistatement closure, that produces an optional view that’s visible if the argument you provide evaluates to true.
- [static func buildLimitedAvailability(any MapContent) -> some MapContent](mapcontentbuilder/buildlimitedavailability(_:).md)
  Provides support for “if” statements with “available” macro clauses in multi-statement closures, producing conditional content for the “then” branch, such the conditionally-available branch.
### Type Methods
- [static func buildBlock<each Content>(repeat each Content) -> TupleMapContent<(repeat each Content)>](mapcontentbuilder/buildblock(_:)-4omn.md)

## See Also

- [protocol DynamicMapContent](dynamicmapcontent.md)
  A  type of view that generates views from an underlying collection of data.
- [protocol MapContent](mapcontent.md)
  A protocol used to construct map content such as controls, markers, and annotations.
- [struct MapContentView](mapcontentview.md)
  A view that contains content that displays on a map at a specific position, and that responds to specific interactions you specify.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mapkit/mapcontentbuilder)*