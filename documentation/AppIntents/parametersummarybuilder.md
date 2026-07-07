# ParameterSummaryBuilder

**Framework**: App Intents  
**Kind**: enum

A result builder that allows you to declaratively describe a parameter summary.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.0+
- visionOS ?+
- watchOS 9.0+

## Declaration

```swift
@resultBuilder
enum ParameterSummaryBuilder<Intent> where Intent : AppIntent
```

## Mentions

- [Adding parameters to an app intent](adding-parameters-to-an-app-intent.md)
- [Creating your first app intent](creating-your-first-app-intent.md)

#### Overview

For more information about using parameters and providing a parameter summary, see [`Provide an interactive parameter summary for your intent`](adding-parameters-to-an-app-intent#Provide-an-interactive-parameter-summary-for-your-intent.md).

## Topics

### Type Methods
- [static func buildBlock<Summary>(Summary) -> Summary](parametersummarybuilder/buildblock(_:).md)
- [static func buildExpression<Summary>(Summary) -> Summary](parametersummarybuilder/buildexpression(_:).md)

## See Also

- [associatedtype SummaryContent : ParameterSummary](appintent/summarycontent.md)
  The type of parameter summary representing this intent.
- [static var parameterSummary: Self.SummaryContent](appintent/parametersummary.md)
  The parameter summary the Shortcuts app uses to generate shortcuts for this intent.
- [static var parameterSummary: some ParameterSummary](appintent/parametersummary-4vgic.md)
- [AppIntent.Parameter](appintent/parameter.md)
- [AppIntent.Case](appintent/case.md)
- [AppIntent.DefaultCase](appintent/defaultcase.md)
- [AppIntent.Summary](appintent/summary.md)
- [AppIntent.Switch](appintent/switch.md)
- [AppIntent.When](appintent/when.md)
- [AppIntent.Option](appintent/option.md)
  A convenience type alias that represents a choice option within the scope of an app intent.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/parametersummarybuilder)*