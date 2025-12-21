# ChartContentBuilder

**Framework**: Swift Charts  
**Kind**: struct

A result builder that you use to compose the contents of a chart.

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
struct ChartContentBuilder
```

#### Overview

This [`Result Builder`](https://developer.apple.comhttps://docs.swift.org/swift-book/LanguageGuide/AdvancedOperators.html#ID630) combines any number of [`ChartContent`](chartcontent.md) instances into a single composite instance, including support for conditionals.

You don’t call the methods of the result builder directly. Instead, Swift uses them to combine the elements that you declare in any closure that has the `@ChartContentBuilder` attribute. In particular, you rely on this behavior when you declare the `content` inside a [`Chart`](chart.md) initializer like [`init(content:)`](chart/init(content:).md).

## Topics

### Building chart content
- [static func buildPartialBlock<T>(first: T) -> T](chartcontentbuilder/buildpartialblock(first:).md)
  Builds a partial result from a single, first component.
- [static func buildPartialBlock(accumulated: some ChartContent, next: some ChartContent) -> some ChartContent](chartcontentbuilder/buildpartialblock(accumulated:next:).md)
  Builds a partial result by combining an accumulated component and a new component.
- [static func buildBlock() -> some ChartContent](chartcontentbuilder/buildblock.md)
  Produces empty chart content.
### Building conditionally
- [static func buildIf<T>(T?) -> T?](chartcontentbuilder/buildif(_:).md)
  Builds a partial result that’s conditionally present.
- [static func buildEither<T1, T2>(first: T1) -> BuilderConditional<T1, T2>](chartcontentbuilder/buildeither(first:).md)
  Builds a partial result from a condition that’s true.
- [static func buildEither<T1, T2>(second: T2) -> BuilderConditional<T1, T2>](chartcontentbuilder/buildeither(second:).md)
  Builds a partial result from a condition that’s false.
### Building with conditional availability
- [static func buildLimitedAvailability(some ChartContent) -> AnyChartContent](chartcontentbuilder/buildlimitedavailability(_:).md)
  Builds a partial result that propagates or erases type information outside a compiler-controlled availability check.
### Supporting types
- [struct BuilderConditional](builderconditional.md)
  A conditional result from a result builder.
### Type Methods
- [static func buildBlock<each C>(repeat each C) -> some ChartContent](chartcontentbuilder/buildblock(_:)-51ukk.md)
  Builds a result from multiple components.
- [static func buildBlock<C>(C) -> C](chartcontentbuilder/buildblock(_:)-797vj.md)
  Builds a result from a single component.
- [static func buildExpression<Content>(Content) -> Content](chartcontentbuilder/buildexpression(_:).md)

## See Also

- [Creating a chart using Swift Charts](creating-a-chart-using-swift-charts.md)
  Make a chart by combining chart building blocks in SwiftUI.
- [Visualizing your app’s data](visualizing-your-app-s-data.md)
  Build complex and interactive charts using Swift Charts.
- [struct Chart](chart.md)
  A SwiftUI view that displays a chart.
- [protocol ChartContent](chartcontent.md)
  A type that represents the content that you draw on a chart.
- [struct Plot](plot.md)
  A mechanism for grouping chart contents into a single entity.


---

*[View on Apple Developer](https://developer.apple.com/documentation/charts/chartcontentbuilder)*