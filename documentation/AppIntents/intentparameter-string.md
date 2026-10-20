# Strings

**Framework**: App Intents  
**Role**: API Collection

Configure the details for parameter variables that contain strings or attributed strings.

## Topics

### Creating an intent parameter for a string
- [convenience init(title: LocalizedStringResource, description: LocalizedStringResource?, default: Value.UnwrappedType?, inputOptions: String.IntentInputOptions?, requestValueDialog: IntentDialog?, inputConnectionBehavior: InputConnectionBehavior)](./intentparameter/init%28title,description,default,inputoptions,requestvaluedialog,inputconnectionbehavior%29.md)
  Creates an app intent parameter.
- [convenience init<Spec>(title: LocalizedStringResource, description: LocalizedStringResource?, default: Value.UnwrappedType?, inputOptions: String.IntentInputOptions?, requestValueDialog: IntentDialog?, inputConnectionBehavior: InputConnectionBehavior, resolvers: () -> Spec)](./intentparameter/init%28title,description,default,inputoptions,requestvaluedialog,inputconnectionbehavior,resolvers%29.md)
  Creates an app intent parameter that can convert the selected value.
- [convenience init<OptionsProvider>(title: LocalizedStringResource, description: LocalizedStringResource?, inputOptions: String.IntentInputOptions?, requestValueDialog: IntentDialog?, inputConnectionBehavior: InputConnectionBehavior, optionsProvider: OptionsProvider)](./intentparameter/init%28title,description,inputoptions,requestvaluedialog,inputconnectionbehavior,optionsprovider%29.md)
  Creates an app intent parameter with a list of selectable options.
- [convenience init<Spec, OptionsProvider>(title: LocalizedStringResource, description: LocalizedStringResource?, inputOptions: String.IntentInputOptions?, requestValueDialog: IntentDialog?, inputConnectionBehavior: InputConnectionBehavior, optionsProvider: OptionsProvider, resolvers: () -> Spec)](./intentparameter/init%28title,description,inputoptions,requestvaluedialog,inputconnectionbehavior,optionsprovider,resolvers%29.md)
  Creates an app intent parameter with a list of selectable options that can convert the selected value.
### Creating an intent parameter for an attributed string
- [convenience init(title: LocalizedStringResource, description: LocalizedStringResource?, default: Value.UnwrappedType?, requestValueDialog: IntentDialog?, inputConnectionBehavior: InputConnectionBehavior)](./intentparameter/init%28title,description,default,requestvaluedialog,inputconnectionbehavior%29-5ouxs.md)
  Creates an app intent parameter.
- [convenience init<Spec>(title: LocalizedStringResource, description: LocalizedStringResource?, default: Value.UnwrappedType?, requestValueDialog: IntentDialog?, inputConnectionBehavior: InputConnectionBehavior, resolvers: () -> Spec)](./intentparameter/init%28title,description,default,requestvaluedialog,inputconnectionbehavior,resolvers%29-7u5zw.md)
  Creates an app intent parameter that can convert the selected value.
- [convenience init<OptionsProvider>(title: LocalizedStringResource, description: LocalizedStringResource?, requestValueDialog: IntentDialog?, inputConnectionBehavior: InputConnectionBehavior, optionsProvider: OptionsProvider)](./intentparameter/init%28title,description,requestvaluedialog,inputconnectionbehavior,optionsprovider%29-2i6xs.md)
  Creates an app intent parameter with a list of selectable options.
- [convenience init<Spec, OptionsProvider>(title: LocalizedStringResource, description: LocalizedStringResource?, requestValueDialog: IntentDialog?, inputConnectionBehavior: InputConnectionBehavior, optionsProvider: OptionsProvider, resolvers: () -> Spec)](./intentparameter/init%28title,description,requestvaluedialog,inputconnectionbehavior,optionsprovider,resolvers%29-7dvis.md)
  Creates an app intent parameter with a list of selectable options that can convert the selected value.
### Accessing the input options
- [var inputOptions: String.IntentInputOptions?](./intentparameter/inputoptions.md)

## See Also

### Creating an intent parameter for primitive types
- [Integers](./intentparameter-int.md)
  Configure the details for parameter variables that contain integers.
- [Doubles](./intentparameter-double.md)
  Configure the details for parameter variables that contain floating-point values.
- [Booleans](./intentparameter-boolean.md)
  Configure the details for parameter variables that contain Boolean values.
- [URLs](./intentparameter-url.md)
  Configure the details for parameter variables that contain URLs.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/intentparameter-string)*