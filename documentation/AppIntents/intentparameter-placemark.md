# Placemarks

**Framework**: App Intents

Configure the details for parameter variables that contain a geographic location.

## Topics

### Creating an intent parameter
- [convenience init(title: LocalizedStringResource, description: LocalizedStringResource?, displayStyle: IntentParameter<Value>.PlacemarkDisplayStyle, requestValueDialog: IntentDialog?, inputConnectionBehavior: InputConnectionBehavior)](intentparameter/init(title:description:displaystyle:requestvaluedialog:inputconnectionbehavior:).md)
  Creates an app intent parameter.
- [convenience init<OptionsProvider>(title: LocalizedStringResource, description: LocalizedStringResource?, displayStyle: IntentParameter<Value>.PlacemarkDisplayStyle, requestValueDialog: IntentDialog?, inputConnectionBehavior: InputConnectionBehavior, optionsProvider: OptionsProvider)](intentparameter/init(title:description:displaystyle:requestvaluedialog:inputconnectionbehavior:optionsprovider:).md)
  Creates an app intent parameter with a list of selectable options.
- [convenience init<Spec, OptionsProvider>(title: LocalizedStringResource, description: LocalizedStringResource?, displayStyle: IntentParameter<Value>.PlacemarkDisplayStyle, requestValueDialog: IntentDialog?, inputConnectionBehavior: InputConnectionBehavior, optionsProvider: OptionsProvider, resolvers: () -> Spec)](intentparameter/init(title:description:displaystyle:requestvaluedialog:inputconnectionbehavior:optionsprovider:resolvers:).md)
  Creates an app intent parameter with a list of selectable options that can convert the selected value.
- [convenience init<Spec>(title: LocalizedStringResource, description: LocalizedStringResource?, displayStyle: IntentParameter<Value>.PlacemarkDisplayStyle, requestValueDialog: IntentDialog?, inputConnectionBehavior: InputConnectionBehavior, resolvers: () -> Spec)](intentparameter/init(title:description:displaystyle:requestvaluedialog:inputconnectionbehavior:resolvers:).md)
  Creates an app intent parameter that can convert the selected value.
### Accessing the display style
- [var displayStyle: IntentParameter<Value>.PlacemarkDisplayStyle?](intentparameter/displaystyle.md)
- [IntentParameter.PlacemarkDisplayStyle](intentparameter/placemarkdisplaystyle.md)
  Describes a location’s display style in Shortcuts and Siri Suggestions.

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
- [People](intentparameter-person.md)
  Configure the details for parameter variables that contain references to people.
- [Measurements](intentparameter-measurements.md)
  Configure the details for parameter variables that contain, among others, temperature, mass, speed, energy, duration, length, and volume values.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/intentparameter-placemark)*