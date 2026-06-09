# MathSettingsCalculator_InputModesObject

**Framework**: Device Management  
**Kind**: dictionary

If present, controls global input options of the calculator. If not present, all input modes are enabled.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+

## Declaration

```swift
object MathSettingsCalculator_InputModesObject
```

## Properties

- `RPN` (boolean) *(required)*: Configures whether RPN input is enabled. Available: macOS 15+
- `UnitConversion` (boolean) *(required)*: Configures whether unit conversions are enabled.

## See Also

- [object MathSettingsCalculator_BasicModeObject](mathsettingscalculator_basicmodeobject.md)
  If present, configures the basic mode of the calculator. Basic mode is always enabled.
- [object MathSettingsCalculator_MathNotesModeObject](mathsettingscalculator_mathnotesmodeobject.md)
  If present, configures the Math Notes mode of the calculator. If not present, Math Notes mode is enabled.
- [object MathSettingsCalculator_ProgrammerModeObject](mathsettingscalculator_programmermodeobject.md)
  If present, configures the programmer mode of the calculator. If not present, programmer mode is enabled.
- [object MathSettingsCalculator_ScientificModeObject](mathsettingscalculator_scientificmodeobject.md)
  If present, configures the scientific mode of the calculator. If not present, scientific mode is enabled.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/mathsettingscalculator_inputmodesobject)*