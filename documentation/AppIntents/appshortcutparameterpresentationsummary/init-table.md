# init(_:table:)

**Framework**: App Intents  
**Kind**: init

Initializes a presentation summary with the specified parameters.

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
init(_ summaryString: AppShortcutParameterPresentationSummaryString<Intent, Value, Parameter, ParameterKeyPath>, table: StaticString? = nil)
```

## Parameters

- `summaryString`: Represents the summary of the  .   Example: “Call (.$person)”.
- `table`: An optional   representing the table to use when localizing the summary.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/appshortcutparameterpresentationsummary/init(_:table:))*