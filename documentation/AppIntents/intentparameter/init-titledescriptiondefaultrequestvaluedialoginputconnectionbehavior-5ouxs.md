# init(title:description:default:requestValueDialog:inputConnectionBehavior:)

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
convenience init(title: LocalizedStringResource, description: LocalizedStringResource? = nil, default defaultValue: Value.UnwrappedType? = nil, requestValueDialog: IntentDialog? = nil, inputConnectionBehavior: InputConnectionBehavior = .default)
```

## Parameters

- `title`: A word or short phrase summarizing this parameter.
- `description`: Additional details about this parameter.
- `defaultValue`: The default value for this parameter. People can specify a different value.
- `requestValueDialog`: A prompt that asks a person to provide the parameter value.
- `inputConnectionBehavior`: An enum that indicates how this parameter receives the output from a preceding app intent.

## See Also

- [convenience init<Spec>(title: LocalizedStringResource, description: LocalizedStringResource?, default: Value.UnwrappedType?, requestValueDialog: IntentDialog?, inputConnectionBehavior: InputConnectionBehavior, resolvers: () -> Spec)](intentparameter/init(title:description:default:requestvaluedialog:inputconnectionbehavior:resolvers:)-7u5zw.md)
  Creates an app intent parameter that can convert the selected value.
- [convenience init<OptionsProvider>(title: LocalizedStringResource, description: LocalizedStringResource?, requestValueDialog: IntentDialog?, inputConnectionBehavior: InputConnectionBehavior, optionsProvider: OptionsProvider)](intentparameter/init(title:description:requestvaluedialog:inputconnectionbehavior:optionsprovider:)-2i6xs.md)
  Creates an app intent parameter with a list of selectable options.
- [convenience init<Spec, OptionsProvider>(title: LocalizedStringResource, description: LocalizedStringResource?, requestValueDialog: IntentDialog?, inputConnectionBehavior: InputConnectionBehavior, optionsProvider: OptionsProvider, resolvers: () -> Spec)](intentparameter/init(title:description:requestvaluedialog:inputconnectionbehavior:optionsprovider:resolvers:)-7dvis.md)
  Creates an app intent parameter with a list of selectable options that can convert the selected value.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/intentparameter/init(title:description:default:requestvaluedialog:inputconnectionbehavior:)-5ouxs)*