# AxisContentBuilder

**Framework**: Swift Charts  
**Kind**: struct

A result builder that constructs axis content.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.0+
- visionOS 1.0+
- watchOS 9.0+

## Declaration

```swift
@resultBuilder
struct AxisContentBuilder
```

## Topics

### Type Methods
- [static func buildBlock() -> some AxisContent](axiscontentbuilder/buildblock.md)
- [static func buildBlock<T>(T) -> T](axiscontentbuilder/buildblock(_:)-27fku.md)
  Builds a result from a single component.
- [static func buildBlock<each T>(repeat each T) -> some AxisContent](axiscontentbuilder/buildblock(_:)-6p3cy.md)
  Builds a result from multiple components.
- [static func buildEither<T1, T2>(first: T1) -> BuilderConditional<T1, T2>](axiscontentbuilder/buildeither(first:).md)
  Provides support for “if-else” statements in multi-statement closures, producing conditional content for the “then” branch.
- [static func buildEither<T1, T2>(second: T2) -> BuilderConditional<T1, T2>](axiscontentbuilder/buildeither(second:).md)
  Provides support for “if-else” statements in multi-statement closures, producing conditional content for the “else” branch.
- [static func buildExpression<Content>(Content) -> Content](axiscontentbuilder/buildexpression(_:).md)
- [static func buildIf<T>(T?) -> T?](axiscontentbuilder/buildif(_:).md)
  Provides support for “if” statements in multi-statement closures, producing an optional axis content that is visible only when the condition evaluates to `true`.
- [static func buildLimitedAvailability<Content>(Content) -> AnyAxisContent](axiscontentbuilder/buildlimitedavailability(_:).md)
  Provides support for “if” statements with `#available()` clauses in multi-statement closures, producing conditional content for the “then” branch, i.e. the conditionally-available branch.
- [static func buildPartialBlock(accumulated: some AxisContent, next: some AxisContent) -> some AxisContent](axiscontentbuilder/buildpartialblock(accumulated:next:).md)
- [static func buildPartialBlock<T>(first: T) -> T](axiscontentbuilder/buildpartialblock(first:).md)

## See Also

- [Customizing axes in Swift Charts](customizing-axes-in-swift-charts.md)
  Improve the clarity of your chart by configuring the appearance of its axes.
- [struct ChartAxisContent](chartaxiscontent.md)
  A view that represents a chart’s axis.
- [protocol AxisContent](axiscontent.md)
  A type that represents the elements you use to build a chart’s axes.
- [struct AxisMarks](axismarks.md)
  A group of visual marks that a chart draws to indicate the composition of a chart’s axes.
- [struct AnyAxisContent](anyaxiscontent.md)
  A type-erased element of a chart’s axis.


---

*[View on Apple Developer](https://developer.apple.com/documentation/charts/axiscontentbuilder)*