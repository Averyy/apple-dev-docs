# MathSettingsSystemBehaviorObject

**Framework**: Device Management  
**Kind**: dictionary  
**Role**: Object

If present, configures math behavior in the system.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+

## Declaration

```
object MathSettingsSystemBehaviorObject
```

## Properties

- `KeyboardSuggestions` (boolean) *(required)*: Controls whether keyboard suggestions include math solutions. This key is also supported by the keyboard.settings configuration.

  **Default**: `true`
- `MathNotes` (boolean) *(required)*: Controls whether Math Notes is allowed in other apps such as Notes.

  **Default**: `true`

## See Also

### Objects
- [object MathSettingsCalculatorObject](./mathsettingscalculatorobject.md)
  If present, configures the built-in Calculator app.


---

*[View on Apple Developer](https://developer.apple.com/documentation/devicemanagement/mathsettingssystembehaviorobject)*