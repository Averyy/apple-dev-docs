# Illuminance

**Framework**: App Intents  
**Role**: API Collection

Configure the details for parameter variables that contain illuminance values.

## Topics

### Creating an intent parameter
- [convenience init(title: LocalizedStringResource, description: LocalizedStringResource?, defaultValue: Double?, defaultUnit: IntentParameter<Value>.Illuminance?, defaultUnitAdjustForLocale: Bool, supportsNegativeNumbers: Bool, requestValueDialog: IntentDialog?, inputConnectionBehavior: InputConnectionBehavior)](./intentparameter/init%28title,description,defaultvalue,defaultunit,defaultunitadjustforlocale,supportsnegativenumbers,requestvaluedialog,inputconnectionbehavior%29-81yqr.md)
  Creates an app intent parameter with a default unit for the measurement.
- [convenience init<Spec>(title: LocalizedStringResource, description: LocalizedStringResource?, defaultValue: Double?, defaultUnit: IntentParameter<Value>.Illuminance?, defaultUnitAdjustForLocale: Bool, supportsNegativeNumbers: Bool, requestValueDialog: IntentDialog?, inputConnectionBehavior: InputConnectionBehavior, resolvers: () -> Spec)](./intentparameter/init%28title,description,defaultvalue,defaultunit,defaultunitadjustforlocale,supportsnegativenumbers,requestvaluedialog,inputconnectionbehavior,resolvers%29-2486g.md)
  Creates an app intent parameter with a default unit for the measurement.
- [convenience init(title: LocalizedStringResource, description: LocalizedStringResource?, defaultValue: Double?, unit: IntentParameter<Value>.Illuminance, unitAdjustForLocale: Bool, supportsNegativeNumbers: Bool, requestValueDialog: IntentDialog?, inputConnectionBehavior: InputConnectionBehavior)](./intentparameter/init%28title,description,defaultvalue,unit,unitadjustforlocale,supportsnegativenumbers,requestvaluedialog,inputconnectionbehavior%29-73fj3.md)
  Creates an app intent parameter that specifies the unit for the measurement.
- [convenience init<Spec>(title: LocalizedStringResource, description: LocalizedStringResource?, defaultValue: Double?, unit: IntentParameter<Value>.Illuminance, unitAdjustForLocale: Bool, supportsNegativeNumbers: Bool, requestValueDialog: IntentDialog?, inputConnectionBehavior: InputConnectionBehavior, resolvers: () -> Spec)](./intentparameter/init%28title,description,defaultvalue,unit,unitadjustforlocale,supportsnegativenumbers,requestvaluedialog,inputconnectionbehavior,resolvers%29-1ji9i.md)
  Creates an app intent parameter that specifies the unit for the measurement.
- [convenience init<OptionsProvider>(title: LocalizedStringResource, description: LocalizedStringResource?, requestValueDialog: IntentDialog?, inputConnectionBehavior: InputConnectionBehavior, optionsProvider: OptionsProvider)](./intentparameter/init%28title,description,requestvaluedialog,inputconnectionbehavior,optionsprovider%29-8j88q.md)
  Creates an app intent parameter with a list of selectable options.
- [convenience init<Spec, OptionsProvider>(title: LocalizedStringResource, description: LocalizedStringResource?, requestValueDialog: IntentDialog?, inputConnectionBehavior: InputConnectionBehavior, resolvers: () -> Spec, optionsProvider: OptionsProvider)](./intentparameter/init%28title,description,requestvaluedialog,inputconnectionbehavior,resolvers,optionsprovider%29-4hm4.md)
  Creates an app intent parameter with a list of selectable options that can convert the selected value.
### Accessing unit details
- [var unit: IntentParameter<Value>.Illuminance?](./intentparameter/unit-5d6kq.md)
- [IntentParameter.Illuminance](./intentparameter/illuminance.md)
- [var defaultUnit: IntentParameter<Value>.Illuminance?](./intentparameter/defaultunit-2j2ui.md)
- [var supportsNegativeNumbers: Bool?](./intentparameter/supportsnegativenumbers-6mvvw.md)
- [var unitAdjustForLocale: Bool?](./intentparameter/unitadjustforlocale-po5z.md)

## See Also

### Creating an intent parameter for measurements
- [Acceleration](./intentparameter-measurements-acceleration.md)
  Configure the details for parameter variables that contain acceleration values.
- [Angles](./intentparameter-measurements-angle.md)
  Configure the details for parameter variables that contain angles.
- [Area](./intentparameter-measurements-area.md)
  Configure the details for parameter variables that contain area values.
- [Concentration mass](./intentparameter-measurements-concentration-mass.md)
  Configure the details for parameter variables that contain concentration mass values.
- [Dispersion](./intentparameter-measurements-dispersion.md)
  Configure the details for parameter variables that contain dispersion values.
- [Durations](./intentparameter-measurements-duration.md)
  Configure the details for parameter variables that contain durations.
- [Electric charge](./intentparameter-measurements-electric-charge.md)
  Configure the details for parameter variables that contain electric charge values.
- [Electric current](./intentparameter-measurements-electric-current.md)
  Configure the details for parameter variables that contain electric current values.
- [Electric potential difference](./intentparameter-measurements-electric-difference.md)
  Configure the details for parameter variables that contain values of electric potential difference.
- [Electric resistance](./intentparameter-measurements-electric-resistance.md)
  Configure the details for parameter variables that contain electric resistance values.
- [Energy](./intentparameter-measurements-energy.md)
  Configure the details for parameter variables that contain energy values.
- [Frequency](./intentparameter-measurements-frequency.md)
  Configure the details for parameter variables that contain frequency values.
- [Fuel efficiency](./intentparameter-measurements-fuel-efficiency.md)
  Configure the details for parameter variables that contain fuel efficiency values.
- [Information storage](./intentparameter-measurements-information-storage.md)
  Configure the details for parameter variables that contain information storage values.
- [Length](./intentparameter-measurements-length.md)
  Configure the details for parameter variables that contain length values.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/intentparameter-measurements-illuminance)*