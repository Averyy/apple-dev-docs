# MathSettingsCalculator_BasicModeObject

**Framework**: Device Management  
**Kind**: dictionary

If present, configures the basic mode of the calculator. Basic mode is always enabled.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+

## Declaration

```swift
object MathSettingsCalculator_BasicModeObject
```

## Properties

- `AddSquareRoot` (boolean) *(required)*: Add the square root button to the basic calculator by replacing the +/- button. Normally, the square root button is available in scientific mode, so this key can be used to make it available when the scientific mode is restricted.

## See Also

- [object MathSettingsCalculator_InputModesObject](mathsettingscalculator_inputmodesobject.md)
  If present, controls global input options of the calculator. If not present, all input modes are enabled.
- [object MathSettingsCalculator_MathNotesModeObject](mathsettingscalculator_mathnotesmodeobject.md)
  If present, configures the Math Notes mode of the calculator. If not present, Math Notes mode is enabled.
- [object MathSettingsCalculator_ProgrammerModeObject](mathsettingscalculator_programmermodeobject.md)
  If present, configures the programmer mode of the calculator. If not present, programmer mode is enabled.
- [object MathSettingsCalculator_ScientificModeObject](mathsettingscalculator_scientificmodeobject.md)
  If present, configures the scientific mode of the calculator. If not present, scientific mode is enabled.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/mathsettingscalculator_basicmodeobject)*