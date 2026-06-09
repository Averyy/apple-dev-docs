# MathSettingsSystemBehaviorObject

**Framework**: Device Management  
**Kind**: dictionary

If present, configures math behavior in the system.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+

## Declaration

```swift
object MathSettingsSystemBehaviorObject
```

## Properties

- `KeyboardSuggestions` (boolean) *(required)*: Controls whether keyboard suggestions include math solutions. This key is also supported by the keyboard.settings configuration.
- `MathNotes` (boolean) *(required)*: Controls whether Math Notes is allowed in other apps such as Notes.

## See Also

- [object MathSettingsCalculatorObject](mathsettingscalculatorobject.md)
  If present, configures the built-in Calculator app.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/mathsettingssystembehaviorobject)*