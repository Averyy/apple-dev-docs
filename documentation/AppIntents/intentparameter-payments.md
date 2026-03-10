# Payments

**Framework**: App Intents

Configure the details for parameter variables that contain payment-related values.

## Topics

### Creating an intent parameter
- [convenience init<OptionsProvider>(title: LocalizedStringResource, description: LocalizedStringResource?, requestValueDialog: IntentDialog?, inputConnectionBehavior: InputConnectionBehavior, optionsProvider: OptionsProvider)](intentparameter/init(title:description:requestvaluedialog:inputconnectionbehavior:optionsprovider:)-7urpy.md)
  Creates an app intent parameter with a list of selectable options.
- [convenience init<Spec, OptionsProvider>(title: LocalizedStringResource, description: LocalizedStringResource?, requestValueDialog: IntentDialog?, inputConnectionBehavior: InputConnectionBehavior, optionsProvider: OptionsProvider, resolvers: () -> Spec)](intentparameter/init(title:description:requestvaluedialog:inputconnectionbehavior:optionsprovider:resolvers:)-7y2uj.md)
  Creates an app intent parameter with a list of selectable options that can convert the selected value.
- [convenience init<Spec, OptionsProvider>(title: LocalizedStringResource, description: LocalizedStringResource?, requestValueDialog: IntentDialog?, inputConnectionBehavior: InputConnectionBehavior, resolvers: () -> Spec, optionsProvider: OptionsProvider)](intentparameter/init(title:description:requestvaluedialog:inputconnectionbehavior:resolvers:optionsprovider:)-1x2m9.md)
  Creates an app intent parameter with a list of selectable options that can convert the selected value.
- [convenience init<Spec>(title: LocalizedStringResource, description: LocalizedStringResource?, requestValueDialog: IntentDialog?, inputConnectionBehavior: InputConnectionBehavior, resolvers: () -> Spec)](intentparameter/init(title:description:requestvaluedialog:inputconnectionbehavior:resolvers:).md)
  Creates an app intent parameter that can convert the selected value.

## See Also

- [Dates](intentparameter-date.md)
  Configure the details for parameter variables that contain date values.
- [Date components](intentparameter-date-components.md)
  Configure the details for parameter variables that contain date components.
- [Files](intentparameter-file.md)
  Configure the details for parameter variables that contain files.
- [Currencies](intentparameter-currencies.md)
  Configure the details for parameter variables that contain currency values.
- [People](intentparameter-person.md)
  Configure the details for parameter variables that contain references to people.
- [Placemarks](intentparameter-placemark.md)
  Configure the details for parameter variables that contain a geographic location.
- [Measurements](intentparameter-measurements.md)
  Configure the details for parameter variables that contain, among others, temperature, mass, speed, energy, duration, length, and volume values.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/intentparameter-payments)*