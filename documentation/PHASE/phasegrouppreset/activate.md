# activate()

**Framework**: PHASE  
**Kind**: method

Applies settings to the designated groups.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 17.0+
- visionOS 1.0+

## Declaration

```swift
func activate()
```

#### Discussion

When you call this function, the framework assigns the group preset as the engine’s [`activeGroupPreset`](phaseengine/activegrouppreset.md) and deactivates the previous assignee, as needed. The settings take effect according to [`timeToTarget`](phasegrouppreset/timetotarget.md).

## See Also

- [func activate(timeToTargetOverride: Double)](phasegrouppreset/activate(timetotargetoverride:).md)
  Applies settings with an overriden fade duration.


---

*[View on Apple Developer](https://developer.apple.com/documentation/phase/phasegrouppreset/activate())*