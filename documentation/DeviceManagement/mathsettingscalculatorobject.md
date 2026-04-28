# MathSettingsCalculatorObject

**Framework**: Device Management  
**Kind**: dictionary

The declaration to configure the calculator app.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- Device Assignment Services ?+
- VPP License Management ?+

## Declaration

```swift
object MathSettingsCalculatorObject
```

## Topics

### Objects
- [object MathSettingsCalculator_BasicModeObject](mathsettingscalculator_basicmodeobject.md)
  The declaration to configure basic mode in the calculator app.
- [object MathSettingsCalculator_InputModesObject](mathsettingscalculator_inputmodesobject.md)
  The declaration to configure the input modes in the calculator app.
- [object MathSettingsCalculator_MathNotesModeObject](mathsettingscalculator_mathnotesmodeobject.md)
  The declaration to configure Math Notes in the calculator app.
- [object MathSettingsCalculator_ProgrammerModeObject](mathsettingscalculator_programmermodeobject.md)
  The declaration to configure programmer mode in the calculator app.
- [object MathSettingsCalculator_ScientificModeObject](mathsettingscalculator_scientificmodeobject.md)
  The declaration to configure scientific mode in the calculator app.

## Properties

- `BasicMode` (MathSettingsCalculator_BasicModeObject): If present, configures the basic mode of the calculator. Basic mode is always enabled.
- `InputModes` (MathSettingsCalculator_InputModesObject): If present, controls global input options of the calculator. If not present, all input modes are enabled.
- `MathNotesMode` (MathSettingsCalculator_MathNotesModeObject): If present, configures the Math Notes mode of the calculator. If not present, Math Notes mode is enabled.
- `ProgrammerMode` (MathSettingsCalculator_ProgrammerModeObject): If present, configures the programmer mode of the calculator. If not present, programmer mode is enabled.
- `ScientificMode` (MathSettingsCalculator_ScientificModeObject): If present, configures the scientific mode of the calculator. If not present, scientific mode is enabled.

## See Also

- [object MathSettingsSystemBehaviorObject](mathsettingssystembehaviorobject.md)
  The declaration to configure math behavior at the system level.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/mathsettingscalculatorobject)*