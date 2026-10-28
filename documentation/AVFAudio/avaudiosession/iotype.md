# AVAudioSession.IOType

**Framework**: AVFAudio  
**Kind**: enum  
**Role**: Enumeration

Constant values used to specify the audio session’s aggregated I/O behavior.

**Availability**:
- iOS
- iPadOS
- Mac Catalyst
- tvOS
- visionOS
- watchOS

## Declaration

```swift
enum IOType
```

```c
enum AVAudioSessionIOType : NSUInteger;
```

## Overview

Starting in iOS 10, apps that use [`AVCaptureSession`](../../AVFoundation/avcapturesession.md) on iPad and iPhone devices, and support taking Live Photos, have nonaggregated audio I/O unless the app opts out by setting its I/O type to [`AVAudioSession.IOType.aggregated`](./iotype/aggregated.md). With nonaggregated audio I/O, the system uses separate threads to service audio I/O for input and output directions.

In cases with nonaggregated I/O, the sample rate and I/O buffer duration properties map to the output audio device. In this scenario, the input and output audio hardware may be running at different sample rates and with different I/O buffer durations. If any of the following are true about your app, set the I/O type to [`AVAudioSession.IOType.aggregated`](./iotype/aggregated.md):

- It requires that input and output audio be presented in the same real-time I/O callback.
- It requires that input and output audio have the same sample rate or I/O buffer duration.
- It requires the ability to set a preferred sample rate or I/O buffer duration for audio input.

Apps that don’t use [`AVCaptureSession`](../../AVFoundation/avcapturesession.md), but do use the [`playAndRecord`](./category-swift.struct/playandrecord.md) category, continue to have aggregated audio I/O, as in previous versions of iOS.

## Topics

### Creating an I/O type
- [init?(rawValue: UInt)](./iotype/init%28rawvalue%29.md)
### Choosing an I/O type
- [AVAudioSession.IOType.notSpecified](./iotype/notspecified.md)
  The default audio session I/O type.
- [AVAudioSession.IOType.aggregated](./iotype/aggregated.md)
  An I/O type that indicates if audio input and output should be presented in the same realtime I/O callback.

## Relationships

### Conforms To
- [BitwiseCopyable](../../Swift/bitwisecopyable.md)
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [RawRepresentable](../../Swift/rawrepresentable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Setting the aggregated I/O preference
- [func setAggregatedIOPreference(AVAudioSession.IOType) throws](./setaggregatediopreference%28_%29.md)
  Sets the audio session’s aggregated I/O configuration preference.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfaudio/avaudiosession/iotype)*