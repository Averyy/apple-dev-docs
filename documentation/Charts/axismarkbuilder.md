# AxisMarkBuilder

**Framework**: Swift Charts  
**Kind**: struct

A result builder that constructs axis marks and overrides default marks.

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
struct AxisMarkBuilder
```

## Topics

### Type Methods
- [static func buildBlock() -> some AxisMark](axismarkbuilder/buildblock.md)
- [static func buildBlock<T>(T) -> T](axismarkbuilder/buildblock(_:)-5kk19.md)
  Builds a result from a single component.
- [static func buildBlock<each T>(repeat each T) -> some AxisMark](axismarkbuilder/buildblock(_:)-97cxo.md)
  Builds a result from multiple components.
- [static func buildEither<T1, T2>(first: T1) -> BuilderConditional<T1, T2>](axismarkbuilder/buildeither(first:).md)
  Provides support for “if-else” statements in multi-statement closures, producing conditional content for the “then” branch.
- [static func buildEither<T1, T2>(second: T2) -> BuilderConditional<T1, T2>](axismarkbuilder/buildeither(second:).md)
  Provides support for “if-else” statements in multi-statement closures, producing conditional content for the “else” branch.
- [static func buildExpression<Content>(Content) -> Content](axismarkbuilder/buildexpression(_:).md)
- [static func buildIf<T>(T?) -> T?](axismarkbuilder/buildif(_:).md)
  Provides support for “if” statements in multi-statement closures, producing an optional axis content that is visible only when the condition evaluates to `true`.
- [static func buildLimitedAvailability<Content>(Content) -> AnyAxisMark](axismarkbuilder/buildlimitedavailability(_:).md)
  Provides support for “if” statements with `#available()` clauses in multi-statement closures, producing conditional content for the “then” branch, i.e. the conditionally-available branch.
- [static func buildPartialBlock(accumulated: some AxisMark, next: some AxisMark) -> some AxisMark](axismarkbuilder/buildpartialblock(accumulated:next:).md)
- [static func buildPartialBlock<T>(first: T) -> T](axismarkbuilder/buildpartialblock(first:).md)

## See Also

- [protocol AxisMark](axismark.md)
  A type that serves as the basic building block for the elements of an axis.
- [struct AxisTick](axistick.md)
  A mark that a chart draws on an axis to indicate a reference point along that axis.
- [struct AxisGridLine](axisgridline.md)
  A line that a chart draws across its plot area to indicate a reference point along a particular axis.
- [struct AxisValueLabel](axisvaluelabel.md)
  A label that describes the value for an axis mark.
- [struct AxisValue](axisvalue.md)
  A value for an axis mark.
- [struct AnyAxisMark](anyaxismark.md)
  A type-erased axis mark.


---

*[View on Apple Developer](https://developer.apple.com/documentation/charts/axismarkbuilder)*