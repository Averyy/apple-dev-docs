# init(title:description:currencyCodes:inclusiveRange:requestValueDialog:inputConnectionBehavior:)

**Framework**: App Intents  
**Kind**: init

Creates an app intent parameter.

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
convenience init(title: LocalizedStringResource, description: LocalizedStringResource? = nil, currencyCodes: [String] = [], inclusiveRange: IntentParameter<Value>.InclusiveRange<Decimal>? = nil, requestValueDialog: IntentDialog? = nil, inputConnectionBehavior: InputConnectionBehavior = .default)
```

## Parameters

- `title`: A word or short phrase summarizing this parameter.
- `description`: Additional details about this parameter.
- `currencyCodes`: A list of selectable currency symbols for this parameter. Use ISO 4217 currency codes.   The default value is an empty array which offers all currency codes to a person.
- `inclusiveRange`: The allowed minimum and maximum values for this parameter.
- `requestValueDialog`: A prompt that asks a person to provide the parameter value.
- `inputConnectionBehavior`: An enum that indicates how this parameter receives the output from a preceding app intent.

## See Also

- [convenience init<OptionsProvider>(title: LocalizedStringResource, description: LocalizedStringResource?, currencyCodes: [String], inclusiveRange: IntentParameter<Value>.InclusiveRange<Decimal>?, requestValueDialog: IntentDialog?, inputConnectionBehavior: InputConnectionBehavior, optionsProvider: OptionsProvider)](intentparameter/init(title:description:currencycodes:inclusiverange:requestvaluedialog:inputconnectionbehavior:optionsprovider:).md)
  Creates an app intent parameter with a list of selectable options.
- [convenience init<Spec, OptionsProvider>(title: LocalizedStringResource, description: LocalizedStringResource?, currencyCodes: [String], inclusiveRange: IntentParameter<Value>.InclusiveRange<Decimal>?, requestValueDialog: IntentDialog?, inputConnectionBehavior: InputConnectionBehavior, optionsProvider: OptionsProvider, resolvers: () -> Spec)](intentparameter/init(title:description:currencycodes:inclusiverange:requestvaluedialog:inputconnectionbehavior:optionsprovider:resolvers:).md)
  Creates an app intent parameter with a list of selectable options that can convert the selected value.
- [convenience init<Spec>(title: LocalizedStringResource, description: LocalizedStringResource?, currencyCodes: [String], inclusiveRange: IntentParameter<Value>.InclusiveRange<Decimal>?, requestValueDialog: IntentDialog?, inputConnectionBehavior: InputConnectionBehavior, resolvers: () -> Spec)](intentparameter/init(title:description:currencycodes:inclusiverange:requestvaluedialog:inputconnectionbehavior:resolvers:).md)
  Creates an app intent parameter that can convert the selected value.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/intentparameter/init(title:description:currencycodes:inclusiverange:requestvaluedialog:inputconnectionbehavior:))*