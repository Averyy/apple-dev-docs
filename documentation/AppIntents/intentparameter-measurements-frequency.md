# Frequency

**Framework**: App Intents

Configure the details for parameter variables that contain frequency values.

## Topics

### Creating an intent parameter
- [convenience init(title: LocalizedStringResource, description: LocalizedStringResource?, defaultValue: Double?, defaultUnit: IntentParameter<Value>.Frequency?, defaultUnitAdjustForLocale: Bool, supportsNegativeNumbers: Bool, requestValueDialog: IntentDialog?, inputConnectionBehavior: InputConnectionBehavior)](intentparameter/init(title:description:defaultvalue:defaultunit:defaultunitadjustforlocale:supportsnegativenumbers:requestvaluedialog:inputconnectionbehavior:)-9tm7b.md)
  Creates an app intent parameter with a default unit for the measurement.
- [convenience init<Spec>(title: LocalizedStringResource, description: LocalizedStringResource?, defaultValue: Double?, defaultUnit: IntentParameter<Value>.Frequency?, defaultUnitAdjustForLocale: Bool, supportsNegativeNumbers: Bool, requestValueDialog: IntentDialog?, inputConnectionBehavior: InputConnectionBehavior, resolvers: () -> Spec)](intentparameter/init(title:description:defaultvalue:defaultunit:defaultunitadjustforlocale:supportsnegativenumbers:requestvaluedialog:inputconnectionbehavior:resolvers:)-6324p.md)
  Creates an app intent parameter with a default unit for the measurement.
- [convenience init(title: LocalizedStringResource, description: LocalizedStringResource?, defaultValue: Double?, unit: IntentParameter<Value>.Frequency, unitAdjustForLocale: Bool, supportsNegativeNumbers: Bool, requestValueDialog: IntentDialog?, inputConnectionBehavior: InputConnectionBehavior)](intentparameter/init(title:description:defaultvalue:unit:unitadjustforlocale:supportsnegativenumbers:requestvaluedialog:inputconnectionbehavior:)-1iwe8.md)
  Creates an app intent parameter that specifies the unit for the measurement.
- [convenience init<Spec>(title: LocalizedStringResource, description: LocalizedStringResource?, defaultValue: Double?, unit: IntentParameter<Value>.Frequency, unitAdjustForLocale: Bool, supportsNegativeNumbers: Bool, requestValueDialog: IntentDialog?, inputConnectionBehavior: InputConnectionBehavior, resolvers: () -> Spec)](intentparameter/init(title:description:defaultvalue:unit:unitadjustforlocale:supportsnegativenumbers:requestvaluedialog:inputconnectionbehavior:resolvers:)-5xtid.md)
  Creates an app intent parameter that specifies the unit for the measurement.
- [convenience init<OptionsProvider>(title: LocalizedStringResource, description: LocalizedStringResource?, requestValueDialog: IntentDialog?, inputConnectionBehavior: InputConnectionBehavior, optionsProvider: OptionsProvider)](intentparameter/init(title:description:requestvaluedialog:inputconnectionbehavior:optionsprovider:)-3vk1g.md)
  Creates an app intent parameter with a list of selectable options.
- [convenience init<Spec, OptionsProvider>(title: LocalizedStringResource, description: LocalizedStringResource?, requestValueDialog: IntentDialog?, inputConnectionBehavior: InputConnectionBehavior, resolvers: () -> Spec, optionsProvider: OptionsProvider)](intentparameter/init(title:description:requestvaluedialog:inputconnectionbehavior:resolvers:optionsprovider:)-4xd9k.md)
  Creates an app intent parameter with a list of selectable options that can convert the selected value.
### Accessing unit details
- [var unit: IntentParameter<Value>.Frequency?](intentparameter/unit-69agf.md)
- [IntentParameter.Frequency](intentparameter/frequency.md)
- [var defaultUnit: IntentParameter<Value>.Frequency?](intentparameter/defaultunit-61co5.md)
- [var supportsNegativeNumbers: Bool?](intentparameter/supportsnegativenumbers-8i8i1.md)
- [var unitAdjustForLocale: Bool?](intentparameter/unitadjustforlocale-52v1p.md)

## See Also

- [Acceleration](intentparameter-measurements-acceleration.md)
  Configure the details for parameter variables that contain acceleration values.
- [Angles](intentparameter-measurements-angle.md)
  Configure the details for parameter variables that contain angles.
- [Area](intentparameter-measurements-area.md)
  Configure the details for parameter variables that contain area values.
- [Concentration mass](intentparameter-measurements-concentration-mass.md)
  Configure the details for parameter variables that contain concentration mass values.
- [Dispersion](intentparameter-measurements-dispersion.md)
  Configure the details for parameter variables that contain dispersion values.
- [Durations](intentparameter-measurements-duration.md)
  Configure the details for parameter variables that contain durations.
- [Electric charge](intentparameter-measurements-electric-charge.md)
  Configure the details for parameter variables that contain electric charge values.
- [Electric current](intentparameter-measurements-electric-current.md)
  Configure the details for parameter variables that contain electric current values.
- [Electric potential difference](intentparameter-measurements-electric-difference.md)
  Configure the details for parameter variables that contain values of electric potential difference.
- [Electric resistance](intentparameter-measurements-electric-resistance.md)
  Configure the details for parameter variables that contain electric resistance values.
- [Energy](intentparameter-measurements-energy.md)
  Configure the details for parameter variables that contain energy values.
- [Fuel efficiency](intentparameter-measurements-fuel-efficiency.md)
  Configure the details for parameter variables that contain fuel efficiency values.
- [Illuminance](intentparameter-measurements-illuminance.md)
  Configure the details for parameter variables that contain illuminance values.
- [Information storage](intentparameter-measurements-information-storage.md)
  Configure the details for parameter variables that contain information storage values.
- [Length](intentparameter-measurements-length.md)
  Configure the details for parameter variables that contain length values.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/intentparameter-measurements-frequency)*