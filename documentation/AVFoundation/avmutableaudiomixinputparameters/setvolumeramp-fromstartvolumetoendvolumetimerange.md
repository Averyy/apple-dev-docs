# setVolumeRamp(fromStartVolume:toEndVolume:timeRange:)

**Framework**: AVFoundation  
**Kind**: method

Sets a volume ramp to apply during a specified time range.

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
func setVolumeRamp(fromStartVolume startVolume: Float, toEndVolume endVolume: Float, timeRange: CMTimeRange)
```

## Parameters

- `startVolume`: The starting volume. The value must be between   and 1.0.
- `endVolume`: The end volume. The value must be between   and  .
- `timeRange`: The time range over which to apply the ramp.

## See Also

- [func setVolume(Float, at: CMTime)](avmutableaudiomixinputparameters/setvolume(_:at:).md)
  Sets the value of the audio volume starting at the specified time.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avmutableaudiomixinputparameters/setvolumeramp(fromstartvolume:toendvolume:timerange:))*