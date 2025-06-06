# type

**Framework**: Core Haptics  
**Kind**: property

The type of the haptic event.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- macOS 10.15+
- tvOS 14.0+
- visionOS 1.0+

## Declaration

```swift
var type: CHHapticEvent.EventType { get }
```

#### Discussion

An audio event can be one of two types: [`audioCustom`](chhapticevent/eventtype/audiocustom.md) or [`audioContinuous`](chhapticevent/eventtype/audiocontinuous.md). Haptic events can be [`hapticTransient`](chhapticevent/eventtype/haptictransient.md) or [`hapticContinuous`](chhapticevent/eventtype/hapticcontinuous.md):

![A chart comparing a transient haptic pattern on the left with a continuous haptic pattern on the right. Transient patterns are instantaneous impulses with almost zero duration, while continuous patterns have a nonzero duration.](https://docs-assets.developer.apple.com/published/26521ebb801409e9176c2d0cbbea7561/media-3197270%402x.png)

A transient event lasts a split-second and registers as a tap or impulse, whereas a continuous event feels like an extended buzz of longer duration.

## See Also

- [CHHapticEvent.EventType](chhapticevent/eventtype.md)
  The types of audio and haptic event waveforms.


---

*[View on Apple Developer](https://developer.apple.com/documentation/corehaptics/chhapticevent/type)*