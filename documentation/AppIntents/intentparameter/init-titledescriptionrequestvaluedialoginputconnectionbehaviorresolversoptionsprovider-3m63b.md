# init(title:description:requestValueDialog:inputConnectionBehavior:resolvers:optionsProvider:)

**Framework**: App Intents  
**Kind**: init

Creates an app intent parameter with a list of selectable options that can convert the selected value.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst ?+
- macOS 14.0+
- tvOS 17.0+
- visionOS ?+
- watchOS 10.0+

## Declaration

```swift
convenience init<Spec, OptionsProvider>(title: LocalizedStringResource, description: LocalizedStringResource? = nil, requestValueDialog: IntentDialog? = nil, inputConnectionBehavior: InputConnectionBehavior = .default, @ResolverSpecificationBuilder<Value.UnwrappedType> resolvers: @escaping () -> Spec, optionsProvider: OptionsProvider) where Spec : ResolverSpecification, OptionsProvider : DynamicOptionsProvider, OptionsProvider.DefaultValue.ValueType == Measurement<UnitArea>
```

## Parameters

- `title`: A word or short phrase summarizing this parameter.
- `description`: Additional details about this parameter.
- `requestValueDialog`: A prompt that asks a person to provide the parameter value.
- `inputConnectionBehavior`: An enum that indicates how this parameter receives the output from a preceding app intent.
- `resolvers`: An object that converts a value of another type to this parameter’s type.
- `optionsProvider`: An object that determines selectable options for this parameter.

## See Also

- [convenience init(title: LocalizedStringResource, description: LocalizedStringResource?, defaultValue: Double?, unit: IntentParameter<Value>.Area, unitAdjustForLocale: Bool, supportsNegativeNumbers: Bool, requestValueDialog: IntentDialog?, inputConnectionBehavior: InputConnectionBehavior)](intentparameter/init(title:description:defaultvalue:unit:unitadjustforlocale:supportsnegativenumbers:requestvaluedialog:inputconnectionbehavior:)-5kph6.md)
  Creates an app intent parameter that specifies the unit for the measurement.
- [convenience init(title: LocalizedStringResource, description: LocalizedStringResource?, defaultValue: Double?, defaultUnit: IntentParameter<Value>.Area?, defaultUnitAdjustForLocale: Bool, supportsNegativeNumbers: Bool, requestValueDialog: IntentDialog?, inputConnectionBehavior: InputConnectionBehavior)](intentparameter/init(title:description:defaultvalue:defaultunit:defaultunitadjustforlocale:supportsnegativenumbers:requestvaluedialog:inputconnectionbehavior:)-8qdin.md)
  Creates an app intent parameter with a default unit for the measurement.
- [convenience init<Spec>(title: LocalizedStringResource, description: LocalizedStringResource?, defaultValue: Double?, defaultUnit: IntentParameter<Value>.Area?, defaultUnitAdjustForLocale: Bool, supportsNegativeNumbers: Bool, requestValueDialog: IntentDialog?, inputConnectionBehavior: InputConnectionBehavior, resolvers: () -> Spec)](intentparameter/init(title:description:defaultvalue:defaultunit:defaultunitadjustforlocale:supportsnegativenumbers:requestvaluedialog:inputconnectionbehavior:resolvers:)-5jrle.md)
  Creates an app intent parameter with a default unit for the measurement.
- [convenience init(title: LocalizedStringResource, description: LocalizedStringResource?, defaultValue: Double?, unit: IntentParameter<Value>.Area, unitAdjustForLocale: Bool, supportsNegativeNumbers: Bool, requestValueDialog: IntentDialog?, inputConnectionBehavior: InputConnectionBehavior)](intentparameter/init(title:description:defaultvalue:unit:unitadjustforlocale:supportsnegativenumbers:requestvaluedialog:inputconnectionbehavior:)-5kph6.md)
  Creates an app intent parameter that specifies the unit for the measurement.
- [convenience init<Spec>(title: LocalizedStringResource, description: LocalizedStringResource?, defaultValue: Double?, unit: IntentParameter<Value>.Area, unitAdjustForLocale: Bool, supportsNegativeNumbers: Bool, requestValueDialog: IntentDialog?, inputConnectionBehavior: InputConnectionBehavior, resolvers: () -> Spec)](intentparameter/init(title:description:defaultvalue:unit:unitadjustforlocale:supportsnegativenumbers:requestvaluedialog:inputconnectionbehavior:resolvers:)-8t00h.md)
  Creates an app intent parameter that specifies the unit for the measurement.
- [convenience init<OptionsProvider>(title: LocalizedStringResource, description: LocalizedStringResource?, requestValueDialog: IntentDialog?, inputConnectionBehavior: InputConnectionBehavior, optionsProvider: OptionsProvider)](intentparameter/init(title:description:requestvaluedialog:inputconnectionbehavior:optionsprovider:)-9l0az.md)
  Creates an app intent parameter with a list of selectable options.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/intentparameter/init(title:description:requestvaluedialog:inputconnectionbehavior:resolvers:optionsprovider:)-3m63b)*