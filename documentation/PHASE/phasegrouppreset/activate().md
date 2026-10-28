# activate()

**Framework**: PHASE  
**Kind**: method  
**Role**: Instance Method

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

```objc
- (void) activate;
```

## Discussion

When you call this function, the framework assigns the group preset as the engine’s [`activeGroupPreset`](../phaseengine/activegrouppreset.md) and deactivates the previous assignee, as needed. The settings take effect according to [`timeToTarget`](./timetotarget.md).

## See Also

### Activating a Group Preset
- [func activate(timeToTargetOverride: Double)](./activate%28timetotargetoverride%29.md)
  Applies settings with an overriden fade duration.


---

*[View on Apple Developer](https://developer.apple.com/documentation/phase/phasegrouppreset/activate())*