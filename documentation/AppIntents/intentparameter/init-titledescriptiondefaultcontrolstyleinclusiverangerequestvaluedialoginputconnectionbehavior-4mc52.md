# init(title:description:default:controlStyle:inclusiveRange:requestValueDialog:inputConnectionBehavior:)

**Framework**: App Intents  
**Kind**: init

Creates an app intent parameter.

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
convenience init(title: LocalizedStringResource, description: LocalizedStringResource? = nil, default defaultValue: Value.UnwrappedType? = nil, controlStyle: IntentParameter<Value>.DoubleControlStyle = .stepper, inclusiveRange: IntentParameter<Value>.InclusiveRange<Value.ValueType>? = nil, requestValueDialog: IntentDialog? = nil, inputConnectionBehavior: InputConnectionBehavior = .default)
```

## Parameters

- `title`: A word or short phrase summarizing this parameter.
- `description`: Additional details about this parameter.
- `defaultValue`: The default value for this parameter. People can specify a different value.
- `controlStyle`: The type of user input control for this parameter.
- `inclusiveRange`: The allowed minimum and maximum values for this parameter.
- `requestValueDialog`: A prompt that asks a person to provide the parameter value.
- `inputConnectionBehavior`: An enum that indicates how this parameter receives the output from a preceding app intent.

## See Also

- [convenience init<OptionsProvider>(title: LocalizedStringResource, description: LocalizedStringResource?, controlStyle: IntentParameter<Value>.DoubleControlStyle, inclusiveRange: IntentParameter<Value>.InclusiveRange<Value.ValueType>?, requestValueDialog: IntentDialog?, inputConnectionBehavior: InputConnectionBehavior, optionsProvider: OptionsProvider)](intentparameter/init(title:description:controlstyle:inclusiverange:requestvaluedialog:inputconnectionbehavior:optionsprovider:)-3la41.md)
  Creates an app intent parameter with a list of selectable options.
- [convenience init<Spec, OptionsProvider>(title: LocalizedStringResource, description: LocalizedStringResource?, controlStyle: IntentParameter<Value>.DoubleControlStyle, inclusiveRange: IntentParameter<Value>.InclusiveRange<Value.ValueType>?, requestValueDialog: IntentDialog?, inputConnectionBehavior: InputConnectionBehavior, optionsProvider: OptionsProvider, resolvers: () -> Spec)](intentparameter/init(title:description:controlstyle:inclusiverange:requestvaluedialog:inputconnectionbehavior:optionsprovider:resolvers:)-2iugu.md)
  Creates an app intent parameter with a list of selectable options that can convert the selected value.
- [convenience init<Spec>(title: LocalizedStringResource, description: LocalizedStringResource?, default: Value.UnwrappedType?, controlStyle: IntentParameter<Value>.DoubleControlStyle, inclusiveRange: IntentParameter<Value>.InclusiveRange<Value.ValueType>?, requestValueDialog: IntentDialog?, inputConnectionBehavior: InputConnectionBehavior, resolvers: () -> Spec)](intentparameter/init(title:description:default:controlstyle:inclusiverange:requestvaluedialog:inputconnectionbehavior:resolvers:)-9yclx.md)
  Creates an app intent parameter that can convert the selected value.
- [IntentParameter.InclusiveRange](intentparameter/inclusiverange-swift.typealias.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/intentparameter/init(title:description:default:controlstyle:inclusiverange:requestvaluedialog:inputconnectionbehavior:)-4mc52)*