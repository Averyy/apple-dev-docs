# MathSettingsSystemBehaviorObject

**Framework**: Device Management  
**Kind**: dictionary

The declaration to configure math behavior at the system level.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- Device Assignment Services ?+
- VPP License Management ?+

## Declaration

```swift
object MathSettingsSystemBehaviorObject
```

## Properties

- `KeyboardSuggestions` (boolean) *(required)*: Controls whether keyboard suggestions include math solutions. This key is also supported by the keyboard.settings configuration.
- `MathNotes` (boolean) *(required)*: Controls whether Math Notes is allowed in other apps such as Notes.

## See Also

- [object MathSettingsCalculatorObject](mathsettingscalculatorobject.md)
  The declaration to configure the calculator app.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/mathsettingssystembehaviorobject)*