# AppIntent.Summary

**Framework**: App Intents  
**Kind**: typealias  
**Role**: Type Alias

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.0+
- visionOS
- watchOS 9.0+

## Declaration

```swift
typealias Summary = IntentParameterSummary<Self>
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
- [AppIntent.Switch](./switch.md)
- [AppIntent.When](./when.md)
- [AppIntent.Option](./option.md)
  A convenience type alias that represents a choice option within the scope of an app intent.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/appintent/summary)*