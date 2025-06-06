# init(title:description:controlStyle:inclusiveRange:requestValueDialog:inputConnectionBehavior:optionsProvider:resolvers:)

**Framework**: App Intents  
**Kind**: init

Creates an app intent parameter with a list of selectable options that can convert the selected value.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.0+
- visionOS 1.0+
- watchOS 9.0+

## Declaration

```swift
convenience init<Spec, OptionsProvider>(title: LocalizedStringResource, description: LocalizedStringResource? = nil, controlStyle: IntentParameter<Value>.DoubleControlStyle = .stepper, inclusiveRange: IntentParameter<Value>.InclusiveRange<Value.ValueType>? = nil, requestValueDialog: IntentDialog? = nil, inputConnectionBehavior: InputConnectionBehavior = .default, optionsProvider: OptionsProvider, @ResolverSpecificationBuilder<Value.UnwrappedType> resolvers: @escaping () -> Spec) where Spec : ResolverSpecification, OptionsProvider : DynamicOptionsProvider, OptionsProvider.DefaultValue.ValueType == Double
```

## Parameters

- `title`: A word or short phrase summarizing this parameter.
- `description`: Additional details about this parameter.
- `controlStyle`: The type of user input control for this parameter.
- `inclusiveRange`: The allowed minimum and maximum values for this parameter.
- `requestValueDialog`: A prompt that asks a person to provide the parameter value.
- `inputConnectionBehavior`: An enum that indicates how this parameter receives the output from a preceding app intent.
- `optionsProvider`: An object that determines selectable options for this parameter.
- `resolvers`: An object that converts a value of another type to this parameter’s type.

## See Also

- [convenience init<OptionsProvider>(title: LocalizedStringResource, description: LocalizedStringResource?, controlStyle: IntentParameter<Value>.DoubleControlStyle, inclusiveRange: IntentParameter<Value>.InclusiveRange<Value.ValueType>?, requestValueDialog: IntentDialog?, inputConnectionBehavior: InputConnectionBehavior, optionsProvider: OptionsProvider)](intentparameter/init(title:description:controlstyle:inclusiverange:requestvaluedialog:inputconnectionbehavior:optionsprovider:)-3la41.md)
  Creates an app intent parameter with a list of selectable options.
- [convenience init(title: LocalizedStringResource, description: LocalizedStringResource?, default: Value.UnwrappedType?, controlStyle: IntentParameter<Value>.DoubleControlStyle, inclusiveRange: IntentParameter<Value>.InclusiveRange<Value.ValueType>?, requestValueDialog: IntentDialog?, inputConnectionBehavior: InputConnectionBehavior)](intentparameter/init(title:description:default:controlstyle:inclusiverange:requestvaluedialog:inputconnectionbehavior:)-4mc52.md)
  Creates an app intent parameter.
- [convenience init<Spec>(title: LocalizedStringResource, description: LocalizedStringResource?, default: Value.UnwrappedType?, controlStyle: IntentParameter<Value>.DoubleControlStyle, inclusiveRange: IntentParameter<Value>.InclusiveRange<Value.ValueType>?, requestValueDialog: IntentDialog?, inputConnectionBehavior: InputConnectionBehavior, resolvers: () -> Spec)](intentparameter/init(title:description:default:controlstyle:inclusiverange:requestvaluedialog:inputconnectionbehavior:resolvers:)-9yclx.md)
  Creates an app intent parameter that can convert the selected value.
- [IntentParameter.InclusiveRange](intentparameter/inclusiverange-swift.typealias.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/intentparameter/init(title:description:controlstyle:inclusiverange:requestvaluedialog:inputconnectionbehavior:optionsprovider:resolvers:)-2iugu)*