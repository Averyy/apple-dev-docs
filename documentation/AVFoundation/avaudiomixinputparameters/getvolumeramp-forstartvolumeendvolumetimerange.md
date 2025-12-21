# getVolumeRamp(for:startVolume:endVolume:timeRange:)

**Framework**: AVFoundation  
**Kind**: method

Retrieves the volume ramp that includes the specified time.

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
func getVolumeRamp(for time: CMTime, startVolume: UnsafeMutablePointer<Float>?, endVolume: UnsafeMutablePointer<Float>?, timeRange: UnsafeMutablePointer<CMTimeRange>?) -> Bool
```

#### Return Value

[`true`](https://developer.apple.com/documentation/Swift/true) if the values were retrieved successfully, otherwise [`false`](https://developer.apple.com/documentation/Swift/false). Returns [`false`](https://developer.apple.com/documentation/Swift/false) if `time` is beyond the duration of the last volume ramp that has been set.

#### Discussion

The process of setting up volume ramps requires the configuration of an instance of [`AVMutableAudioMixInputParameters`](avmutableaudiomixinputparameters.md).

## Parameters

- `time`: If a ramp with a time range that contains the specified time has been set, information about the effective ramp for that time is supplied. Otherwise, information about the first ramp that starts after the specified time is supplied.
- `startVolume`: This value may be  .
- `endVolume`: This value may be  .
- `timeRange`: This value may be  .


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfoundation/avaudiomixinputparameters/getvolumeramp(for:startvolume:endvolume:timerange:))*