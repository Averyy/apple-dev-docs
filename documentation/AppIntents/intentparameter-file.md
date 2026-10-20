# Files

**Framework**: App Intents  
**Role**: API Collection

Configure the details for parameter variables that contain files.

## Topics

### Creating an intent parameter
- [convenience init(title: LocalizedStringResource, description: LocalizedStringResource?, default: Value.UnwrappedType?, supportedTypeIdentifiers: [String], requestValueDialog: IntentDialog?, inputConnectionBehavior: InputConnectionBehavior)](./intentparameter/init%28title,description,default,supportedtypeidentifiers,requestvaluedialog,inputconnectionbehavior%29.md)
  Creates an app intent parameter.
- [convenience init<Spec>(title: LocalizedStringResource, description: LocalizedStringResource?, default: Value.UnwrappedType?, supportedTypeIdentifiers: [String], requestValueDialog: IntentDialog?, inputConnectionBehavior: InputConnectionBehavior, resolvers: () -> Spec)](./intentparameter/init%28title,description,default,supportedtypeidentifiers,requestvaluedialog,inputconnectionbehavior,resolvers%29.md)
  Creates an app intent parameter that can convert the selected value.
- [convenience init<OptionsProvider>(title: LocalizedStringResource, description: LocalizedStringResource?, supportedTypeIdentifiers: [String], requestValueDialog: IntentDialog?, inputConnectionBehavior: InputConnectionBehavior, optionsProvider: OptionsProvider)](./intentparameter/init%28title,description,supportedtypeidentifiers,requestvaluedialog,inputconnectionbehavior,optionsprovider%29.md)
  Creates an app intent parameter with a list of selectable options.
- [convenience init<Spec, OptionsProvider>(title: LocalizedStringResource, description: LocalizedStringResource?, supportedTypeIdentifiers: [String], requestValueDialog: IntentDialog?, inputConnectionBehavior: InputConnectionBehavior, optionsProvider: OptionsProvider, resolvers: () -> Spec)](./intentparameter/init%28title,description,supportedtypeidentifiers,requestvaluedialog,inputconnectionbehavior,optionsprovider,resolvers%29.md)
  Creates an app intent parameter with a list of selectable options that can convert the selected value.

## See Also

### Creating an intent parameter for common framework types
- [Dates](./intentparameter-date.md)
  Configure the details for parameter variables that contain date values.
- [Date components](./intentparameter-date-components.md)
  Configure the details for parameter variables that contain date components.
- [Currencies](./intentparameter-currencies.md)
  Configure the details for parameter variables that contain currency values.
- [Payments](./intentparameter-payments.md)
  Configure the details for parameter variables that contain payment-related values.
- [People](./intentparameter-person.md)
  Configure the details for parameter variables that contain references to people.
- [Placemarks](./intentparameter-placemark.md)
  Configure the details for parameter variables that contain a geographic location.
- [Measurements](./intentparameter-measurements.md)
  Configure the details for parameter variables that contain, among others, temperature, mass, speed, energy, duration, length, and volume values.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/intentparameter-file)*