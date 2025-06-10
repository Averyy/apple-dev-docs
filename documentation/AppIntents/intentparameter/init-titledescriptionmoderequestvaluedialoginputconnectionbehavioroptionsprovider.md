# init(title:description:mode:requestValueDialog:inputConnectionBehavior:optionsProvider:)

**Framework**: App Intents  
**Kind**: init

Creates an app intent parameter with a list of selectable options.

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
convenience init<OptionsProvider>(title: LocalizedStringResource, description: LocalizedStringResource? = nil, mode: IntentPerson.ParameterMode = .contact, requestValueDialog: IntentDialog? = nil, inputConnectionBehavior: InputConnectionBehavior = .default, optionsProvider: OptionsProvider) where OptionsProvider : DynamicOptionsProvider, OptionsProvider.DefaultValue.ValueType == IntentPerson
```

## Parameters

- `title`: A word or short phrase summarizing this parameter.
- `description`: Additional details about this parameter.
- `mode`: The user interface that appears when a person chooses a value for this parameter. Default value is  .
- `requestValueDialog`: A prompt that asks a person to provide the parameter value.
- `inputConnectionBehavior`: An enum that indicates how this parameter receives the output from a preceding app intent.
- `optionsProvider`: An object that determines selectable options for this parameter.

## See Also

- [convenience init(title: LocalizedStringResource, description: LocalizedStringResource?, mode: IntentPerson.ParameterMode, requestValueDialog: IntentDialog?, inputConnectionBehavior: InputConnectionBehavior)](intentparameter/init(title:description:mode:requestvaluedialog:inputconnectionbehavior:).md)
  Creates an app intent parameter.
- [convenience init<Spec, OptionsProvider>(title: LocalizedStringResource, description: LocalizedStringResource?, mode: IntentPerson.ParameterMode, requestValueDialog: IntentDialog?, inputConnectionBehavior: InputConnectionBehavior, optionsProvider: OptionsProvider, resolvers: () -> Spec)](intentparameter/init(title:description:mode:requestvaluedialog:inputconnectionbehavior:optionsprovider:resolvers:).md)
  Creates an app intent parameter with a list of selectable options that can convert the selected value.
- [convenience init<Spec>(title: LocalizedStringResource, description: LocalizedStringResource?, mode: IntentPerson.ParameterMode, requestValueDialog: IntentDialog?, inputConnectionBehavior: InputConnectionBehavior, resolvers: () -> Spec)](intentparameter/init(title:description:mode:requestvaluedialog:inputconnectionbehavior:resolvers:).md)
  Creates an app intent parameter that can convert the selected value.
- [convenience init(title: LocalizedStringResource, description: LocalizedStringResource?, mode: IntentPerson.ParameterMode, size: [IntentWidgetFamily : IntentCollectionSize], inputConnectionBehavior: InputConnectionBehavior)](intentparameter/init(title:description:mode:size:inputconnectionbehavior:)-1i2sn.md)
  Creates an app intent parameter for an array with a specified size per widget family.
- [convenience init(title: LocalizedStringResource, description: LocalizedStringResource?, mode: IntentPerson.ParameterMode, size: IntentCollectionSize, inputConnectionBehavior: InputConnectionBehavior)](intentparameter/init(title:description:mode:size:inputconnectionbehavior:)-6efsz.md)
  Creates an app intent parameter for an array with a specified size.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/intentparameter/init(title:description:mode:requestvaluedialog:inputconnectionbehavior:optionsprovider:))*