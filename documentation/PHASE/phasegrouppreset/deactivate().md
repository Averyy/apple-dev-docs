# deactivate()

**Framework**: PHASE  
**Kind**: method  
**Role**: Instance Method

Reverts settings for the preset’s groups.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 17.0+
- visionOS 1.0+

## Declaration

```swift
func deactivate()
```

```objc
- (void) deactivate;
```

## Discussion

When you call this function, the framework restores the group’s default state by removing the preset’s settings. The settings fade over the [`timeToReset`](./timetoreset.md) duration, and the engine removes the preset from [`activeGroupPreset`](../phaseengine/activegrouppreset.md).

## See Also

### Deactivating a Group Preset
- [func deactivate(timeToResetOverride: Double)](./deactivate%28timetoresetoverride%29.md)
  Reverts settings for the preset’s groups using a timed adjustment.


---

*[View on Apple Developer](https://developer.apple.com/documentation/phase/phasegrouppreset/deactivate())*