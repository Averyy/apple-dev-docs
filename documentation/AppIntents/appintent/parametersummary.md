# parameterSummary

**Framework**: App Intents  
**Kind**: property  
**Required**: Yes

Defines the summary of this intent in relation to how its parameters are populated.

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
static var parameterSummary: Self.SummaryContent { get }
```

## Mentions

- [Adding parameters to an app intent](adding-parameters-to-an-app-intent.md)

#### Discussion

For more information about using parameters and providing a parameter summary, see [`Provide an interactive parameter summary for your intent`](adding-parameters-to-an-app-intent#Provide-an-interactive-parameter-summary-for-your-intent.md).

## See Also

- [associatedtype SummaryContent : ParameterSummary](appintent/summarycontent.md)
  The type of parameter summary representing this intent.
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

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/appintent/parametersummary)*