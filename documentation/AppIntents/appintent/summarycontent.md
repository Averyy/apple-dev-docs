# SummaryContent

**Framework**: App Intents  
**Kind**: associatedtype  
**Required**: Yes

The type of parameter summary representing this intent.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst ?+
- macOS 13.0+
- tvOS 16.0+
- visionOS ?+
- watchOS 9.0+

## Declaration

```swift
associatedtype SummaryContent : ParameterSummary
```

#### Discussion

When you create an intent, Swift infers this type from your implementation of the [`parameterSummary`](appintent/parametersummary.md) property.

## See Also

- [static var parameterSummary: Self.SummaryContent](appintent/parametersummary.md)
  Defines the summary of this intent in relation to how its parameters are populated.
- [static var parameterSummary: some ParameterSummary](appintent/parametersummary-4vgic.md)
- [enum ParameterSummaryBuilder](parametersummarybuilder.md)
  A result builder that allows you to declaratively describe a parameter summary.
- [AppIntent.Parameter](appintent/parameter.md)
- [AppIntent.Case](appintent/case.md)
- [AppIntent.DefaultCase](appintent/defaultcase.md)
- [AppIntent.Summary](appintent/summary.md)
- [AppIntent.Switch](appintent/switch.md)
- [AppIntent.When](appintent/when.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/appintent/summarycontent)*