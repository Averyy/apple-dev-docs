# init(description:requestValueDialog:inputConnectionBehavior:optionsProvider:)

**Framework**: App Intents  
**Kind**: init

Creates an app intent parameter with a list of selectable options.

**Availability**:
- iOS 18.2+
- iPadOS 18.2+
- Mac Catalyst ?+
- macOS 15.2+
- tvOS 18.2+
- visionOS 2.2+
- watchOS 11.2+

## Declaration

```swift
convenience init<OptionsProvider>(description: LocalizedStringResource? = nil, requestValueDialog: IntentDialog? = nil, inputConnectionBehavior: InputConnectionBehavior = .default, optionsProvider: OptionsProvider) where OptionsProvider : DynamicOptionsProvider, OptionsProvider.DefaultValue.ValueType == Calendar.RecurrenceRule
```

## Parameters

- `description`: Additional details about this parameter.
- `requestValueDialog`: A prompt that asks a person to provide the parameter value.
- `inputConnectionBehavior`: An enum that indicates how this parameter receives the output from a preceding app intent.
- `optionsProvider`: An object that determines selectable options for this parameter.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/intentparameter/init(description:requestvaluedialog:inputconnectionbehavior:optionsprovider:)-2thrb)*