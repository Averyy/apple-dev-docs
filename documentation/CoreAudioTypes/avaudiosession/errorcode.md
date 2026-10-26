# AVAudioSession.ErrorCode

**Framework**: Core Audio Types  
**Kind**: enum  
**Role**: Enumeration

Codes that describe error conditions that may occur when performing audio session operations.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- macOS 10.15+
- tvOS 13.0+
- visionOS 1.0+
- watchOS 6.0+

## Declaration

```swift
enum ErrorCode
```

```c
enum AVAudioSessionErrorCode : AVAudioInteger;
```

## Topics

### Error codes
- [AVAudioSession.ErrorCode.none](./errorcode/none.md)
  An error code that indicates the operation succeeded.
- [AVAudioSession.ErrorCode.badParam](./errorcode/badparam.md)
  An error code that indicates an attempt to set a property to an illegal value.
- [AVAudioSession.ErrorCode.cannotInterruptOthers](./errorcode/cannotinterruptothers.md)
  An error code that indictates an attempt to make a nonmixable audio session active while the app was in the background.
- [AVAudioSession.ErrorCode.cannotStartPlaying](./errorcode/cannotstartplaying.md)
  An error code that indicates an attempt to start audio playback when it wasn’t allowed.
- [AVAudioSession.ErrorCode.cannotStartRecording](./errorcode/cannotstartrecording.md)
  An error code that indicates an attempt to start audio recording, but the operation failed.
- [AVAudioSession.ErrorCode.expiredSession](./errorcode/expiredsession.md)
  An error code that indicates that an operation failed because the system deallocated the associated session.
- [AVAudioSession.ErrorCode.incompatibleCategory](./errorcode/incompatiblecategory.md)
  An error code that indicates an attempt to perform an operation that the current audio session category doesn’t support.
- [AVAudioSession.ErrorCode.isBusy](./errorcode/isbusy.md)
  An error code that indicates an attempt to deactivate the audio session while it’s still playing or recording.
- [AVAudioSession.ErrorCode.mediaServicesFailed](./errorcode/mediaservicesfailed.md)
  An error code that indictates an attempt to use the audio session during or after a Media Services failure.
- [AVAudioSession.ErrorCode.missingEntitlement](./errorcode/missingentitlement.md)
  An error code that indicates an attempt to perform an operation for which the app doesn’t have the required entitlements.
- [AVAudioSession.ErrorCode.resourceNotAvailable](./errorcode/resourcenotavailable.md)
  An error code that indicates that an operation failed because the device doesn’t have sufficient hardware resources to complete the action.
- [AVAudioSession.ErrorCode.sessionNotActive](./errorcode/sessionnotactive.md)
  An error code that indicates the operation failed because the session isn’t active.
- [AVAudioSession.ErrorCode.siriIsRecording](./errorcode/siriisrecording.md)
  An error code that indicates an attempt to perform an operation that isn’t allowed while Siri is recording.
- [AVAudioSession.ErrorCode.unspecified](./errorcode/unspecified.md)
  An error code that indicates an unspecified error occurred.
- [AVAudioSession.ErrorCode.insufficientPriority](./errorcode/insufficientpriority.md)
  An error code that indicates the app isn’t allowed to set the audio category because it’s in use by another app.
### Initializers
- [init?(rawValue: AVAudioInteger)](./errorcode/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../../Swift/bitwisecopyable.md)
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [RawRepresentable](../../Swift/rawrepresentable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreaudiotypes/avaudiosession/errorcode)*