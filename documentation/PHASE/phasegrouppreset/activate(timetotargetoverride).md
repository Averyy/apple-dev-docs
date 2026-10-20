# activate(timeToTargetOverride:)

**Framework**: PHASE  
**Kind**: method  
**Role**: Instance Method

Applies settings with an overriden fade duration.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 17.0+
- visionOS 1.0+

## Declaration

```swift
func activate(timeToTargetOverride: Double)
```

```objc
- (void) activateWithTimeToTargetOverride:(double) timeToTargetOverride;
```

## Parameters

- `timeToTargetOverride`: A duration in which the engine fades the settings from their original value to their new value. Overrides [`timeToTarget`](./timetotarget.md).

## See Also

### Activating a Group Preset
- [func activate()](./activate%28%29.md)
  Applies settings to the designated groups.


---

*[View on Apple Developer](https://developer.apple.com/documentation/phase/phasegrouppreset/activate(timetotargetoverride:))*