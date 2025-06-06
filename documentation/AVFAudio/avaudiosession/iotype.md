# AVAudioSession.IOType

**Framework**: AVFAudio  
**Kind**: enum

Constant values used to specify the audio session’s aggregated I/O behavior.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- tvOS ?+
- visionOS ?+
- watchOS ?+

## Declaration

```swift
enum IOType
```

#### Overview

Starting in iOS 10, apps that use [`AVCaptureSession`](https://developer.apple.com/documentation/AVFoundation/AVCaptureSession) on iPad and iPhone devices, and support taking Live Photos, have nonaggregated audio I/O unless the app opts out by setting its I/O type to [`AVAudioSession.IOType.aggregated`](avaudiosession/iotype/aggregated.md). With nonaggregated audio I/O, the system uses separate threads to service audio I/O for input and output directions.

In cases with nonaggregated I/O, the sample rate and I/O buffer duration properties map to the output audio device. In this scenario, the input and output audio hardware may be running at different sample rates and with different I/O buffer durations. If any of the following are true about your app, set the I/O type to [`AVAudioSession.IOType.aggregated`](avaudiosession/iotype/aggregated.md):

- It requires that input and output audio be presented in the same real-time I/O callback.
- It requires that input and output audio have the same sample rate or I/O buffer duration.
- It requires the ability to set a preferred sample rate or I/O buffer duration for audio input.

Apps that don’t use [`AVCaptureSession`](https://developer.apple.com/documentation/AVFoundation/AVCaptureSession), but do use the [`playAndRecord`](avaudiosession/category-swift.struct/playandrecord.md) category, continue to have aggregated audio I/O, as in previous versions of iOS.

## Topics

### I/O Types
- [AVAudioSession.IOType.notSpecified](avaudiosession/iotype/notspecified.md)
  The default audio session I/O type.
- [AVAudioSession.IOType.aggregated](avaudiosession/iotype/aggregated.md)
  An I/O type that indicates if audio input and output should be presented in the same realtime I/O callback.
### Initializers
- [init?(rawValue: UInt)](avaudiosession/iotype/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [func setAggregatedIOPreference(AVAudioSession.IOType) throws](avaudiosession/setaggregatediopreference(_:).md)
  Sets the audio session’s aggregated I/O configuration preference.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfaudio/avaudiosession/iotype)*