# init(title:description:requestValueDialog:inputConnectionBehavior:optionsProvider:resolvers:)

**Framework**: App Intents  
**Kind**: init

Creates an app intent parameter with a list of selectable options that can convert the selected value.

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
convenience init<Spec, OptionsProvider>(title: LocalizedStringResource, description: LocalizedStringResource? = nil, requestValueDialog: IntentDialog? = nil, inputConnectionBehavior: InputConnectionBehavior = .default, optionsProvider: OptionsProvider, @ResolverSpecificationBuilder<Value.UnwrappedType> resolvers: @escaping () -> Spec) where Spec : ResolverSpecification, OptionsProvider : DynamicOptionsProvider, OptionsProvider.DefaultValue.ValueType == URL
```

## Parameters

- `title`: A word or short phrase summarizing this parameter.
- `description`: Additional details about this parameter.
- `requestValueDialog`: A prompt that asks a person to provide the parameter value.
- `inputConnectionBehavior`: An enum that indicates how this parameter receives the output from a preceding app intent.
- `optionsProvider`: An object that determines selectable options for this parameter.
- `resolvers`: An object that converts a value of another type to this parameter’s type.

## See Also

- [convenience init<OptionsProvider>(title: LocalizedStringResource, description: LocalizedStringResource?, requestValueDialog: IntentDialog?, inputConnectionBehavior: InputConnectionBehavior, optionsProvider: OptionsProvider)](intentparameter/init(title:description:requestvaluedialog:inputconnectionbehavior:optionsprovider:)-17a31.md)
  Creates an app intent parameter with a list of selectable options.
- [convenience init(title: LocalizedStringResource, description: LocalizedStringResource?, default: Value.UnwrappedType?, requestValueDialog: IntentDialog?, inputConnectionBehavior: InputConnectionBehavior)](intentparameter/init(title:description:default:requestvaluedialog:inputconnectionbehavior:)-518bz.md)
  Creates an app intent parameter.
- [convenience init(title: LocalizedStringResource, description: LocalizedStringResource?, default: [Value.ValueType?], requestValueDialog: IntentDialog?, inputConnectionBehavior: InputConnectionBehavior)](intentparameter/init(title:description:default:requestvaluedialog:inputconnectionbehavior:)-9wlo0.md)
  Creates an app intent parameter.
- [convenience init<Spec>(title: LocalizedStringResource, description: LocalizedStringResource?, default: [Value.ValueType?], requestValueDialog: IntentDialog?, inputConnectionBehavior: InputConnectionBehavior, resolvers: () -> Spec)](intentparameter/init(title:description:default:requestvaluedialog:inputconnectionbehavior:resolvers:)-6mfw6.md)
  Creates an app intent parameter that can convert the selected value.
- [convenience init<Spec>(title: LocalizedStringResource, description: LocalizedStringResource?, default: Value.UnwrappedType?, requestValueDialog: IntentDialog?, inputConnectionBehavior: InputConnectionBehavior, resolvers: () -> Spec)](intentparameter/init(title:description:default:requestvaluedialog:inputconnectionbehavior:resolvers:)-7lt0.md)
  Creates an app intent parameter that can convert the selected value.
- [convenience init<OptionsProvider>(title: LocalizedStringResource, description: LocalizedStringResource?, requestValueDialog: IntentDialog?, inputConnectionBehavior: InputConnectionBehavior, optionsProvider: OptionsProvider)](intentparameter/init(title:description:requestvaluedialog:inputconnectionbehavior:optionsprovider:)-17a31.md)
  Creates an app intent parameter with a list of selectable options.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/intentparameter/init(title:description:requestvaluedialog:inputconnectionbehavior:optionsprovider:resolvers:)-8g3g7)*