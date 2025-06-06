# Doubles

**Framework**: App Intents

Configure the details for parameter variables that contain floating-point values.

## Topics

### Creating an intent parameter
- [convenience init<OptionsProvider>(title: LocalizedStringResource, description: LocalizedStringResource?, controlStyle: IntentParameter<Value>.DoubleControlStyle, inclusiveRange: IntentParameter<Value>.InclusiveRange<Value.ValueType>?, requestValueDialog: IntentDialog?, inputConnectionBehavior: InputConnectionBehavior, optionsProvider: OptionsProvider)](intentparameter/init(title:description:controlstyle:inclusiverange:requestvaluedialog:inputconnectionbehavior:optionsprovider:)-3la41.md)
  Creates an app intent parameter with a list of selectable options.
- [convenience init<Spec, OptionsProvider>(title: LocalizedStringResource, description: LocalizedStringResource?, controlStyle: IntentParameter<Value>.DoubleControlStyle, inclusiveRange: IntentParameter<Value>.InclusiveRange<Value.ValueType>?, requestValueDialog: IntentDialog?, inputConnectionBehavior: InputConnectionBehavior, optionsProvider: OptionsProvider, resolvers: () -> Spec)](intentparameter/init(title:description:controlstyle:inclusiverange:requestvaluedialog:inputconnectionbehavior:optionsprovider:resolvers:)-2iugu.md)
  Creates an app intent parameter with a list of selectable options that can convert the selected value.
- [convenience init(title: LocalizedStringResource, description: LocalizedStringResource?, default: Value.UnwrappedType?, controlStyle: IntentParameter<Value>.DoubleControlStyle, inclusiveRange: IntentParameter<Value>.InclusiveRange<Value.ValueType>?, requestValueDialog: IntentDialog?, inputConnectionBehavior: InputConnectionBehavior)](intentparameter/init(title:description:default:controlstyle:inclusiverange:requestvaluedialog:inputconnectionbehavior:)-4mc52.md)
  Creates an app intent parameter.
- [convenience init<Spec>(title: LocalizedStringResource, description: LocalizedStringResource?, default: Value.UnwrappedType?, controlStyle: IntentParameter<Value>.DoubleControlStyle, inclusiveRange: IntentParameter<Value>.InclusiveRange<Value.ValueType>?, requestValueDialog: IntentDialog?, inputConnectionBehavior: InputConnectionBehavior, resolvers: () -> Spec)](intentparameter/init(title:description:default:controlstyle:inclusiverange:requestvaluedialog:inputconnectionbehavior:resolvers:)-9yclx.md)
  Creates an app intent parameter that can convert the selected value.
- [IntentParameter.InclusiveRange](intentparameter/inclusiverange-swift.typealias.md)
### Accessing the control style
- [var controlStyle: IntentParameter<Value>.DoubleControlStyle?](intentparameter/controlstyle-5ryd1.md)
- [IntentParameter.DoubleControlStyle](intentparameter/doublecontrolstyle.md)
  An enum that describes the control style of a Double parameter.

## See Also

- [Integers](intentparameter-int.md)
  Configure the details for parameter variables that contain integers.
- [Booleans](intentparameter-boolean.md)
  Configure the details for parameter variables that contain Boolean values.
- [Strings](intentparameter-string.md)
  Configure the details for parameter variables that contain strings or attributed strings.
- [URLs](intentparameter-url.md)
  Configure the details for parameter variables that contain URLs.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/intentparameter-double)*