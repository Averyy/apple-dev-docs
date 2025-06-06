# People

**Framework**: App Intents

Configure the details for parameter variables that contain references to people.

## Topics

### Creating an intent parameter
- [convenience init(title: LocalizedStringResource, description: LocalizedStringResource?, mode: IntentPerson.ParameterMode, requestValueDialog: IntentDialog?, inputConnectionBehavior: InputConnectionBehavior)](intentparameter/init(title:description:mode:requestvaluedialog:inputconnectionbehavior:).md)
  Creates an app intent parameter.
- [convenience init<OptionsProvider>(title: LocalizedStringResource, description: LocalizedStringResource?, mode: IntentPerson.ParameterMode, requestValueDialog: IntentDialog?, inputConnectionBehavior: InputConnectionBehavior, optionsProvider: OptionsProvider)](intentparameter/init(title:description:mode:requestvaluedialog:inputconnectionbehavior:optionsprovider:).md)
  Creates an app intent parameter with a list of selectable options.
- [convenience init<Spec, OptionsProvider>(title: LocalizedStringResource, description: LocalizedStringResource?, mode: IntentPerson.ParameterMode, requestValueDialog: IntentDialog?, inputConnectionBehavior: InputConnectionBehavior, optionsProvider: OptionsProvider, resolvers: () -> Spec)](intentparameter/init(title:description:mode:requestvaluedialog:inputconnectionbehavior:optionsprovider:resolvers:).md)
  Creates an app intent parameter with a list of selectable options that can convert the selected value.
- [convenience init<Spec>(title: LocalizedStringResource, description: LocalizedStringResource?, mode: IntentPerson.ParameterMode, requestValueDialog: IntentDialog?, inputConnectionBehavior: InputConnectionBehavior, resolvers: () -> Spec)](intentparameter/init(title:description:mode:requestvaluedialog:inputconnectionbehavior:resolvers:).md)
  Creates an app intent parameter that can convert the selected value.
- [convenience init(title: LocalizedStringResource, description: LocalizedStringResource?, mode: IntentPerson.ParameterMode, size: [IntentWidgetFamily : IntentCollectionSize], inputConnectionBehavior: InputConnectionBehavior)](intentparameter/init(title:description:mode:size:inputconnectionbehavior:)-1i2sn.md)
  Creates an app intent parameter for an array with a specified size per widget family.
- [convenience init(title: LocalizedStringResource, description: LocalizedStringResource?, mode: IntentPerson.ParameterMode, size: IntentCollectionSize, inputConnectionBehavior: InputConnectionBehavior)](intentparameter/init(title:description:mode:size:inputconnectionbehavior:)-6efsz.md)
  Creates an app intent parameter for an array with a specified size.
### Accessing the parameter mode
- [var parameterMode: IntentPerson.ParameterMode?](intentparameter/parametermode.md)
- [IntentPerson.ParameterMode](intentperson/parametermode.md)
  The type of interface to show when someone chooses a parameter that contains information about a person.

## See Also

- [Dates](intentparameter-date.md)
  Configure the details for parameter variables that contain date values.
- [Date components](intentparameter-date-components.md)
  Configure the details for parameter variables that contain date components.
- [Files](intentparameter-file.md)
  Configure the details for parameter variables that contain files.
- [Currencies](intentparameter-currencies.md)
  Configure the details for parameter variables that contain currency values.
- [Payments](intentparameter-payments.md)
  Configure the details for parameter variables that contain payment-related values.
- [Placemarks](intentparameter-placemark.md)
  Configure the details for parameter variables that contain a geographic location.
- [Measurements](intentparameter-measurements.md)
  Configure the details for parameter variables that contain, among others, temperature, mass, speed, energy, duration, length, and volume values.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/intentparameter-person)*