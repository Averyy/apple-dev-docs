# MathSettingsCalculatorObject

**Framework**: Device Management  
**Kind**: dictionary

If present, configures the built-in Calculator app.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+

## Declaration

```swift
object MathSettingsCalculatorObject
```

## Topics

### Objects
- [object MathSettingsCalculator_BasicModeObject](mathsettingscalculator_basicmodeobject.md)
  If present, configures the basic mode of the calculator. Basic mode is always enabled.
- [object MathSettingsCalculator_InputModesObject](mathsettingscalculator_inputmodesobject.md)
  If present, controls global input options of the calculator. If not present, all input modes are enabled.
- [object MathSettingsCalculator_MathNotesModeObject](mathsettingscalculator_mathnotesmodeobject.md)
  If present, configures the Math Notes mode of the calculator. If not present, Math Notes mode is enabled.
- [object MathSettingsCalculator_ProgrammerModeObject](mathsettingscalculator_programmermodeobject.md)
  If present, configures the programmer mode of the calculator. If not present, programmer mode is enabled.
- [object MathSettingsCalculator_ScientificModeObject](mathsettingscalculator_scientificmodeobject.md)
  If present, configures the scientific mode of the calculator. If not present, scientific mode is enabled.

## Properties

- `BasicMode` (MathSettingsCalculator_BasicModeObject): If present, configures the basic mode of the calculator. Basic mode is always enabled.
- `InputModes` (MathSettingsCalculator_InputModesObject): If present, controls global input options of the calculator. If not present, all input modes are enabled.
- `MathNotesMode` (MathSettingsCalculator_MathNotesModeObject): If present, configures the Math Notes mode of the calculator. If not present, Math Notes mode is enabled.
- `ProgrammerMode` (MathSettingsCalculator_ProgrammerModeObject): If present, configures the programmer mode of the calculator. If not present, programmer mode is enabled. Available: macOS 15+
- `ScientificMode` (MathSettingsCalculator_ScientificModeObject): If present, configures the scientific mode of the calculator. If not present, scientific mode is enabled.

## See Also

- [object MathSettingsSystemBehaviorObject](mathsettingssystembehaviorobject.md)
  If present, configures math behavior in the system.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/mathsettingscalculatorobject)*