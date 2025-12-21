# PHASEEngine.UpdateMode.manual

**Framework**: PHASE  
**Kind**: case

A mode that indicates the app controls when the framework adjusts state.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- tvOS ?+
- visionOS ?+

## Declaration

```swift
case manual
```

#### Discussion

In this mode, the framework waits for the app to call [`update()`](phaseengine/update().md) before processing the app’s API calls and adjusting internal states.

## See Also

- [PHASEEngine.UpdateMode.automatic](phaseengine/updatemode/automatic.md)
  A mode that indicates PHASE sets the timing of state adjustments.


---

*[View on Apple Developer](https://developer.apple.com/documentation/phase/phaseengine/updatemode/manual)*