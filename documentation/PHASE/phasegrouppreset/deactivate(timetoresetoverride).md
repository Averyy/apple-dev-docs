# deactivate(timeToResetOverride:)

**Framework**: PHASE  
**Kind**: method  
**Role**: Instance Method

Reverts settings for the preset’s groups using a timed adjustment.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 17.0+
- visionOS 1.0+

## Declaration

```swift
func deactivate(timeToResetOverride: Double)
```

```objc
- (void) deactivateWithTimeToResetOverride:(double) timeToResetOverride;
```

## Parameters

- `timeToResetOverride`: A duration that overrides [`timeToReset`](./timetoreset.md), in which the engine restores the group’s original state.

## See Also

### Deactivating a Group Preset
- [func deactivate()](./deactivate%28%29.md)
  Reverts settings for the preset’s groups.


---

*[View on Apple Developer](https://developer.apple.com/documentation/phase/phasegrouppreset/deactivate(timetoresetoverride:))*