# init(title:description:supportedTypeIdentifiers:requestValueDialog:inputConnectionBehavior:optionsProvider:)

**Framework**: App Intents  
**Kind**: init

Creates an app intent parameter with a list of selectable options.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst ?+
- macOS 13.0+
- tvOS 16.0+
- visionOS 1.0+
- watchOS 9.0+

## Declaration

```swift
convenience init<OptionsProvider>(title: LocalizedStringResource, description: LocalizedStringResource? = nil, supportedTypeIdentifiers: [String] = ["public.item"], requestValueDialog: IntentDialog? = nil, inputConnectionBehavior: InputConnectionBehavior = .default, optionsProvider: OptionsProvider) where OptionsProvider : DynamicOptionsProvider, OptionsProvider.DefaultValue.ValueType == IntentFile
```

## Parameters

- `title`: A word or short phrase summarizing this parameter.
- `description`: Additional details about this parameter.
- `supportedTypeIdentifiers`: A list of selectable type identifiers for this []. The default value is ‘public.item’.
- `requestValueDialog`: A prompt that asks a person to provide the parameter value.
- `inputConnectionBehavior`: An enum that indicates how this parameter receives the output from a preceding app intent.
- `optionsProvider`: An object that determines selectable options for this parameter.

## See Also

- [convenience init(title: LocalizedStringResource, description: LocalizedStringResource?, default: Value.UnwrappedType?, supportedTypeIdentifiers: [String], requestValueDialog: IntentDialog?, inputConnectionBehavior: InputConnectionBehavior)](intentparameter/init(title:description:default:supportedtypeidentifiers:requestvaluedialog:inputconnectionbehavior:).md)
  Creates an app intent parameter.
- [convenience init<Spec>(title: LocalizedStringResource, description: LocalizedStringResource?, default: Value.UnwrappedType?, supportedTypeIdentifiers: [String], requestValueDialog: IntentDialog?, inputConnectionBehavior: InputConnectionBehavior, resolvers: () -> Spec)](intentparameter/init(title:description:default:supportedtypeidentifiers:requestvaluedialog:inputconnectionbehavior:resolvers:).md)
  Creates an app intent parameter that can convert the selected value.
- [convenience init<Spec, OptionsProvider>(title: LocalizedStringResource, description: LocalizedStringResource?, supportedTypeIdentifiers: [String], requestValueDialog: IntentDialog?, inputConnectionBehavior: InputConnectionBehavior, optionsProvider: OptionsProvider, resolvers: () -> Spec)](intentparameter/init(title:description:supportedtypeidentifiers:requestvaluedialog:inputconnectionbehavior:optionsprovider:resolvers:).md)
  Creates an app intent parameter with a list of selectable options that can convert the selected value.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/intentparameter/init(title:description:supportedtypeidentifiers:requestvaluedialog:inputconnectionbehavior:optionsprovider:))*