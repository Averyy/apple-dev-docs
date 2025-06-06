# init(engine:settings:timeToTarget:timeToReset:)

**Framework**: PHASE  
**Kind**: init

Creates a group preset with the designated engine, settings, and fade parameters.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 17.0+
- visionOS 1.0+

## Declaration

```swift
init(engine: PHASEEngine, settings: [String : PHASEGroupPresetSetting], timeToTarget: Double, timeToReset: Double)
```

## Parameters

- `engine`: An engine containing groups to configure with settings.
- `settings`: A dictionary with preset setting values and group objects as keys. See  .
- `timeToTarget`: A duration in which the engine fades the settings from their original value to their new value. See  .
- `timeToReset`: A duration in which the framework restores the group’s original state. See  .


---

*[View on Apple Developer](https://developer.apple.com/documentation/phase/phasegrouppreset/init(engine:settings:timetotarget:timetoreset:))*