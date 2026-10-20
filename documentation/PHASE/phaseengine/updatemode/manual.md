# PHASEEngine.UpdateMode.manual

**Framework**: PHASE  
**Kind**: case  
**Role**: Case

A mode that indicates the app controls when the framework adjusts state.

**Availability**:
- iOS
- iPadOS
- Mac Catalyst
- macOS
- tvOS
- visionOS

## Declaration

```swift
case manual
```

```c
PHASEUpdateModeManual
```

#### Discussion

In this mode, the framework waits for the app to call [`update()`](../update%28%29.md) before processing the app’s API calls and adjusting internal states.

## See Also

### Modes
- [PHASEEngine.UpdateMode.automatic](./automatic.md)
  A mode that indicates PHASE sets the timing of state adjustments.


---

*[View on Apple Developer](https://developer.apple.com/documentation/phase/phaseengine/updatemode/manual)*