# reverbLevel

**Framework**: RealityKit  
**Kind**: property

The level of reverberated signal that an entity emits.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- visionOS 1.0+

## Declaration

```swift
var reverbLevel: Audio.Decibel
```

#### Discussion

The reverb level is in relative decibels, in the range  `[-Decibel.infinity, Decibel.zero]`, where `Decibel.zero` is the default.

Reduce this value to make the sounds less reverberant and more intimate. Reduce this value to `-Decibel.infinity` to cause the sounds to collapse into the head of the listener.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/spatialaudiocomponent/reverblevel)*