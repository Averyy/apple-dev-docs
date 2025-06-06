# setVolume(_:at:)

**Framework**: AVFoundation  
**Kind**: method

Sets the value of the audio volume starting at the specified time.

**Availability**:
- iOS 4.0+
- iPadOS 4.0+
- Mac Catalyst 13.1+
- macOS 10.7+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 1.0+

## Declaration

```swift
func setVolume(_ volume: Float, at time: CMTime)
```

#### Discussion

This method adds a volume ramp starting at `time`. This volume setting remains in effect until the end of the track unless you set a different volume level to start at a later time.

## Parameters

- `volume`: The volume. The value must be between   and  .
- `time`: The start time at which to set the volume.

## See Also

- [func setVolumeRamp(fromStartVolume: Float, toEndVolume: Float, timeRange: CMTimeRange)](avmutableaudiomixinputparameters/setvolumeramp(fromstartvolume:toendvolume:timerange:).md)
  Sets a volume ramp to apply during a specified time range.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avmutableaudiomixinputparameters/setvolume(_:at:))*