# Integers

**Framework**: App Intents

Configure the details for parameter variables that contain integers.

## Topics

### Creating an intent parameter
- [convenience init<OptionsProvider>(title: LocalizedStringResource, description: LocalizedStringResource?, controlStyle: IntentParameter<Value>.IntControlStyle, inclusiveRange: IntentParameter<Value>.InclusiveRange<Value.ValueType>?, requestValueDialog: IntentDialog?, inputConnectionBehavior: InputConnectionBehavior, optionsProvider: OptionsProvider)](intentparameter/init(title:description:controlstyle:inclusiverange:requestvaluedialog:inputconnectionbehavior:optionsprovider:)-86n3q.md)
  Creates an app intent parameter with a list of selectable options.
- [convenience init<Spec, OptionsProvider>(title: LocalizedStringResource, description: LocalizedStringResource?, controlStyle: IntentParameter<Value>.IntControlStyle, inclusiveRange: IntentParameter<Value>.InclusiveRange<Value.ValueType>?, requestValueDialog: IntentDialog?, inputConnectionBehavior: InputConnectionBehavior, optionsProvider: OptionsProvider, resolvers: () -> Spec)](intentparameter/init(title:description:controlstyle:inclusiverange:requestvaluedialog:inputconnectionbehavior:optionsprovider:resolvers:)-8ej37.md)
  Creates an app intent parameter with a list of selectable options that can convert the selected value.
- [convenience init(title: LocalizedStringResource, description: LocalizedStringResource?, default: Value.UnwrappedType?, controlStyle: IntentParameter<Value>.IntControlStyle, inclusiveRange: IntentParameter<Value>.InclusiveRange<Value.ValueType>?, requestValueDialog: IntentDialog?, inputConnectionBehavior: InputConnectionBehavior)](intentparameter/init(title:description:default:controlstyle:inclusiverange:requestvaluedialog:inputconnectionbehavior:)-2wjbq.md)
  Creates an app intent parameter.
- [convenience init<Spec>(title: LocalizedStringResource, description: LocalizedStringResource?, default: Value.UnwrappedType?, controlStyle: IntentParameter<Value>.IntControlStyle, inclusiveRange: IntentParameter<Value>.InclusiveRange<Value.ValueType>?, requestValueDialog: IntentDialog?, inputConnectionBehavior: InputConnectionBehavior, resolvers: () -> Spec)](intentparameter/init(title:description:default:controlstyle:inclusiverange:requestvaluedialog:inputconnectionbehavior:resolvers:)-83igq.md)
  Creates an app intent parameter that can convert the selected value.
- [IntentParameter.InclusiveRange](intentparameter/inclusiverange-swift.typealias.md)
### Accessing the control style
- [var controlStyle: IntentParameter<Value>.IntControlStyle?](intentparameter/controlstyle-4q1s9.md)
- [IntentParameter.IntControlStyle](intentparameter/intcontrolstyle.md)
  An enum that describes the control style of an Integer parameter.

## See Also

- [Doubles](intentparameter-double.md)
  Configure the details for parameter variables that contain floating-point values.
- [Booleans](intentparameter-boolean.md)
  Configure the details for parameter variables that contain Boolean values.
- [Strings](intentparameter-string.md)
  Configure the details for parameter variables that contain strings or attributed strings.
- [URLs](intentparameter-url.md)
  Configure the details for parameter variables that contain URLs.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/intentparameter-int)*