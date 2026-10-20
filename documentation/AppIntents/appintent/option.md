# AppIntent.Option

**Framework**: App Intents  
**Kind**: typealias  
**Role**: Type Alias

A convenience type alias that represents a choice option within the scope of an app intent.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- tvOS 26.0+
- visionOS 26.0+
- watchOS 26.0+

## Declaration

```swift
typealias Option = IntentChoiceOption
```

## See Also

### Summarizing the parameters
- [associatedtype SummaryContent : ParameterSummary](./summarycontent.md)
  The type of parameter summary representing this intent.
- [static var parameterSummary: Self.SummaryContent](./parametersummary.md)
  The parameter summary the Shortcuts app uses to generate shortcuts for this intent.
- [static var parameterSummary: some ParameterSummary](./parametersummary-4vgic.md)
- [enum ParameterSummaryBuilder](../parametersummarybuilder.md)
  A result builder that allows you to declaratively describe a parameter summary.
- [AppIntent.Parameter](./parameter.md)
- [AppIntent.Case](./case.md)
- [AppIntent.DefaultCase](./defaultcase.md)
- [AppIntent.Summary](./summary.md)
- [AppIntent.Switch](./switch.md)
- [AppIntent.When](./when.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/appintent/option)*