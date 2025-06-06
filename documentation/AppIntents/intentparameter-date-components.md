# Date components

**Framework**: App Intents

Configure the details for parameter variables that contain date components.

## Topics

### Creating an intent parameter
- [convenience init(title: LocalizedStringResource, description: LocalizedStringResource?, kind: IntentParameter<Value>.DateKind, requestValueDialog: IntentDialog?, inputConnectionBehavior: InputConnectionBehavior)](intentparameter/init(title:description:kind:requestvaluedialog:inputconnectionbehavior:)-1no2a.md)
  Creates an app intent parameter.
- [convenience init<OptionsProvider>(title: LocalizedStringResource, description: LocalizedStringResource?, kind: IntentParameter<Value>.DateKind, requestValueDialog: IntentDialog?, inputConnectionBehavior: InputConnectionBehavior, optionsProvider: OptionsProvider)](intentparameter/init(title:description:kind:requestvaluedialog:inputconnectionbehavior:optionsprovider:)-38o37.md)
  Creates an app intent parameter with a list of selectable options.
- [convenience init<Spec, OptionsProvider>(title: LocalizedStringResource, description: LocalizedStringResource?, kind: IntentParameter<Value>.DateKind, requestValueDialog: IntentDialog?, inputConnectionBehavior: InputConnectionBehavior, optionsProvider: OptionsProvider, resolvers: () -> Spec)](intentparameter/init(title:description:kind:requestvaluedialog:inputconnectionbehavior:optionsprovider:resolvers:)-4438x.md)
  Creates an app intent parameter with a list of selectable options that can convert the selected value.
- [convenience init<Spec>(title: LocalizedStringResource, description: LocalizedStringResource?, kind: IntentParameter<Value>.DateKind, requestValueDialog: IntentDialog?, inputConnectionBehavior: InputConnectionBehavior, resolvers: () -> Spec)](intentparameter/init(title:description:kind:requestvaluedialog:inputconnectionbehavior:resolvers:)-8vfnx.md)
  Creates an app intent parameter that can convert the selected value.
### Accessing the date kind
- [var dateKind: IntentParameter<Value>.DateKind?](intentparameter/datekind-7wjso.md)
- [IntentParameter.DateKind](intentparameter/datekind-swift.enum.md)

## See Also

- [Dates](intentparameter-date.md)
  Configure the details for parameter variables that contain date values.
- [Files](intentparameter-file.md)
  Configure the details for parameter variables that contain files.
- [Currencies](intentparameter-currencies.md)
  Configure the details for parameter variables that contain currency values.
- [Payments](intentparameter-payments.md)
  Configure the details for parameter variables that contain payment-related values.
- [People](intentparameter-person.md)
  Configure the details for parameter variables that contain references to people.
- [Placemarks](intentparameter-placemark.md)
  Configure the details for parameter variables that contain a geographic location.
- [Measurements](intentparameter-measurements.md)
  Configure the details for parameter variables that contain, among others, temperature, mass, speed, energy, duration, length, and volume values.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/intentparameter-date-components)*