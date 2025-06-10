# init(title:description:controlStyle:inclusiveRange:requestValueDialog:inputConnectionBehavior:optionsProvider:)

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
convenience init<OptionsProvider>(title: LocalizedStringResource, description: LocalizedStringResource? = nil, controlStyle: IntentParameter<Value>.IntControlStyle = .stepper, inclusiveRange: IntentParameter<Value>.InclusiveRange<Value.ValueType>? = nil, requestValueDialog: IntentDialog? = nil, inputConnectionBehavior: InputConnectionBehavior = .default, optionsProvider: OptionsProvider) where OptionsProvider : DynamicOptionsProvider, OptionsProvider.DefaultValue.ValueType == Int
```

## Parameters

- `title`: A word or short phrase summarizing this parameter.
- `description`: Additional details about this parameter.
- `controlStyle`: The type of user input control for this parameter.
- `inclusiveRange`: The allowed minimum and maximum values for this parameter.
- `requestValueDialog`: A prompt that asks a person to provide the parameter value.
- `inputConnectionBehavior`: An enum that indicates how this parameter receives the output from a preceding app intent.
- `optionsProvider`: An object that determines selectable options for this parameter.

## See Also

- [convenience init<Spec, OptionsProvider>(title: LocalizedStringResource, description: LocalizedStringResource?, controlStyle: IntentParameter<Value>.IntControlStyle, inclusiveRange: IntentParameter<Value>.InclusiveRange<Value.ValueType>?, requestValueDialog: IntentDialog?, inputConnectionBehavior: InputConnectionBehavior, optionsProvider: OptionsProvider, resolvers: () -> Spec)](intentparameter/init(title:description:controlstyle:inclusiverange:requestvaluedialog:inputconnectionbehavior:optionsprovider:resolvers:)-8ej37.md)
  Creates an app intent parameter with a list of selectable options that can convert the selected value.
- [convenience init(title: LocalizedStringResource, description: LocalizedStringResource?, default: Value.UnwrappedType?, controlStyle: IntentParameter<Value>.IntControlStyle, inclusiveRange: IntentParameter<Value>.InclusiveRange<Value.ValueType>?, requestValueDialog: IntentDialog?, inputConnectionBehavior: InputConnectionBehavior)](intentparameter/init(title:description:default:controlstyle:inclusiverange:requestvaluedialog:inputconnectionbehavior:)-2wjbq.md)
  Creates an app intent parameter.
- [convenience init<Spec>(title: LocalizedStringResource, description: LocalizedStringResource?, default: Value.UnwrappedType?, controlStyle: IntentParameter<Value>.IntControlStyle, inclusiveRange: IntentParameter<Value>.InclusiveRange<Value.ValueType>?, requestValueDialog: IntentDialog?, inputConnectionBehavior: InputConnectionBehavior, resolvers: () -> Spec)](intentparameter/init(title:description:default:controlstyle:inclusiverange:requestvaluedialog:inputconnectionbehavior:resolvers:)-83igq.md)
  Creates an app intent parameter that can convert the selected value.
- [IntentParameter.InclusiveRange](intentparameter/inclusiverange-swift.typealias.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/intentparameter/init(title:description:controlstyle:inclusiverange:requestvaluedialog:inputconnectionbehavior:optionsprovider:)-86n3q)*