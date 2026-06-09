# parameterSummary

**Framework**: App Intents  
**Kind**: property  
**Required**: Yes

The parameter summary the Shortcuts app uses to generate shortcuts for this intent.

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
static var parameterSummary: Self.SummaryContent { get }
```

## Mentions

- [Adding parameters to an app intent](adding-parameters-to-an-app-intent.md)
- [Creating your first app intent](creating-your-first-app-intent.md)

#### Discussion

Use this property to create interactive descriptions of your app intent that include relevant parameter values. You can use this property to provide multiple summaries reflecting specific parameter values or combinations of values. You can also incorporate specific parameters values into your descriptions using variable substitution. The Shortcuts app uses the contents of this property to create bespoke shortcuts for your app.

For information about how to create parameter summaries for an app intent, see [`Provide an interactive parameter summary for your intent`](adding-parameters-to-an-app-intent#Provide-an-interactive-parameter-summary-for-your-intent.md).

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
- [AppIntent.Option](appintent/option.md)
  A convenience type alias that represents a choice option within the scope of an app intent.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/appintent/parametersummary)*