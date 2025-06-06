# Currencies

**Framework**: App Intents

Configure the details for parameter variables that contain currency values.

## Topics

### Creating an intent parameter
- [convenience init(title: LocalizedStringResource, description: LocalizedStringResource?, currencyCodes: [String], inclusiveRange: IntentParameter<Value>.InclusiveRange<Decimal>?, requestValueDialog: IntentDialog?, inputConnectionBehavior: InputConnectionBehavior)](intentparameter/init(title:description:currencycodes:inclusiverange:requestvaluedialog:inputconnectionbehavior:).md)
  Creates an app intent parameter.
- [convenience init<OptionsProvider>(title: LocalizedStringResource, description: LocalizedStringResource?, currencyCodes: [String], inclusiveRange: IntentParameter<Value>.InclusiveRange<Decimal>?, requestValueDialog: IntentDialog?, inputConnectionBehavior: InputConnectionBehavior, optionsProvider: OptionsProvider)](intentparameter/init(title:description:currencycodes:inclusiverange:requestvaluedialog:inputconnectionbehavior:optionsprovider:).md)
  Creates an app intent parameter with a list of selectable options.
- [convenience init<Spec, OptionsProvider>(title: LocalizedStringResource, description: LocalizedStringResource?, currencyCodes: [String], inclusiveRange: IntentParameter<Value>.InclusiveRange<Decimal>?, requestValueDialog: IntentDialog?, inputConnectionBehavior: InputConnectionBehavior, optionsProvider: OptionsProvider, resolvers: () -> Spec)](intentparameter/init(title:description:currencycodes:inclusiverange:requestvaluedialog:inputconnectionbehavior:optionsprovider:resolvers:).md)
  Creates an app intent parameter with a list of selectable options that can convert the selected value.
- [convenience init<Spec>(title: LocalizedStringResource, description: LocalizedStringResource?, currencyCodes: [String], inclusiveRange: IntentParameter<Value>.InclusiveRange<Decimal>?, requestValueDialog: IntentDialog?, inputConnectionBehavior: InputConnectionBehavior, resolvers: () -> Spec)](intentparameter/init(title:description:currencycodes:inclusiverange:requestvaluedialog:inputconnectionbehavior:resolvers:).md)
  Creates an app intent parameter that can convert the selected value.
### Accessing the configuration
- [var currencyCodes: [String]?](intentparameter/currencycodes.md)
- [var inclusiveRange: IntentParameter<Value>.InclusiveRange<Decimal>?](intentparameter/inclusiverange-swift.property.md)
- [IntentParameter.InclusiveRange](intentparameter/inclusiverange-swift.typealias.md)

## See Also

- [Dates](intentparameter-date.md)
  Configure the details for parameter variables that contain date values.
- [Date components](intentparameter-date-components.md)
  Configure the details for parameter variables that contain date components.
- [Files](intentparameter-file.md)
  Configure the details for parameter variables that contain files.
- [Payments](intentparameter-payments.md)
  Configure the details for parameter variables that contain payment-related values.
- [People](intentparameter-person.md)
  Configure the details for parameter variables that contain references to people.
- [Placemarks](intentparameter-placemark.md)
  Configure the details for parameter variables that contain a geographic location.
- [Measurements](intentparameter-measurements.md)
  Configure the details for parameter variables that contain, among others, temperature, mass, speed, energy, duration, length, and volume values.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/intentparameter-currencies)*