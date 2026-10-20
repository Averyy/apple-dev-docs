# init(title:description:defaultValue:defaultUnit:defaultUnitAdjustForLocale:supportsNegativeNumbers:requestValueDialog:inputConnectionBehavior:)

**Framework**: App Intents  
**Kind**: init  
**Role**: Initializer

Creates an app intent parameter with a default unit for the measurement.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- tvOS 17.0+
- visionOS
- watchOS 10.0+

## Declaration

```swift
convenience init(title: LocalizedStringResource, description: LocalizedStringResource? = nil, defaultValue: Double? = nil, defaultUnit: IntentParameter<Value>.ElectricPotentialDifference? = nil, defaultUnitAdjustForLocale: Bool = false, supportsNegativeNumbers: Bool = true, requestValueDialog: IntentDialog? = nil, inputConnectionBehavior: InputConnectionBehavior = .default)
```

Available when `Value` conforms to `_IntentValue`, `Value` conforms to `Sendable`, and `Value.ValueType` is `Measurement<UnitElectricPotentialDifference>`.

## Parameters

- `title`: A word or short phrase summarizing this parameter.
- `description`: Additional details about this parameter.
- `defaultValue`: The default value for this parameter. People can specify a different value.
- `defaultUnit`: The default unit that should be selected when this parameter is initially created.
- `defaultUnitAdjustForLocale`: Whether or not the default unit should adjust to match someone’s locale. Default value is `false`.
- `supportsNegativeNumbers`: Whether or not this parameter supports negative number inputs. Default value is `true`.
- `requestValueDialog`: A prompt that asks a person to provide the parameter value.
- `inputConnectionBehavior`: An enum that indicates how this parameter receives the output from a preceding app intent.

## See Also

### Creating an intent parameter
- [convenience init<Spec>(title: LocalizedStringResource, description: LocalizedStringResource?, defaultValue: Double?, defaultUnit: IntentParameter<Value>.ElectricPotentialDifference?, defaultUnitAdjustForLocale: Bool, supportsNegativeNumbers: Bool, requestValueDialog: IntentDialog?, inputConnectionBehavior: InputConnectionBehavior, resolvers: () -> Spec)](./init%28title,description,defaultvalue,defaultunit,defaultunitadjustforlocale,supportsnegativenumbers,requestvaluedialog,inputconnectionbehavior,resolvers%29-5zan3.md)
  Creates an app intent parameter with a default unit for the measurement.
- [convenience init(title: LocalizedStringResource, description: LocalizedStringResource?, defaultValue: Double?, unit: IntentParameter<Value>.ElectricPotentialDifference, unitAdjustForLocale: Bool, supportsNegativeNumbers: Bool, requestValueDialog: IntentDialog?, inputConnectionBehavior: InputConnectionBehavior)](./init%28title,description,defaultvalue,unit,unitadjustforlocale,supportsnegativenumbers,requestvaluedialog,inputconnectionbehavior%29-85h1x.md)
  Creates an app intent parameter that specifies the unit for the measurement.
- [convenience init<Spec>(title: LocalizedStringResource, description: LocalizedStringResource?, defaultValue: Double?, unit: IntentParameter<Value>.ElectricPotentialDifference, unitAdjustForLocale: Bool, supportsNegativeNumbers: Bool, requestValueDialog: IntentDialog?, inputConnectionBehavior: InputConnectionBehavior, resolvers: () -> Spec)](./init%28title,description,defaultvalue,unit,unitadjustforlocale,supportsnegativenumbers,requestvaluedialog,inputconnectionbehavior,resolvers%29-90byi.md)
  Creates an app intent parameter that specifies the unit for the measurement.
- [convenience init<OptionsProvider>(title: LocalizedStringResource, description: LocalizedStringResource?, requestValueDialog: IntentDialog?, inputConnectionBehavior: InputConnectionBehavior, optionsProvider: OptionsProvider)](./init%28title,description,requestvaluedialog,inputconnectionbehavior,optionsprovider%29-5tqr4.md)
  Creates an app intent parameter with a list of selectable options.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/intentparameter/init(title:description:defaultvalue:defaultunit:defaultunitadjustforlocale:supportsnegativenumbers:requestvaluedialog:inputconnectionbehavior:)-20tna)*