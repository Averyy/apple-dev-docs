# IntentParameterContext

**Framework**: App Intents  
**Kind**: struct

A type that provides information about an associated parameter during value resolution.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.0+
- visionOS 1.0+
- watchOS 9.0+

## Declaration

```swift
struct IntentParameterContext<Value> where Value : _IntentValue, Value : Sendable
```

## Topics

### Instance Properties
- [var controlStyle: IntentParameter<Value>.IntControlStyle?](intentparametercontext/controlstyle-2sflf.md)
- [var controlStyle: IntentParameter<Value>.DoubleControlStyle?](intentparametercontext/controlstyle-6k0y7.md)
- [var currencyCodes: [String]?](intentparametercontext/currencycodes.md)
- [var dateKind: IntentParameter<Value>.DateKind?](intentparametercontext/datekind-1znbd.md)
- [var dateKind: IntentParameter<Value>.DateKind?](intentparametercontext/datekind-301pp.md)
- [var defaultUnit: IntentParameter<Measurement<UnitFuelEfficiency>>.FuelEfficiency?](intentparametercontext/defaultunit-14jlt.md)
- [var defaultUnit: IntentParameter<Measurement<UnitLength>>.Length?](intentparametercontext/defaultunit-1b43r.md)
- [var defaultUnit: IntentParameter<Measurement<UnitAcceleration>>.Acceleration?](intentparametercontext/defaultunit-1h4fh.md)
- [var defaultUnit: IntentParameter<Measurement<UnitElectricResistance>>.ElectricResistance?](intentparametercontext/defaultunit-1iv6c.md)
- [var defaultUnit: IntentParameter<Measurement<UnitDispersion>>.Dispersion?](intentparametercontext/defaultunit-2lxed.md)
- [var defaultUnit: IntentParameter<Measurement<UnitVolume>>.Volume?](intentparametercontext/defaultunit-31gc1.md)
- [var defaultUnit: IntentParameter<Measurement<UnitMass>>.Mass?](intentparametercontext/defaultunit-3jg9t.md)
- [var defaultUnit: IntentParameter<Measurement<UnitConcentrationMass>>.ConcentrationMass?](intentparametercontext/defaultunit-3yj46.md)
- [var defaultUnit: IntentParameter<Measurement<UnitElectricPotentialDifference>>.ElectricPotentialDifference?](intentparametercontext/defaultunit-4utvz.md)
- [var defaultUnit: IntentParameter<Measurement<UnitEnergy>>.Energy?](intentparametercontext/defaultunit-60crf.md)
- [var defaultUnit: IntentParameter<Measurement<UnitFrequency>>.Frequency?](intentparametercontext/defaultunit-60fdy.md)
- [var defaultUnit: IntentParameter<Measurement<UnitElectricCharge>>.ElectricCharge?](intentparametercontext/defaultunit-65ijm.md)
- [var defaultUnit: IntentParameter<Measurement<UnitTemperature>>.Temperature?](intentparametercontext/defaultunit-65voi.md)
- [var defaultUnit: IntentParameter<Measurement<UnitAngle>>.Angle?](intentparametercontext/defaultunit-6qm7u.md)
- [var defaultUnit: IntentParameter<Measurement<UnitArea>>.Area?](intentparametercontext/defaultunit-7ix5r.md)
- [var defaultUnit: IntentParameter<Measurement<UnitDuration>>.Duration?](intentparametercontext/defaultunit-7uvfx.md)
- [var defaultUnit: IntentParameter<Measurement<UnitIlluminance>>.Illuminance?](intentparametercontext/defaultunit-847tm.md)
- [var defaultUnit: IntentParameter<Measurement<UnitInformationStorage>>.InformationStorage?](intentparametercontext/defaultunit-8ois6.md)
- [var defaultUnit: IntentParameter<Measurement<UnitPower>>.Power?](intentparametercontext/defaultunit-9ibfi.md)
- [var defaultUnit: IntentParameter<Measurement<UnitPressure>>.Pressure?](intentparametercontext/defaultunit-b5mb.md)
- [var defaultUnit: IntentParameter<Measurement<UnitSpeed>>.Speed?](intentparametercontext/defaultunit-dk7x.md)
- [var defaultUnit: IntentParameter<Measurement<UnitElectricCurrent>>.ElectricCurrent?](intentparametercontext/defaultunit-mzcu.md)
- [var displayName: Bool.IntentDisplayName?](intentparametercontext/displayname.md)
- [var displayStyle: IntentParameter<Value>.PlacemarkDisplayStyle?](intentparametercontext/displaystyle.md)
- [var inclusiveRange: IntentParameter<Value>.InclusiveRange<Decimal>?](intentparametercontext/inclusiverange-276sa.md)
- [var inclusiveRange: IntentParameter<Value>.InclusiveRange<Double>?](intentparametercontext/inclusiverange-7i6st.md)
- [var inclusiveRange: IntentParameter<Value>.InclusiveRange<Int>?](intentparametercontext/inclusiverange-8kc7r.md)
- [var isOptional: Bool](intentparametercontext/isoptional.md)
- [var parameterMode: IntentPerson.ParameterMode?](intentparametercontext/parametermode.md)
- [var supportsNegativeNumbers: Bool?](intentparametercontext/supportsnegativenumbers-11s8.md)
- [var supportsNegativeNumbers: Bool?](intentparametercontext/supportsnegativenumbers-15kgw.md)
- [var supportsNegativeNumbers: Bool?](intentparametercontext/supportsnegativenumbers-1e69e.md)
- [var supportsNegativeNumbers: Bool?](intentparametercontext/supportsnegativenumbers-25jk6.md)
- [var supportsNegativeNumbers: Bool?](intentparametercontext/supportsnegativenumbers-2w87c.md)
- [var supportsNegativeNumbers: Bool?](intentparametercontext/supportsnegativenumbers-39689.md)
- [var supportsNegativeNumbers: Bool?](intentparametercontext/supportsnegativenumbers-3ds0o.md)
- [var supportsNegativeNumbers: Bool?](intentparametercontext/supportsnegativenumbers-3erhs.md)
- [var supportsNegativeNumbers: Bool?](intentparametercontext/supportsnegativenumbers-3ljcc.md)
- [var supportsNegativeNumbers: Bool?](intentparametercontext/supportsnegativenumbers-41o2y.md)
- [var supportsNegativeNumbers: Bool?](intentparametercontext/supportsnegativenumbers-462o4.md)
- [var supportsNegativeNumbers: Bool?](intentparametercontext/supportsnegativenumbers-59mfp.md)
- [var supportsNegativeNumbers: Bool?](intentparametercontext/supportsnegativenumbers-6hpxs.md)
- [var supportsNegativeNumbers: Bool?](intentparametercontext/supportsnegativenumbers-7650x.md)
- [var supportsNegativeNumbers: Bool?](intentparametercontext/supportsnegativenumbers-7i28a.md)
- [var supportsNegativeNumbers: Bool?](intentparametercontext/supportsnegativenumbers-8617w.md)
- [var supportsNegativeNumbers: Bool?](intentparametercontext/supportsnegativenumbers-8i9m4.md)
- [var supportsNegativeNumbers: Bool?](intentparametercontext/supportsnegativenumbers-8ssre.md)
- [var supportsNegativeNumbers: Bool?](intentparametercontext/supportsnegativenumbers-9d7pr.md)
- [var supportsNegativeNumbers: Bool?](intentparametercontext/supportsnegativenumbers-9hw2e.md)
- [var supportsNegativeNumbers: Bool?](intentparametercontext/supportsnegativenumbers-d2w4.md)
- [var supportsNegativeNumbers: Bool?](intentparametercontext/supportsnegativenumbers-jgtm.md)
- [var title: LocalizedStringResource](intentparametercontext/title.md)
- [var unit: IntentParameter<Measurement<UnitPower>>.Power?](intentparametercontext/unit-18npz.md)
- [var unit: IntentParameter<Measurement<UnitElectricPotentialDifference>>.ElectricPotentialDifference?](intentparametercontext/unit-1mmz4.md)
- [var unit: IntentParameter<Measurement<UnitMass>>.Mass?](intentparametercontext/unit-2zxw8.md)
- [var unit: IntentParameter<Measurement<UnitElectricCurrent>>.ElectricCurrent?](intentparametercontext/unit-34157.md)
- [var unit: IntentParameter<Measurement<UnitSpeed>>.Speed?](intentparametercontext/unit-38zpf.md)
- [var unit: IntentParameter<Measurement<UnitElectricResistance>>.ElectricResistance?](intentparametercontext/unit-39r8x.md)
- [var unit: IntentParameter<Measurement<UnitTemperature>>.Temperature?](intentparametercontext/unit-4aapu.md)
- [var unit: IntentParameter<Measurement<UnitPressure>>.Pressure?](intentparametercontext/unit-4awol.md)
- [var unit: IntentParameter<Measurement<UnitDispersion>>.Dispersion?](intentparametercontext/unit-4koze.md)
- [var unit: IntentParameter<Measurement<UnitArea>>.Area?](intentparametercontext/unit-4rx08.md)
- [var unit: IntentParameter<Measurement<UnitLength>>.Length?](intentparametercontext/unit-5p7x6.md)
- [var unit: IntentParameter<Measurement<UnitElectricCharge>>.ElectricCharge?](intentparametercontext/unit-6qvx7.md)
- [var unit: IntentParameter<Measurement<UnitVolume>>.Volume?](intentparametercontext/unit-71usu.md)
- [var unit: IntentParameter<Measurement<UnitInformationStorage>>.InformationStorage?](intentparametercontext/unit-72hcm.md)
- [var unit: IntentParameter<Measurement<UnitFrequency>>.Frequency?](intentparametercontext/unit-75ikr.md)
- [var unit: IntentParameter<Measurement<UnitAngle>>.Angle?](intentparametercontext/unit-78ccp.md)
- [var unit: IntentParameter<Measurement<UnitIlluminance>>.Illuminance?](intentparametercontext/unit-78p18.md)
- [var unit: IntentParameter<Measurement<UnitEnergy>>.Energy?](intentparametercontext/unit-7lril.md)
- [var unit: IntentParameter<Measurement<UnitFuelEfficiency>>.FuelEfficiency?](intentparametercontext/unit-8lih3.md)
- [var unit: IntentParameter<Measurement<UnitConcentrationMass>>.ConcentrationMass?](intentparametercontext/unit-8omlm.md)
- [var unit: IntentParameter<Measurement<UnitAcceleration>>.Acceleration?](intentparametercontext/unit-fzbg.md)
- [var unit: IntentParameter<Measurement<UnitDuration>>.Duration?](intentparametercontext/unit-i68w.md)
- [var unitAdjustForLocale: Bool?](intentparametercontext/unitadjustforlocale-108qa.md)
- [var unitAdjustForLocale: Bool?](intentparametercontext/unitadjustforlocale-10odh.md)
- [var unitAdjustForLocale: Bool?](intentparametercontext/unitadjustforlocale-18j21.md)
- [var unitAdjustForLocale: Bool?](intentparametercontext/unitadjustforlocale-1gvv5.md)
- [var unitAdjustForLocale: Bool?](intentparametercontext/unitadjustforlocale-1ndgn.md)
- [var unitAdjustForLocale: Bool?](intentparametercontext/unitadjustforlocale-3c4a3.md)
- [var unitAdjustForLocale: Bool?](intentparametercontext/unitadjustforlocale-48rfb.md)
- [var unitAdjustForLocale: Bool?](intentparametercontext/unitadjustforlocale-4kowc.md)
- [var unitAdjustForLocale: Bool?](intentparametercontext/unitadjustforlocale-5euoy.md)
- [var unitAdjustForLocale: Bool?](intentparametercontext/unitadjustforlocale-5xz43.md)
- [var unitAdjustForLocale: Bool?](intentparametercontext/unitadjustforlocale-6cf45.md)
- [var unitAdjustForLocale: Bool?](intentparametercontext/unitadjustforlocale-6zbbp.md)
- [var unitAdjustForLocale: Bool?](intentparametercontext/unitadjustforlocale-77fh8.md)
- [var unitAdjustForLocale: Bool?](intentparametercontext/unitadjustforlocale-79tzk.md)
- [var unitAdjustForLocale: Bool?](intentparametercontext/unitadjustforlocale-8w6d0.md)
- [var unitAdjustForLocale: Bool?](intentparametercontext/unitadjustforlocale-8x6an.md)
- [var unitAdjustForLocale: Bool?](intentparametercontext/unitadjustforlocale-9b11y.md)
- [var unitAdjustForLocale: Bool?](intentparametercontext/unitadjustforlocale-9kt4r.md)
- [var unitAdjustForLocale: Bool?](intentparametercontext/unitadjustforlocale-b2at.md)
- [var unitAdjustForLocale: Bool?](intentparametercontext/unitadjustforlocale-fh5h.md)
- [var unitAdjustForLocale: Bool?](intentparametercontext/unitadjustforlocale-q9qf.md)
- [var unitAdjustForLocale: Bool?](intentparametercontext/unitadjustforlocale-srcg.md)
### Instance Methods
- [func needsDisambiguationError(among: [Value.ValueType], dialog: IntentDialog?) -> AppIntentError](intentparametercontext/needsdisambiguationerror(among:dialog:).md)
  Returns a `restartPerform` error with context for the user to disambiguate amongst an array of values from for this parameter and re-perform the intent with the new value.
- [func needsValueError(IntentDialog?) -> AppIntentError](intentparametercontext/needsvalueerror(_:).md)
  Returns a `restartPerform` error with context to request a value from the user for this parameter and re-perform the intent with the new value.
- [func requestConfirmation(for: Value.ValueType, dialog: IntentDialog?) async throws -> Bool](intentparametercontext/requestconfirmation(for:dialog:).md)
  Use `requestConfirmation` when you need to the ask user to confirm the parameter value.
- [func requestConfirmation<ViewType>(for: Value.ValueType, dialog: IntentDialog?, view: ViewType) async throws -> Bool](intentparametercontext/requestconfirmation(for:dialog:view:)-6n0qp.md)
  Use `requestConfirmation` when you need to the ask user to confirm the parameter value.
- [func requestConfirmation<ViewType>(for: Value.ValueType, dialog: IntentDialog?, view: () -> ViewType) async throws -> Bool](intentparametercontext/requestconfirmation(for:dialog:view:)-97i0g.md)
  Use `requestConfirmation` when you need to the ask user to confirm the parameter value.
- [func requestDisambiguation(among: [Value.ValueType], dialog: IntentDialog?) async throws -> Value.ValueType](intentparametercontext/requestdisambiguation(among:dialog:).md)
  Request that the user disambiguate amongst an array of values for this parameter.
- [func requestValue(IntentDialog?) async throws -> Value.ValueType](intentparametercontext/requestvalue(_:).md)
  Request a value from the user for this parameter.

## Relationships

### Conforms To
- [AnyIntentValue](anyintentvalue.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [class IntentParameter](intentparameter.md)
  A property wrapper that indicates the associated property is an input argument of the app intent.
- [class IntentParameterDependency](intentparameterdependency.md)
  A property wrapper that represents an app intent dependency you use to provide dynamic options.
- [enum InputConnectionBehavior](inputconnectionbehavior.md)
  Describes the input behaviors for connecting a parameter to the output of the previous App Intent.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appintents/intentparametercontext)*